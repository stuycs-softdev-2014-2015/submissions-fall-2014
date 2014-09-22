#!/usr/bin/python
from flask import Flask, render_template, request

app = Flask(__name__)

    
#setting up RANKINGS
c=open("scores.txt")
ranks=c.read()
c.close()
ranks=ranks.split("\n")

#MAKING RANKING LISTS
i=0
while i<len(ranks):
    ranks[i]=ranks[i].split(',')[1:]
    while '' in ranks[i]:
        ranks[i].remove('')
    i+=1
ranks=ranks[:len(ranks)-1]

#SETTING UP VCRIMES
c=open('gundeath.txt')
vcrimes=c.read()
c.close()
vcrimes=vcrimes.split('\n')

#UPCASE
def upCase(c):
    if "a"<=c<="z":
        return chr(ord(c)+(ord("A")-ord("a")))
    else:
        return c
def toUpper(s):
    a=''
    for x in s:
        a+=upCase(x)
    return a

#MAKING VCRIMES LIST
i=0

while i<len(vcrimes): 
    vcrimes[i]=vcrimes[i].split(',')
    vcrimes[i][0]=toUpper(vcrimes[i][0])
    while '' in vcrimes[i]:
        vcrimes[i].remove('')
    i+=1




#FINDING NATIONAL AVERAGES
ca=0.
for x in vcrimes[1:]:
    ca+=float(x[1])
ca/=50

ra=0.
for x in ranks[1:]:
    ra+=float(x[1])
ra/=50


#MAKING DICTIONARIES OF RANKS AND VCRIMES
crimesd={}
ranksd={}

for x in vcrimes[1:]:
    crimesd[x[0]]=x[1]
    
for x in ranks[1:]:
    ranksd[x[0]]=x[1]
ranksd['RHODE ISLAND ']=ranksd['\xc2\xa0RHODE ISLAND ']
ranksd.pop('\xc2\xa0RHODE ISLAND ')


sortedranksd= sorted(ranksd)

#MAKING BIG TABLE:

table='<table border="1"><tr><th>State</th><th>Score for Gun Control*</th><th>Gun Deaths per 100,000</th></tr>'

for x in sorted(ranksd):
    table+='<tr><td>'+x+'</td><td>'+ranksd[x]+'</td><td>'+crimesd[x[:len(x)-1]]+"</td></tr>\n"

table+='</table>'
crimesdVals={}
i=0
for x in sorted(ranksd):
    crimesdVals[x]=crimesd[x[:len(x)-1]]
                           
                                                                 

#FINDING % OF STATES W/ RANKS BELOW AVERAGE
num=0.
d=0.
c=0.
for x in crimesd:
    if float(ranksd[x+' '])<=ra:
        d+=1
    if float(crimesd[x])<=ca:
        num+=1
        if float(ranksd[x+' '])<=ra:
            c+=1
                    

percent=c/num

basicdata=[['Gun Control Score',str(d),str(d/.50)],['Murders by Fire Arm',str(num),str(num/.5)],['States with Both',str(c),str(c/.50)]]
btable='<table border=1><tr><th>Statistic</th><th>Number of States</th><th>Percent of States</th></tr>'
for x in basicdata:
    btable+='<tr>'
    for y in x:
        btable+='<td>'+y+'</td>'
    btable+='</tr>'
btable+='</table>'





@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    

@app.route("/why",methods=["POST","GET"])
def why():
    if request.method == "POST" and request.form["name"] != "":
        name=request.form["name"]
    else:
        name='Clyde "Thluffy" Sinclaire'
    return render_template("why.html",name=name)



@app.route("/data",methods=["POST","GET"])
def data():
    if request.method == "POST" and request.form["name"] != "":
        name=request.form["name"]
    else:
        name='Clyde "Thluffy" Sinclaire'
    return render_template("data.html",ranksd=ranksd, sortedranksd=sortedranksd, crimesdVals=crimesdVals,name=name)



@app.route("/analysis",methods=["POST","GET"])
def analysis():
    if request.method == "POST" and request.form["name"] != "":
        name=request.form["name"]
    else:
        name='Clyde "Thluffy" Sinclaire'
    return render_template("analysis.html", numDeathsGun=ca, averageScore=ra,basicdataResults=basicdata,name=name);



@app.route("/sources",methods=["POST","GET"])
def sources():
    if request.method == "POST" and request.form["name"] != "":
        name=request.form["name"]
    else:
        name='Clyde "Thluffy" Sinclaire'
    return render_template("sources.html",name=name);



if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=1209)
    app.run()
