from googletrans import Translator

def translate(text, target_lang='en'):
    """
    Uses the Google Translate API to translate text into the target language and returns the translated text.
    """
    # Create a translator object
    translator = Translator()

    # Translate the text
    translation = translator.translate(text, dest=target_lang)

    # Return the translated text
    return translation.text
