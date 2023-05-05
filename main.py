import speech_recognition as sr
from nlp import get_intent
from machine_learning import predict_action
from translation import translate_text

# Initialize the speech recognizer
r = sr.Recognizer()

# Define the voice command function
def voice_command():
    # Initialize the text variable
    text = ""

    # Record the audio
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    # Attempt to recognize the speech
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        # Translate the speech to English
        translated_text = translate_text(text, "en")
        print(f"Translated text: {translated_text}")

        # Get the intent of the speech
        intent = get_intent(translated_text)
        print(f"Intent: {intent}")

        # Predict the action to take based on the intent
        action = predict_action(intent)
        print(f"Action: {action}")

        # Add code here to perform the action
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Call the voice command function
voice_command()
