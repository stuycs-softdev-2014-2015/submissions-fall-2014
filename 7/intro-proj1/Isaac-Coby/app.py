from flask import Flask, render_template

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/")
@app.route("/data")
def data():
    return render_template("data.html")
    
@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

if __name__ == "__main__":
    app.run(debug=True)
