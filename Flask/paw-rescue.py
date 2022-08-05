"""Flask Application for Paws Rescue Center."""
from flask import Flask
app = Flask(__name__)


@app.route("/home")
def homepage():
    """View Function for the Home Page."""
    return "Paws Rescue Center 🐾"


@app.route("/about")
def about():
    """View Function for the About Page."""
    return """We are a non-profit organization working as an animal rescue center. 
    We aim to help you connect with the perfect fur-baby for you! 
    The animals you find at our website are rescue animals which have been rehabilitated. 
    Our mission is to promote the ideology of "Adopt, don't Shop"! """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
