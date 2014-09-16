from flask import Flask, render_template


newanalysis = Flask(__name__)


f = open('static/figures.csv', 'r');
csvstuff = f.readlines()
f.close()
csvstuff = csvstuff[1:]
docnums = [ ]
epnames = [ ]
viewernums = [ ]


@newanalysis.route("/")
def home():
    for x in csvstuff:
        L = x.split(",")
        docnums.append(L[0])
        epnames.append(L[1])
        viewernums.append(L[2][0:-2])
    return render_template("analysis.html",
                           docnums=docnums,
                           epnames=epnames,
                           viewernums=viewernums,
                           listlen=len(docnums))

if __name__=="__main__":
    # set the instance variable debug to True
    newanalysis.debug = True
    # call the run method
    newanalysis.run()
