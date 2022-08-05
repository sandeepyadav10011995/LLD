"""An example application to demonstrate Variable Rules in Routing"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """View for the Home page of the website."""
    return "Welcome to the HomePage!"


@app.route("/<my_name>")
def greetings(my_name):
    """View function to greet the user by name."""
    return "Welcome " + my_name + "!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
