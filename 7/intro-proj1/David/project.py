from flask import Flask, render_template

app = Flask(__name__)

def tabledata():
    f = open('wastecollection.csv', 'r')
    s = f.readlines()
    f.close
    finals = []
    i = 0
    while i < len(s):
        s[i] = s[i].split(',')
        finals.append(s[i])
        i += 1
    return s

@app.route("/")
@app.route("/analysis")
def analysis():
    return "Sorry. The analysis is not ready yet."
@app.route("/data")
def data():
    return render_template("page.html", table = tabledata())


if __name__ == "__main__":
    app.debug = True
    app.run()
