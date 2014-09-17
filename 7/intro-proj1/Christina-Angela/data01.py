from flask import Flask, render_template
app = Flask(__name__)

stream=open('scores.csv', 'r') 
readas=stream.read()

stream.close()

@app.route("/")
def home():
    return "<h1>Hello</h1>"

@app.route("/data")
def dataPage():
    listlist = []
    ret = readas.splitlines()
    for x in ret:
        innerlist=x.split(",")
        listlist.append(innerlist)
    return render_template("data.html", listlist=listlist)

if __name__ == "__main__":
    app.debug = True
    app.run() #can specify which port




