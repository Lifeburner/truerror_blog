from flask import Flask 

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello there!"


@app.route("/admin")
def admin():
    return "Admin page here."


@app.route("/admin/newpost")
def new_post():
    return "New post."


@app.route("/archive")
def archive():
    return "Archive."
