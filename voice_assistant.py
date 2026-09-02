import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Text-to-speech setup
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Sorry, there is a problem with the speech service.")
        return ""


def assistant():
    speak("Hello! I am your Voice assistant, Siri.")
    speak("How can I help you?")

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! Nice to meet you.")

        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)

        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "search" in command:
            search_query = command.replace("search", "").strip()

            if search_query:
                speak("Searching for " + search_query)
                url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
                webbrowser.open(url)
            else:
                speak("What should I search for?")

        elif "exit" in command or "stop" in command or "goodbye" in command:
            speak("Goodbye! Have a great day.")
            break

        elif command:
            speak("I don't know that command yet.")


if __name__ == "__main__":
    assistant()
