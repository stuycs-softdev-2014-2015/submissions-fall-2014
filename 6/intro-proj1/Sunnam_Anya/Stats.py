from flask import Flask,render_template,request

Stats = Flask(__name__)

stats = []
with open("Salaries.csv", "rb") as f:
    doc = f.read()
    data = doc.split('\r\n')
    for l in data:
        stats.append(l.split(','))

yra = {}

def yravg(a, y):
    n = 0
    ans = 0
    for i in a[1:]:
        if len(i) == 5:
            if int(i[0]) == y:
                ans += long(i[4])
                n += 1
    yra[y] = float(ans/n)

for y in range(1985, 2014):
    yravg(stats, y)

teamavgdic = {}

def teamavg(a, y):
    n = 0
    ans = 0
    for i in a[1:]:
        if len(i) == 5:
            if i[1] == y:
                ans += long(i[4])
                n += 1
    teamavgdic[y] = float(ans/n)

teams = ['ANA', 'ARI', 'ATL', 'BAL', 'BOS', 'CAL', 'CHA', 'CHN', 'CIN', 'CLE',
         'COL', 'DET', 'FLO', 'HOU', 'KCA', 'LAA', 'LAN', 'MIA', 'MIL', 'MIN',
         'ML4', 'MON', 'NYA', 'NYN', 'OAK', 'PHI', 'PIT', 'SDN', 'SEA', 'SFN',
         'SLN', 'TBA', 'TEX', 'TOR', 'WAS']

for y in teams:
    teamavg(stats, y)
    
@Stats.route("/","/home", methods=["GET", "POST"])
def home():
    l = ['Year', 'Team']
    if request.method=="GET":
        return render_template("Home.html",l=l)
    else:
        page = request.form["page"]
        if page == "Year":
            return year()
        elif page == "Team":
            return team()

@Stats.route("/year")
def year():
    dic = yra
    tdic = teamavgdic
    return render_template("Year.html"
                            ,dic = dic
                            ,tdic = tdic)

@Stats.route("/team")
def team():
    dic = yra
    tdic = teamavgdic
    return render_template("Team.html"
                           ,dic = dic
                           ,tdic = tdic)

if __name__=="__main__":
    Stats.debug = True
    Stats.run()

