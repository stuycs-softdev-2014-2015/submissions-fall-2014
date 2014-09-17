from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def analysis():
	f = open("static/SAT__College_Board__2010_School_Level_Results.csv")
	s = f.read()
	f.close()
	return render_template("analysis.html")

if __name__ == '__main__':
    app.run(debug = True)

