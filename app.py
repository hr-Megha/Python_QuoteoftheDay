from flask import Flask, render_template,request
import random

app=Flask(__name__)


# A list of quotes
quotes = [
    "Believe in yourself!",
    "Stay hungry, stay foolish. – Steve Jobs",
    "Success is not final, failure is not fatal. – Winston Churchill",
    "The best way to predict the future is to create it. – Peter Drucker",
    "In the middle of difficulty lies opportunity. – Albert Einstein"
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)