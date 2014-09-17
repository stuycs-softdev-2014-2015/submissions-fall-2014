#had some trouble with my flask (although it was alrady installed). Definitely not fnished webpage! More features and prettiness to come!)Also have to incorporate the css more

from flask import Flask,render_template

Stats = Flask(__name__)

stats = []
with open("Salaries.csv", "rb") as f:
    doc = f.read()
    data = doc.split('\r\n')
    for l in data:
        stats.append(l.split(','))#stats is a list of lists. The inner lists are
                                  #lists of the elements of each line in the file
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

#print yra

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
    
@Stats.route("/home")
@Stats.route("/")
def home():

    a = """
    <h1> Welcome to our Baseball Salary Stats! </h1>
    <button>Click here!!</button>


    <table>
    <thead>
    <tr>
    <th>Year</th>
    <th>Average Salary </th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>""" + stats[0][0] + """</td>
    <td>""" + stats[0][1] + """</td>
    <td>""" + stats[1][0] + """</td>
    <td>""" + stats[1][1] + """</td>
    <td>""" + stats[2][0] + """</td>
    <td>""" + stats[2][1] + """</td>
    <td>""" + stats[3][0] + """</td>
    <td>""" + stats[3][1] + """</td>
    <td>""" + stats[4][0] + """</td>   
    <td>""" + stats[4][1] + """</td>
    <td>""" + stats[5][0] + """</td>
    <td>""" + stats[5][1] + """</td>
    </tr>
    </tbody>
    </table>"""

    return a

if __name__=="__main__":
    Stats.debug = True
    Stats.run()

        
            


