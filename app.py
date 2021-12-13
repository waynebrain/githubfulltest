from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)
#this is the main index
@app.route("/")
def index():
    return render_template("index.html")
