"""
This is a Flask application that provides a simple API with a home route.
"""
#app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    Handles the home route and returns a greeting message in JSON format.
    """
    return jsonify(message="Hello level 400 FET, Quality Assurance!")

if __name__ == '__main__':
    """
    Entry point for running the Flask application.
    """
    app.run(debug=True)