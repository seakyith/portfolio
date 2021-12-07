
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work1")
def work():
    return render_template("work1.html")