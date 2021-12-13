from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)
#this is the main index
@app.route("/")
def index():
    #redner this template
    return render_template("index.html")
