from flask import Flask, render_template
import count

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/count")
def count():
    return render_template("count.html")

if __name__ == "__main__":
    app.run(debug=True)
