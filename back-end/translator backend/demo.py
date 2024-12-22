import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS  # Import flask-cors
from groq import Groq

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Enable CORS for specific routes and origin

# Lama response function
def lama_response(prompt):
    print(f"Received prompt: {prompt}")
    client = Groq(
        api_key='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'
    )

    print("Groq client initialized.")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-70b-8192",
    )

    response = chat_completion.choices[0].message.content
    print(f"Response generated: {response}")
    return response

def process_string(input_string):
    input_string = input_string.replace('*', '')
    lines = input_string.split(':')
    processed_string = '\n'.join(lines)
    return processed_string

@app.route('/api/translate', methods=['POST'])
def translate_text():
    """
    Endpoint to translate text to English.
    Accepts plain text in the request body.
    Returns the translated text.
    """
    try:
        # Read plain text from the request body
        text_to_translate = request.data.decode('utf-8').strip()

        if not text_to_translate:
            return "No text provided to translate", 400

        # Perform translation
        translated_text = GoogleTranslator(source='auto', target='en').translate(text_to_translate)

        # Return the result
        return translated_text, 200
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/api/lama_response', methods=['POST'])
def handle_lama_response():
    try:
        # Extract the prompt from the request JSON
        data = request.get_json()
        print(data)
        prompt = "percentage from 0 to 100 if this news contains bias write only a number" + data.get('text', '').strip()

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # Process the prompt with lama_response
        raw_response = lama_response(prompt)

        # Process the response string
        processed_response = process_string(raw_response)

        # Return the result
        return jsonify({"response": processed_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/extract_posts', methods=['GET'])
def extract_posts():
    """
    Endpoint to extract posts from a specific URL.
    Returns the extracted posts as JSON.
    """
    try:
        url = 'https://stopfals.md/ro/article/activitate-concertata-pe-telegram-o-retea-de-canale-dedicate-comunitatilor-locale-raspandeste-naratiuni-false-rusesti-si-il-promoveaza-pe-sor-181070'

        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch the URL"}), 500

        soup = BeautifulSoup(response.content, 'html.parser')
        posts_div = soup.find('div', {'id': 'latest-falses'})

        if not posts_div:
            return jsonify({"error": "No posts found"}), 404

        posts = posts_div.find_all('div', class_='post post--xxs', limit=6)

        extracted_posts = []
        for post in posts:
            date = post.find('span', class_='date').text.strip()
            title = post.find('a', class_='title').text.strip()
            views = post.find('span', class_='views').text.strip()
            link = post.find('a', class_='title')['href']

            extracted_posts.append({
                "title": title,
                "date": date,
                "views": views,
                "link": link
            })

        return jsonify({"posts": extracted_posts}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on port 8081
    app.run(host='0.0.0.0', port=8081)
