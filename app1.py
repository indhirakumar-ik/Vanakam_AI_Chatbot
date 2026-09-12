from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

CHAT_FILE = "chat_history.txt"


def save_chat(user_message, bot_response):

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open(CHAT_FILE, "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write(f"Time    : {current_time}\n")
        file.write(f"User    : {user_message}\n")
        file.write(f"Bot     : {bot_response}\n")
        file.write("=" * 60 + "\n\n")


def get_bot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in ["hi", "hii", "hello", "hey", "vanakkam"]:
        return "Hello da! 👋 எப்படி இருக்க?"
    
    elif "nalla iruka nee epdi iruka" in user_input:
        return "Naa eppovume nalla thada irupe.."

    elif "good morning" in user_input:
        return "Good Morning! ☀️ Have a great day!"

    elif "good afternoon" in user_input:
        return "Good Afternoon! 😊"

    elif "good evening" in user_input:
        return "Good Evening! 🌙"

    elif "how are you" in user_input:
        return "I'm doing great da! 🤖 How are you?"

    elif "how r u" in user_input:
        return "I'm good da 😎"

    elif "what are you doing" in user_input:
        return "I'm waiting to chat with you 😄"

    elif "enna pandra" in user_input:
        return "Summa tha da 😎 Nee enna pandra?"

    elif "saptiya" in user_input:
        return "Naan AI da 😂 எனக்கு சாப்பாடு தேவையில்லை!"

    elif "what is your name" in user_input:
        return "My name is Vanakam AI 🤖"

    elif "who are you" in user_input:
        return "I'm Vanakam, your personal chatbot assistant 🤖"

    elif "who created you" in user_input:
        return "I was created using Python, Flask, HTML, CSS and JavaScript 🚀"

    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        if name:
            return f"Nice to meet you, {name.title()}! 😊"
        else:
            return "Tell me your name properly 😄"
        
    elif "python" in user_input:
        return "Python is a beginner-friendly programming language 🐍"

    elif "java" in user_input:
        return "Java is an object-oriented programming language ☕"

    elif "html" in user_input:
        return "HTML is used to create the structure of a website 🌐"

    elif "css" in user_input:
        return "CSS is used to style and design a website 🎨"

    elif "javascript" in user_input or "js" == user_input:
        return "JavaScript makes websites interactive ⚡"

    elif "flask" in user_input:
        return "Flask is a lightweight Python web framework 🔥"

    elif "programming" in user_input or "coding" in user_input:
        return "Coding is all about solving problems step by step 💻"

    elif "what is api" in user_input:
        return "An API helps different applications communicate with each other 🔗"

    elif "time" in user_input:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current server time is {current_time} ⏰"

    elif "date" in user_input:

        current_date = datetime.now().strftime("%d-%m-%Y")

        return f"Today's date is {current_date} 📅"

    elif "day" in user_input:

        current_day = datetime.now().strftime("%A")

        return f"Today is {current_day} 📆"

    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😂🐛"

    elif "fun fact" in user_input:
        return "Fun fact: The first computer bug was an actual moth found inside a computer! 🦋💻"

    elif "motivate" in user_input or "motivation" in user_input:
        return "Don't worry about being perfect. Just keep learning and improving every day! 🚀"

    elif "bored" in user_input:
        return "Let's do something! You can ask me for a joke, fun fact, coding tip or motivation 😎"

    elif "thank" in user_input:
        return "You're always welcome! 😊❤️"

    elif user_input in ["bye", "bye bye", "seri", "ok bye"]:
        return "Bye bye da! 👋 Take care!"

    elif user_input in ["ok", "okay", "seri da"]:
        return "Seri da 😄 என்ன வேணும்னாலும் கேளு!"

    elif "help" in user_input:
        return """
I can help you with:

🤖 Basic conversation
💻 Programming
🐍 Python
☕ Java
🌐 HTML
🎨 CSS
⚡ JavaScript
🔥 Flask
😂 Jokes
💡 Motivation
⏰ Time and Date
"""

    elif user_input == "":
        return "Please type something 😄"

    else:
        return "Hmm 🤔 I don't understand that yet. Try asking me something about coding, jokes, time, motivation, or say 'help'."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "response": "Invalid request"
            }), 400

        user_input = data.get("message", "").strip()

        # Get bot response
        response = get_bot_response(user_input)

        # Save user + bot conversation
        save_chat(user_input, response)

        # Send response to frontend
        return jsonify({
            "response": response
        })

    except Exception as error:

        print("Error:", error)

        return jsonify({
            "response": "Something went wrong 😢"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)