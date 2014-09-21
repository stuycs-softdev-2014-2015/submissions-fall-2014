from flask import Flask, render_template, request

app= Flask(__name__)

stream=open('scores.csv', 'r')
readas=stream.read()
stream.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("login.html")
    else:
        user = request.form['user']
        pwd = request.form['pwd']
        if user==None or pwd==None:
            return render_template("login.html")
        else:
            return render_template("home.html", user=user, pwd=pwd)

@app.route("/login", methods=["GET","POST"]) 
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        user = request.form['user']
        pwd = request.form['pwd']
        if user==None or pwd==None:
            return render_template("login.html")
        else:
            return render_template("home.html", user=user, pwd=pwd)

@app.route("/data")
def data():
    listlist = []
    searchlist = []
    ret = readas.splitlines()
    for x in ret:
        innerlist=x.split(",")
        listlist.append(innerlist)
    searchlist = listlist[1:]
    #print searchlist
    return render_template("data.html", listlist=listlist,searchlist=searchlist)

@app.route("/analysis")
def analysis():
    Northeast=["Maine","New Hampshire", "Vermont","Massachusetts","Rhode Island","Connecticut","New York","Pennsylvania","New Jersey"]
    Midwest=["Wisconsin","Michigan","Illinois","Indiana","Ohio","Missouri","North Dakota","South Dakota","Nebraska","Kansas","Minnesota","Iowa"]
    South=["Delaware","Maryland","District of Columbia","Virginia","West Virginia","North Carolina","South Carolina","Georgia","Florida","Kentucky","Tennessee","Mississippi","Alabama","Oklahoma","Texas","Arkansas","Louisiana"]
    West=["Idaho","Montana","Wyoming","Nevada","Utah","Colorado","Arizona","New Mexico","Alaska","Washington","Oregon","California","Hawaii"]
    NortheastSum=[0,0,0,0,0,0,0,0,0,0,0,0]
    MidWestSum=[0,0,0,0,0,0,0,0,0,0,0,0]
    SouthSum=[0,0,0,0,0,0,0,0,0,0,0,0]
    WestSum=[0,0,0,0,0,0,0,0,0,0,0,0]
    NEAverage=[]
    MWAverage=[]
    SAverage=[]
    WAverage=[]
    AVGHolders=[NEAverage,MWAverage,SAverage,WAverage]
    NAMES=["Northeast", "MidWest", "South", "West"]
    ret=readas.splitlines()
    #print ret
    ret=ret[1:]
    #print ret #checks that heading is gone
    for x in ret:
        index=0
        state=x[:x.find(",")]
        if state in Northeast:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                NortheastSum[index]+=float(x[index])
                index+=1
        if state in Midwest:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                MidWestSum[index]+=float(x[index])
                index +=1
        if state in South:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                SouthSum[index]+=float(x[index])
                index+=1
        if state in West:
            x=x.split(",") #splits by commas: basically, each column in the .csv file will become a separate string within the list
            x=x[1:]
            while index<len(x):
                WestSum[index]+=float(x[index])
                index+=1
    for variable in NortheastSum:
        variable=variable/9 #9 is the number of states in the Northeast (hence average of those 9 states can be found by dividing by 9)
        NEAverage.append(variable)
        #print NEAverage
    for variable in MidWestSum:
            variable=variable/12 #12 is the number of states in the MidWest
            MWAverage.append(variable)
        #print MWAverage
    for variable in SouthSum:
        variable=variable/17 #17 is the number of states including D.C. in the South
        SAverage.append(variable)
        #print SAverage
    for variable in WestSum:
        variable=variable/13 #13 is the number of states in the West
        WAverage.append(variable)
        #print WAverage
    return render_template("analysis.html", NEAverage=NEAverage, MWAverage = MWAverage, SAverage = SAverage, WAverage = WAverage)

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)#0.0.0.0 means can run on any host
