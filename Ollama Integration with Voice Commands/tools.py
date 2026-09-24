import webbrowser
import datetime


def open_website(url):
    webbrowser.open(url)
    return f"Opened {url}"


def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")
