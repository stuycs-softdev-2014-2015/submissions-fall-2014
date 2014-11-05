from flask import Flask,render_template,request

app = Flask(__name__)

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

@app.route("/",methods=["GET","POST"])
def main():
    button = request.args.get("button",None)
    t  = request.args.get("type",None) #type
    chose1 = request.args.get("statistic",None)
    chose2 = request.args.get("draft",None)
    #print button,t,chose1,chose2
    l = ['Points','Rebounds','Assists','Field_Goal','Free_Throw']
    if request.method=="GET":
        return render_template("main.html",l=l)
    else:
        chose1 = request.form.getlist("statistic")
        chose2 = request.form.getlist("draft")
        t = request.form['type']
        button = request.form['button']
        if button == "submit":
            if t == "stat":
                return render_template("stat.html",info=getanalysisinfo(),
                                       draftStats=formatdata(info1),
                                       draft2Stats=formatdata(info2),
                                       nbadraftStats=formatdata(info3),
                                       l=chose1)
            else:
                return render_template("draft.html",info=getanalysisinfo(2),l=chose2)

if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
