import pyttsx3
import speech_recognition as sr
import eel
import time

def speak_text(text: str) -> None:
    """
    Function to convert text to speech using pyttsx3 library.

    Args:
        text (str): The text to be converted to speech.

    Returns:
        None
    """
    engine = pyttsx3.init('nsss')  # Use 'nsss' for MacOS, 'sapi5' for Windows

    engine.setProperty('rate', 174)  # Speed percent (can go over 100)
    voices = engine.getProperty('voices') 

    # List all available voices
    # for index, voice in enumerate(voices):
    #     print(f"{index}: ID={voice.id}, Name={voice.name}, Langs={voice.languages}, Gender={voice.gender}")

        
    # engine.setProperty('voice', voices[18].id)
    # For Mac, If you face error related to "pyobjc" when running the `init()` method :
    # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

    engine.say(text)
    engine.runAndWait()

@eel.expose
def take_command() -> str:
    """
    Function to take voice command from the user and convert it to text using speech_recognition library.

    Returns:
        str: The recognized text from the voice command.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, 10, 6) # Adjusted for better responsiveness

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        speak_text(query)  # Echo the recognized text
        eel.showHood()
    except sr.UnknownValueError:
        msg = "Sorry, I did not understand that."
        print(msg)
        eel.DisplayMessage(msg)
        speak_text(msg)
        eel.showHood()
        return ""
    except sr.RequestError as e:
        msg = f"Could not request results; {e}"
        print(msg)
        eel.DisplayMessage(msg)
        speak_text(msg)
        eel.showHood()
        return ""

    return query