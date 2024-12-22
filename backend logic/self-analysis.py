from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator



# Function to read the text from a file
def read_file():
    try:
        with open('news_article.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found. Please make sure 'news_article.txt' is in the same folder."



# Function to translate the text to English
def translate_to_english(text):
    translator = Translator()
    text2 = "Salut"
    translated = translator.translate(text2, src='ro', dest='en').text
    return translated



# Function to analyze sentiment of the text
def analyze_sentiment(text, analyzer):
    sentiment_scores = analyzer.polarity_scores(text)
    print("Sentiment Scores:", sentiment_scores)

    if sentiment_scores['compound'] >= 0.05:
        print("Overall Sentiment: Positive")
    elif sentiment_scores['compound'] <= -0.05:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")



def main():
    analyzer = SentimentIntensityAnalyzer()

    text = read_file()

    if text != "File not found. Please make sure 'news_article.txt' is in the same folder.":
        #translated_text = translate_to_english(text)
        translated_text = text
        #print("Translated Text:", translated_text)

        analyze_sentiment(translated_text, analyzer)
    else:
        print(text)


if __name__ == "__main__":
    main()
