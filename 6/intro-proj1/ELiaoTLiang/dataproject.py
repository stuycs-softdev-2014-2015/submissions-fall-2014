from flask import Flask, render_template
import cgi, cgitb
form = cgi.FieldStorage()

def getForm():
    ans = {}
    for element in form:
        ans[element] = form[element].value
    return ans

form = getForm()

f=open('data1.csv',"r")
data = f.read()
databackup = f.read()
f.close()

##assigns ordering
if 'order' not in form:
    form['order'] = 'Performance Points'
if 'direction' not in form:
    form['direction'] = 'up'
        
##assigns interval, default=25
if 'interval' not in form:
    form['interval'] = 25

##changes ordering, order will be a string
def order(column, direction):
    least2big = []
    head = data.split("\n")[0]
    head = head.split(', ')
    index = head.index(column)
    lines = data.split("\n")[1:-1]
    for x in range(len(lines)):
        lines[x] = lines[x].split(',')
    for x in lines:
        for element in range(len(x)):
            x[element] = x[element].strip(' ')
    #now in format [ [a] [b] [c] ]
    for x in range(len(lines)):
        least = lines[-1]
        for element in lines:
            if column== "Score Rank":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column=="SS":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column == "Performance Points":
                if int(least[index][:-2]) > int(element[index][:-2]):
                    least = element
        least2big.append(least)
        lines.pop(lines.index(least))
    if direction == 'up':

        least2big.insert(0,head)
    else:
        least2big.reverse()
        least2big.insert(0,head)
    return least2big


app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

tablestring = "Temporary Table String"
@app.route("/table")
def makeTablePage():
    return render_template("table.html",tablestr=tablestring)

if __name__ == "__main__":
    app.debug=True
    app.run()
