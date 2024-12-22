from googletrans import Translator

# Create a Translator object
translator = Translator()

# Text to be translated
text = "Hello, how are you?"

# Translate the text to a target language (e.g., Spanish)
translated = translator.translate(text, src='en', dest='es')

# Print the translated text
print(f"Original text: {text}")
print(f"Translated text: {translated.text}")
