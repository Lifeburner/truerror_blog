from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", title="Rowie's Home Page")


@app.route("/admin")
def admin():
    return "Admin page here."


@app.route("/admin/newpost")
def new_post():
    return "New post."


@app.route("/archive")
def archive():
    return "Archive."


if __name__ == "__main__":
    app.run(debug=True)
