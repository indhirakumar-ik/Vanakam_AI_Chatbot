from flask import Flask, render_template, request, jsonify
from datetime import datetime
import webbrowser
import subprocess
import platform
import random
import os
import re

app = Flask(__name__)

CHAT_FILE = "chat_history.txt"


# ============================================================
# SAVE CHAT TO FILE
# ============================================================

def save_chat(user_message, bot_response):

    current_time = datetime.now().strftime(
        "%d-%m-%Y %I:%M:%S %p"
    )

    with open(CHAT_FILE, "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write(f"Time : {current_time}\n")
        file.write(f"User : {user_message}\n")
        file.write(f"Bot  : {bot_response}\n")
        file.write("=" * 60 + "\n\n")


# ============================================================
# OPEN WEBSITE
# ============================================================

def open_website(url, name):

    try:
        webbrowser.open(url)
        return f"Opening {name} 🌐"

    except Exception:
        return f"I couldn't open {name}."


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(query):

    url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)

    return f"Searching Google for '{query}' 🔎"


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(query):

    url = (
        "https://www.youtube.com/results?search_query="
        + query.replace(" ", "+")
    )

    webbrowser.open(url)

    return f"Searching YouTube for '{query}' ▶️"


# ============================================================
# OPEN WINDOWS APPLICATION
# ============================================================

def open_application(app_name):

    try:

        if platform.system() != "Windows":
            return "This application command is configured for Windows."

        applications = {

            "notepad": ["notepad.exe"],

            "calculator": ["calc.exe"],

            "paint": ["mspaint.exe"],

            "cmd": ["cmd.exe"],

            "terminal": ["cmd.exe"],

            "explorer": ["explorer.exe"]
        }

        if app_name in applications:

            subprocess.Popen(
                applications[app_name]
            )

            return f"Opening {app_name} 💻"

        return f"I don't know how to open {app_name}."

    except Exception as error:

        print("Application Error:", error)

        return f"Unable to open {app_name}."


# ============================================================
# PLAY MUSIC
# ============================================================

def play_music(song):

    url = (
        "https://www.youtube.com/results?search_query="
        + song.replace(" ", "+")
    )

    webbrowser.open(url)

    return f"Searching YouTube for {song} 🎵"


# ============================================================
# WEATHER
# ============================================================

def weather(city):

    url = (
        "https://www.google.com/search?q="
        + f"weather+in+{city.replace(' ', '+')}"
    )

    webbrowser.open(url)

    return f"Checking weather in {city} 🌤️"


# ============================================================
# TIME
# ============================================================

def get_time():

    current_time = datetime.now().strftime(
        "%I:%M:%S %p"
    )

    return f"The current time is {current_time} ⏰"


# ============================================================
# DATE
# ============================================================

def get_date():

    current_date = datetime.now().strftime(
        "%d-%m-%Y"
    )

    return f"Today's date is {current_date} 📅"


# ============================================================
# DAY
# ============================================================

def get_day():

    current_day = datetime.now().strftime(
        "%A"
    )

    return f"Today is {current_day} 📆"


# ============================================================
# CALCULATOR
# ============================================================

def calculate(expression):

    try:

        expression = expression.lower()

        expression = expression.replace(
            "plus", "+"
        )

        expression = expression.replace(
            "minus", "-"
        )

        expression = expression.replace(
            "multiply", "*"
        )

        expression = expression.replace(
            "multiplied by", "*"
        )

        expression = expression.replace(
            "divide", "/"
        )

        expression = expression.replace(
            "divided by", "/"
        )

        expression = expression.strip()

        # Allow only numbers and basic operators
        if not re.fullmatch(
            r"[0-9+\-*/(). %]+",
            expression
        ):
            return "I can calculate only basic mathematical expressions 🧮"

        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        return f"The answer is {result} 🧮"

    except Exception:

        return "I couldn't calculate that expression."


# ============================================================
# RANDOM NUMBER
# ============================================================

def random_number():

    number = random.randint(1, 100)

    return f"Your random number is {number} 🎲"


# ============================================================
# COIN TOSS
# ============================================================

def coin_toss():

    result = random.choice(
        ["Heads", "Tails"]
    )

    return f"It's {result}! 🪙"


# ============================================================
# DICE
# ============================================================

def roll_dice():

    result = random.randint(1, 6)

    return f"You rolled {result}! 🎲"


# ============================================================
# PASSWORD GENERATOR
# ============================================================

def generate_password():

    characters = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*"
    )

    password = "".join(
        random.choice(characters)
        for _ in range(12)
    )

    return f"Your generated password is:\n{password} 🔐"


# ============================================================
# ROCK PAPER SCISSORS
# ============================================================

def rock_paper_scissors(user_choice):

    choices = [
        "rock",
        "paper",
        "scissors"
    ]

    computer = random.choice(choices)

    if user_choice not in choices:

        return "Choose rock, paper or scissors."

    if user_choice == computer:

        result = "It's a draw! 🤝"

    elif (
        user_choice == "rock"
        and computer == "scissors"
    ) or (
        user_choice == "paper"
        and computer == "rock"
    ) or (
        user_choice == "scissors"
        and computer == "paper"
    ):

        result = "You win! 🎉"

    else:

        result = "I win! 🤖"

    return (
        f"You chose {user_choice}.\n"
        f"I chose {computer}.\n"
        f"{result}"
    )


# ============================================================
# SYSTEM INFORMATION
# ============================================================

def system_info():

    system = platform.system()
    version = platform.version()
    machine = platform.machine()

    return (
        f"💻 System Information\n\n"
        f"Operating System : {system}\n"
        f"Version         : {version}\n"
        f"Machine         : {machine}"
    )


# ============================================================
# COMMAND LIST
# ============================================================

def show_help():

    return """
🤖 VANAKAM AI COMMANDS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👋 CONVERSATION

hi
hello
how are you
what is your name
who are you
enna pandra
saptiya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏰ DATE & TIME

time
date
day

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 WEBSITES

open google
open youtube
open github
open chatgpt
open gmail
open spotify

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔎 SEARCH

google python tutorial
search google for java dsa

youtube java tutorial
search youtube for python course

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💻 APPLICATIONS

open notepad
open calculator
open paint
open terminal
open cmd
open file explorer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎵 MUSIC

play music believer
play music arijit singh

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌤️ WEATHER

weather in chennai
weather in coimbatore

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧮 CALCULATOR

calculate 25 + 50
calculate 100 / 5
calculate 10 * 20

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎮 GAMES

roll dice
flip coin
rock
paper
scissors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 TOOLS

generate password
system information

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

😂 FUN

joke
fun fact
motivation
bored

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You can also ask normal questions.
If I don't recognize a command,
I will give the default response.
"""


# ============================================================
# MAIN CHATBOT LOGIC
# ============================================================

def get_bot_response(user_input):

    text = user_input.lower().strip()


    # ========================================================
    # EMPTY
    # ========================================================

    if text == "":
        return "Please type something 😄"


    # ========================================================
    # GREETINGS
    # ========================================================

    if text in [
        "hi",
        "hii",
        "hello",
        "hey",
        "vanakkam"
    ]:

        return "Hello da! 👋 எப்படி இருக்க?"


    if "good morning" in text:

        return "Good Morning! ☀️ Have a great day!"


    if "good afternoon" in text:

        return "Good Afternoon! 😊"


    if "good evening" in text:

        return "Good Evening! 🌙"


    if "good night" in text:

        return "Good Night! 🌙 Sleep well 😴"


    # ========================================================
    # PERSONAL CONVERSATION
    # ========================================================

    if "say my name" in text:

        return "Theriyathu sollu..? 😄"


    if "nalla iruka nee epdi iruka" in text:

        return "Naa eppovume nalla thada irupe 😎"


    if "how are you" in text:

        return "I'm doing great da! 🤖 How are you?"


    if "how r u" in text:

        return "I'm good da 😎"


    if "what are you doing" in text:

        return "I'm waiting to chat with you 😄"


    if "enna pandra" in text:

        return "Summa tha da 😎 Nee enna pandra?"


    if "saptiya" in text:

        return (
            "Naan AI da 😂 "
            "எனக்கு சாப்பாடு தேவையில்லை!"
        )


    if "what is your name" in text:

        return "My name is Vanakam AI 🤖"


    if "who are you" in text:

        return (
            "I'm Vanakam, "
            "your personal chatbot assistant 🤖"
        )


    if "who created you" in text:

        return (
            "I was created using "
            "Python, Flask, HTML, CSS and JavaScript 🚀"
        )


    # ========================================================
    # USER NAME
    # ========================================================

    if "my name is" in text:

        name = text.replace(
            "my name is",
            "",
            1
        ).strip()

        if name:

            return (
                f"Nice to meet you, "
                f"{name.title()}! 😊"
            )

        return "Tell me your name properly 😄"


    # ========================================================
    # PROGRAMMING
    # ========================================================

    if text == "python":

        return (
            "Python is a high-level, interpreted "
            "programming language known for readability, "
            "simplicity and versatility. 🐍"
        )


    if text == "java":

        return (
            "Java is an object-oriented programming "
            "language designed around the idea of "
            "Write Once, Run Anywhere. ☕"
        )


    if text == "html":

        return (
            "HTML creates the structure and content "
            "of webpages. 🌐"
        )


    if text == "css":

        return (
            "CSS controls the design, layout, colors "
            "and appearance of webpages. 🎨"
        )


    if text in ["javascript", "js"]:

        return (
            "JavaScript adds interactivity and dynamic "
            "behavior to webpages. ⚡"
        )


    if text == "flask":

        return (
            "Flask is a lightweight Python web framework "
            "used to build web applications and APIs. 🔥"
        )


    if "programming" in text or "coding" in text:

        return (
            "Coding is all about solving problems "
            "step by step. 💻"
        )


    if "what is api" in text:

        return (
            "An API allows different software applications "
            "to communicate with each other. 🔗"
        )


    if "what is dsa" in text:

        return (
            "DSA means Data Structures and Algorithms. "
            "It helps you store data efficiently and "
            "solve programming problems. 🧠"
        )


    # ========================================================
    # TIME / DATE
    # ========================================================

    if text in [
        "time",
        "what is the time",
        "current time"
    ]:

        return get_time()


    if text in [
        "date",
        "what is the date",
        "today's date"
    ]:

        return get_date()


    if text in [
        "day",
        "what day is today"
    ]:

        return get_day()


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    if text.startswith(
        "search google for "
    ):

        query = text.replace(
            "search google for ",
            "",
            1
        ).strip()

        if query:

            return google_search(query)


    if text.startswith("google "):

        query = text.replace(
            "google ",
            "",
            1
        ).strip()

        if query:

            return google_search(query)


    # ========================================================
    # YOUTUBE SEARCH
    # ========================================================

    if text.startswith(
        "search youtube for "
    ):

        query = text.replace(
            "search youtube for ",
            "",
            1
        ).strip()

        if query:

            return youtube_search(query)


    if text.startswith("youtube "):

        query = text.replace(
            "youtube ",
            "",
            1
        ).strip()

        if query:

            return youtube_search(query)


    # ========================================================
    # WEATHER
    # ========================================================

    if text.startswith("weather in "):

        city = text.replace(
            "weather in ",
            "",
            1
        ).strip()

        if city:

            return weather(city)


    # ========================================================
    # OPEN WEBSITES
    # ========================================================

    if text == "open google":

        return open_website(
            "https://www.google.com",
            "Google"
        )


    if text == "open youtube":

        return open_website(
            "https://www.youtube.com",
            "YouTube"
        )


    if text == "open github":

        return open_website(
            "https://github.com",
            "GitHub"
        )


    if text == "open chatgpt":

        return open_website(
            "https://chatgpt.com",
            "ChatGPT"
        )


    if text == "open gmail":

        return open_website(
            "https://mail.google.com",
            "Gmail"
        )


    if text == "open spotify":

        return open_website(
            "https://open.spotify.com",
            "Spotify"
        )


    if text == "open linkedin":

        return open_website(
            "https://www.linkedin.com",
            "LinkedIn"
        )


    # ========================================================
    # OPEN WINDOWS APPLICATIONS
    # ========================================================

    if text == "open notepad":

        return open_application(
            "notepad"
        )


    if text in [
        "open calculator",
        "open calc"
    ]:

        return open_application(
            "calculator"
        )


    if text == "open paint":

        return open_application(
            "paint"
        )


    if text in [
        "open terminal",
        "open cmd",
        "open command prompt"
    ]:

        return open_application(
            "cmd"
        )


    if text in [
        "open file explorer",
        "open explorer"
    ]:

        return open_application(
            "explorer"
        )


    # ========================================================
    # MUSIC
    # ========================================================

    if text.startswith("play music "):

        song = text.replace(
            "play music ",
            "",
            1
        ).strip()

        if song:

            return play_music(song)


    if text.startswith("play "):

        song = text.replace(
            "play ",
            "",
            1
        ).strip()

        if song:

            return play_music(song)


    # ========================================================
    # CALCULATOR
    # ========================================================

    if text.startswith("calculate "):

        expression = text.replace(
            "calculate ",
            "",
            1
        ).strip()

        return calculate(expression)


    # ========================================================
    # RANDOM NUMBER
    # ========================================================

    if text in [
        "random number",
        "give me a random number"
    ]:

        return random_number()


    # ========================================================
    # COIN
    # ========================================================

    if text in [
        "flip coin",
        "toss coin",
        "coin toss"
    ]:

        return coin_toss()


    # ========================================================
    # DICE
    # ========================================================

    if text in [
        "roll dice",
        "roll a dice"
    ]:

        return roll_dice()


    # ========================================================
    # PASSWORD
    # ========================================================

    if text in [
        "generate password",
        "create password",
        "make password"
    ]:

        return generate_password()


    # ========================================================
    # ROCK PAPER SCISSORS
    # ========================================================

    if text in [
        "rock",
        "paper",
        "scissors"
    ]:

        return rock_paper_scissors(text)


    # ========================================================
    # SYSTEM INFORMATION
    # ========================================================

    if text in [
        "system information",
        "system info",
        "computer information"
    ]:

        return system_info()


    # ========================================================
    # JOKE
    # ========================================================

    if "joke" in text:

        return (
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs! 😂🐛"
        )


    # ========================================================
    # FUN FACT
    # ========================================================

    if "fun fact" in text:

        return (
            "The first computer bug was an actual moth "
            "found inside a computer! 🦋💻"
        )


    # ========================================================
    # MOTIVATION
    # ========================================================

    if (
        "motivate" in text
        or "motivation" in text
    ):

        return (
            "Don't worry about being perfect. "
            "Keep learning and improving every day! 🚀"
        )


    # ========================================================
    # BORED
    # ========================================================

    if "bored" in text:

        return (
            "Let's do something! 😎\n\n"
            "Try:\n"
            "• joke\n"
            "• fun fact\n"
            "• roll dice\n"
            "• flip coin\n"
            "• generate password"
        )


    # ========================================================
    # THANKS
    # ========================================================

    if "thank" in text:

        return "You're always welcome! 😊❤️"


    # ========================================================
    # GOODBYE
    # ========================================================

    if text in [
        "bye",
        "bye bye",
        "goodbye",
        "ok bye"
    ]:

        return "Bye bye da! 👋 Take care!"


    # ========================================================
    # OK
    # ========================================================

    if text in [
        "ok",
        "okay",
        "seri",
        "seri da"
    ]:

        return (
            "Seri da 😄 "
            "என்ன வேணும்னாலும் கேளு!"
        )


    # ========================================================
    # HELP
    # ========================================================

    if text in [
        "help",
        "commands",
        "show commands"
    ]:

        return show_help()


    # ========================================================
    # DEFAULT
    # ========================================================

    return (
        "Hmm 🤔 I don't understand that yet.\n\n"
        "Type 'help' to see all available commands."
    )


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# CHAT API
# ============================================================

@app.route(
    "/chat",
    methods=["POST"]
)
def chat():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "response":
                    "Invalid request ❌"
            }), 400


        user_input = data.get(
            "message",
            ""
        ).strip()


        # Get chatbot response
        response = get_bot_response(
            user_input
        )


        # Save conversation
        save_chat(
            user_input,
            response
        )


        # Send response
        return jsonify({
            "response":
                response
        })


    except Exception as error:

        print(
            "Error:",
            error
        )

        return jsonify({
            "response":
                "Something went wrong 😢"
        }), 500


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )