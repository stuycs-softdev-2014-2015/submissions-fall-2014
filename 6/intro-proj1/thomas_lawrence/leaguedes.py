from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("home")
def home():
    return "<h1>Welcome to the league of desu</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run()
