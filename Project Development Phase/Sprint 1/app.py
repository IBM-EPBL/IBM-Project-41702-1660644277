from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("home.html")
@app.route("/About")
def about():
    return render_template ("about.html")
@app.route("/signup")
def signup():
    return render_template ("signup.html")
@app.route("/Registration")
def registration():
    return render_template ("registration.html")
@app.route("/signinsignup")
def signinsignup():
    return render_template ("index.html")
        

