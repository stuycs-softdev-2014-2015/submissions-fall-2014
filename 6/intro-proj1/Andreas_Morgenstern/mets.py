from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    inStream = open("data01.csv",'r')
    data = inStream.read()
    inStream.close()
    rows = data.split("\n")
    for i in range(0,len(rows)):
        rows[i] = rows[i].split(",")
    return render_template("data.html", info = rows)


@app.route("/analysis")
def analysis():
    inStream = open("averages_hw25.csv","r")
    data = inStream.read()
    inStream.close()
    rows = data.split("\n")
    for i in range(0,len(rows)):
        rows[i] = rows[i].split(",")
    return render_template("analysis.html", info=rows)
if __name__=="__main__":
    app.debug=True
    app.run() 

    
