from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

one = open('./static/data/2012draft.csv', 'r')
info1 = one.readlines()
one.close()

two = open('./static/data/2012draftexpress.csv', 'r')
info2 = two.readlines()
two.close()

three = open('./static/data/2012NBAdraft.csv', 'r')
info3 = three.readlines()
three.close()

def formatdata(info):
    newdata = []
    for index in range(len(info)):
        line = info[index]
        line = line.replace('\n' , '')
        line = line.split(',')
        newdata.append(line)
    return newdata

def getanalysisinfo():
    analysis = {}
    draft = formatdata(info1)
    draftexpress = formatdata(info2)
    NBAdraft = formatdata(info3)
    for pick in range(1, 32):
        index = pick - 1
        analysis[pick] = [draft[index][0], draft[index][2], draftexpress[index][2], NBAdraft[index][2]]
    return analysis

@app.route("/draft")
def draft():
    return render_template("draft.html",info=getanalysisinfo())

@app.route("/stat")
def stat():
    return render_template("stat.html")

if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)

