"""An example application to demonstrate Dynamic Routing"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """"View for the Home page of the Website"""
    return "Welcome to the HomePage!"


@app.route('/square/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of " + str(number) + " is: " + str(number * number)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
