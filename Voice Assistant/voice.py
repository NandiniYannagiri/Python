import speech_recognition as sr
import pyttsx3


# -----------------------------
# SPEECH RECOGNITION
# -----------------------------

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            print("Recognizing...")

            text = recognizer.recognize_google(audio)

            print("You:", text)

            return text

        except sr.WaitTimeoutError:

            print("No speech detected.")
            return ""

        except sr.UnknownValueError:

            print("I couldn't understand you.")
            return ""

        except sr.RequestError as e:

            print("Speech recognition error:", e)
            return ""


# -----------------------------
# TEXT TO SPEECH
# -----------------------------

def speak(text):

    text = str(text)

    print("Assistant:", text)

    # Create a fresh engine for every response
    engine = pyttsx3.init()

    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()

    engine.stop()
