import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the HomePage!"


@app.route("/educative")
def learn():
    return "Happy Learning at Educative!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
