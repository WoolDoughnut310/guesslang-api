from flask import Flask, request, abort
from guesslang import Guess

app = Flask(__name__)
guess = Guess()

EXTENSIONS = {
    "javascript": "js",
}


@app.route("/")
def index():
    return "Hello, world!"


@app.post('/identify')
def identify():
    source_code = request.form["source_code"]
    language = guess.language_name(source_code)

    if language == None:
        abort(404, "Language not found")

    return language


@app.route('/about')
def about():
    return 'About'
