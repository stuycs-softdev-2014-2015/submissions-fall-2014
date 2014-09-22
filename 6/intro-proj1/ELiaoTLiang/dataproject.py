from flask import Flask, render_template, request
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
        
##assigns interval, default=50
if 'interval' not in form:
    form['interval'] = 50

##changes ordering, order will be a string
def order(column, directions):
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
            if column== "Score":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column=="SS":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column == "Performance Points":
                if int(least[index][:-2]) > int(element[index][:-2]):
                    least = element
            elif column == "Accuracy":
                if least[index][:-2] > element[index][:-2]:
                    least = element
            elif column=="Score Rank":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column=="Play Count":
                if int(least[index][:-9]) > int(element[index][:-9]):
                    least = element
            elif column=="S":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column=="A":
                if int(least[index]) > int(element[index]):
                    least = element
            elif column=="Nation":
                if least[index] > element[index]:
                    least = element
            elif column=="Player Name":
                if least[index] > element[index]:
                    least = element
        least2big.append(least)
        lines.pop(lines.index(least))
    if directions == 'up':
        least2big.insert(0,head)
    else:
        least2big.reverse()
        least2big.insert(0,head)
    return least2big
#######################################################
##cuttable
form['direction']="up"

def cutTable(pageNum, interval):
    printedString="";
    if 'pageNum' not in form:
        form['pageNum'] = 0
    table = "<table border='1' class='pure-table'>"
    lines=order(form['order'], form['direction'])
    for x in lines:
        table+="<tr>"
        for atom in x:
            table+="<td><font color='white'>" + str(atom) + "</font></td>"
        table+="</tr>"
    table+="</table>"
    
    ###########the buttons to sort
    upCaret='<form method="POST" action="."><button class="pure-button" type="submit" name="'
    upCaret2='" value="up"><i class="fa fa-caret-up"></i></button></form>'
    downCaret='<form method="POST" action="."><button class="pure-button" type="submit" name="'
    downCaret2='" value="down"><i class="fa fa-caret-down"></i></button></form>'

    printedString+= '<table border="1" class="pure-table"><thead>'
    printedString+= "<tr><th bgcolor='white'>Rank<br>" + upCaret+ "Rank"+upCaret2+ downCaret+"Rank"+downCaret2 +"</th><th bgcolor='white'>Nation<br>" + upCaret + "Nation" + upCaret2 + downCaret + "Nation" + downCaret2 +"</th><th bgcolor='white'>Player Name<br>" + upCaret +"Player Name" + upCaret2 + downCaret + "Player Name" + downCaret2 +" </th>"
    printedString+= "<th bgcolor='white'>Accuracy<br>"+upCaret + "Accuracy" + upCaret2 +downCaret+ "Accuracy" + downCaret2+"</th><th bgcolor='white'>Play Count<br>"+upCaret+"Play Count" + upCaret2 +downCaret + "Play Count" + downCaret2+"</th><th bgcolor='white'>Performance Points<br>"+upCaret+ "Performance Points" + upCaret2 + downCaret+"Performance Points"+downCaret2+"</th>"
    printedString+= "<th bgcolor='white'>Score Rank<br>"+upCaret+"Score Rank"+upCaret2+downCaret+"Score Rank"+downCaret2+"</th><th bgcolor='white'>SS<br>"+upCaret+"SS"+upCaret2+downCaret+"SS"+downCaret2+"</th><th bgcolor='white'>S<br>"+upCaret+"S"+upCaret2+downCaret+"S"+downCaret2+"</th><th bgcolor='white'>A<br>"+upCaret+"A"+upCaret2+downCaret+"A"+downCaret2+"</th></tr></form></thead><tbody>"
    blah = table.split("<tr>")
    
    x = blah.pop(0)
    currentPage = blah[1+(int(form['pageNum']) * int(form['interval'])) : 1 + int(form['interval'])+ (int(form['pageNum'])*int(form['interval']))]
    return printedString+"<tr>".join(currentPage)+"</tbody></table>"+x



##all tablecode goes under here
if 'pageNum' not in form:
    form['pageNum'] = 0
##basic landing table
##analysis in form here?
def prepareTable():
    ans=""
    ans+= cutTable(int(form['pageNum']),int(form['interval']))
    ans+= '<br><br>'
    return ans;

####################################################
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/table/", methods=['GET','POST'])
def makeTablePage():
    print request.data
    print request.form
    print request.method
    if (request.method=="POST"):
        form['order']=request.form.keys()[0]
        form['direction']=request.form.values()[0]
        direction= request.form.values()[0]
        print direction
        tablestring=""
        tablestring=prepareTable()
    else:
        print "swag"
        tablestring = prepareTable()
    ##render all table operations here
    return render_template("table.html",tablestr=tablestring)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.debug=True
    app.run()


