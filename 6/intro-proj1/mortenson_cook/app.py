from flask import Flask,render_template,request
import cgi, cgitb, os
cgitb.enable()
F=cgi.FieldStorage()


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)


def average(L):
    i=0.0
    for n in L:
        i+=n
    i/=len(L)
    return i
    
def convertData(D):
    for x in D:
        D[x]=[average(D[x]),len (D[x])]
    return D
@app.route("/results")
def results():
        f=open('data1.csv','r')
        pitchers=f.read()
        f.close()
        pitchers=pitchers.split()
        pitchers=pitchers[1:]
        D1={}
        for n in range(len(pitchers)):
                pitchers[n]=pitchers[n].split(',')
                if float(pitchers[n][1]) in D1:
                        D1[float(pitchers[n][1])]+=[float(pitchers[n][2])]
                else:
                        D1[float(pitchers[n][1])]=[float(pitchers[n][2])]
        
                g=open('data2.csv','r')
                batters=g.read()
                g.close()
                batters=batters.split()
                batters=batters[1:]
                D2={}
        for n in range(len(batters)):
                batters[n]=batters[n].split(',')
                if float(batters[n][1]) in D2:
                        D2[float(batters[n][1])]+=[float(batters[n][2])]
                else:
                    D2[float(batters[n][1])]=[float(batters[n][2])]
            


        convertData(D1) 
        convertData(D2) 
        Pi=[]
        for n in sorted(D1):
                Pi+=[[n]+D1[n]]
                
        Ba=[]
        for n in sorted(D2):
                Ba+=[[n]+D2[n]]
                
        
        return render_template("results.html", Ba=Ba, Pi=Pi)

@app.route("/rawdata")
def rawdata():
    f=open('data1.csv','r')
    pitchers=f.read()
    f.close()
    pitchers=pitchers.split()

    g=open('data2.csv','r')
    batters=g.read()
    g.close()
    batters=batters.split()
    players=[]
    for n in range(len(batters)):
        pitchers[n]=pitchers[n].split(',')
        batters[n]=batters[n].split(',')
        players.append([pitchers[n][0],batters[n][3],pitchers[n][1],pitchers[n][2],batters[n][1],batters[n][2]])
    pi='<table border=1>'
    i=0
    for n in range(len(players)):
        pi+='<tr><td>'+str(players[n][0])+'</td><td>'+str(players[n][1])+'</td><td>'+str(players[n][2])+'</td><td>'+str(players[n][3])+'</td><td>'
        pi+=str(players[n][4])+'</td><td>'+str(players[n][5])+'</td></tr>'
        i+=1
    pi+='</table>'
    q=[]
    return render_template("rawdata.html",players=players,q=q)

@app.route("/filter", methods= ["GET", "POST"])
def filter():
    team="Tm"
    boxes=20
    year= "Yr"
    sort=""
    hilo=""  
    f=open('data1.csv','r')
    pitchers=f.read()
    f.close()
    pitchers=pitchers.split()    
    g=open('data2.csv','r')
    batters=g.read()
    g.close()
    batters=batters.split()
    players=[]
    for n in range(len(batters)):
        pitchers[n]=pitchers[n].split(',')
        batters[n]=batters[n].split(',')
        players.append([pitchers[n][0],batters[n][3],pitchers[n][1],pitchers[n][2],batters[n][1],batters[n][2]])
        i=0
    if request.method== "GET":
        q=["Tm",20,"Yr"]
        return render_template("filter.html",players=players[:q[1]+1],q=q)
    else:
        team=request.form["team"]
        boxes=request.form["boxes"]
        year=request.form["year"]
        sort=request.form["sort"]
        hilo=request.form["hilo"]
        print team+boxes+year+sort+hilo
    #if 'p' in F:
    #    p=int(F['p'].value)
    #else:
        p=1
        if str(sort)=='runs':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][5]=players[n][5],players[n][0]
            players.sort()
            if str(hilo)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][5],players[n][0]=players[n][0],players[n][5]
            players.insert(0,first)
            
        if str(sort)=='runa':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][3]=players[n][3],players[n][0]
            players.sort()
            if str(hilo)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][3],players[n][0]=players[n][0],players[n][3]
            players.insert(0,first)
            
        if str(sort)=='bage':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][4]=players[n][4],players[n][0]
            players.sort()
            if str(hilo)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][4],players[n][0]=players[n][0],players[n][4]
            players.insert(0,first)
            
        if str(sort)=='page':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][2]=players[n][2],players[n][0]
            players.sort()
            if str(hilo)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][2],players[n][0]=players[n][0],players[n][2]
            players.insert(0,first)

        if str(sort)=='yr':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][1]=players[n][1],players[n][0]
            players.sort()
            if str(hilo)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][1],players[n][0]=players[n][0],players[n][1]
            players.insert(0,first)

        if str(sort)=='tm':
            first=players[0]
            players.remove(players[0])
            players.sort()
            if str(hilo)=='lo':
                players=players[::-1]
            players.insert(0,first)
            
        q=[team,int(boxes),year];
        return render_template("filter.html", players=players, q=q)
    
@app.route("/home")
@app.route("/") 
def home():
   
    return render_template("home.html")

if __name__=="__main__":
    app.debug=True
    app.run() 

    
