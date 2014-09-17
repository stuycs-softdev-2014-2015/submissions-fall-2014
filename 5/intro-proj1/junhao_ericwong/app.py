from flask import Flask,render_template

app = Flask(__name__)

if __name__=="__main__":
    app.debug=True
    app.run()

@app.route("/")
def main():
    return render_template("main.html")

one = open('2012draft.csv', 'r')
info1 = open.readlines()
one.close()

two = open('2012draftexpress.csv', 'r')
info2 = open.readlines()
two.close()

three = open('2012NBAdraft.csv', 'r')
info3 = open.readlines()
three.close()

@app.route("/draft")
def draft():
    return render_template("draft.html",)

@app.route("/stat")
def stat():
    return render_template("stat.html")


