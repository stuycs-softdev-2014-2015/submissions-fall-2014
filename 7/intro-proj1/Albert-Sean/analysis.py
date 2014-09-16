from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def analysis():
	return render_template("analysis.html")

if __name__ == '__main__':
    app.run()

