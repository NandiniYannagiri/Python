from ollama import chat
from tools import open_website, get_time
import json
from voice import listen, speak



MODEL = "llama3.2:3b"


def ask_ollama(user_text):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are the brain of a desktop voice assistant.

You MUST classify the user's request into exactly ONE of these actions:

1. answer
   For normal questions, conversation, explanations,
   programming questions, science, history, mathematics, etc.

2. time
   ONLY when the user explicitly asks for the current time.

3. open_website
   ONLY when the user explicitly asks to open or visit
   a website.

Return ONLY valid JSON.

For a normal question:
{"action":"answer","text":"your answer"}

For current time:
{"action":"time","text":""}

For opening a website:
{"action":"open_website","url":"https://example.com","text":""}

IMPORTANT:
If the user asks "what is Python", the action MUST be "answer".
Never use "time" for a normal question.
"""
            },
            {
                "role": "user",
                "content": user_text
            }
        ]
    )

    return response.message.content


def execute_response(response):

    print("\nOllama raw response:")
    print(response)

    try:

        # Remove markdown code fences if the model adds them
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        data = json.loads(response)

        action = data.get("action")

        # -------------------------
        # NORMAL ANSWER
        # -------------------------

        if action == "answer":

            return data.get(
                "text",
                "I don't have an answer."
            )

        # -------------------------
        # TIME
        # -------------------------

        elif action == "time":

            return get_time()

        # -------------------------
        # WEBSITE
        # -------------------------

        elif action == "open_website":

            url = data.get("url")

            if not url:
                return "I don't know which website to open."

            return open_website(url)

        # -------------------------
        # UNKNOWN ACTION
        # -------------------------

        else:

            return "I don't know how to handle that request."

    except Exception as e:

        print("JSON ERROR:", e)

        return response


def main():

    speak("Hello. I am your assistant. How can I help you?")

    while True:

        user_text = listen()

        if not user_text:
            continue

        if user_text.lower() in [
            "exit",
            "quit",
            "goodbye",
            "stop"
        ]:

            speak("Assistant: Goodbye!")
            break

        response = ask_ollama(user_text)

        answer = execute_response(response)

        speak(answer)



if __name__ == "__main__":
    main()
