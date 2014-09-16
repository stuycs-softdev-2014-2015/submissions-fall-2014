from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    s = """
    <h1>Welcome to our webpage.</h1>
    <h2> Tianshi Wang, Barak Zhou, pd7 </h2>
    """
    return s;

@app.route("/kda")
def kda():
    return render_template("kda.html")

@app.route("/kills")
def kills():
    
