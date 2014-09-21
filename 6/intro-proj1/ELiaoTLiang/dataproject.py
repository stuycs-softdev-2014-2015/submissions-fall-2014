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
        
##assigns interval, default=50
if 'interval' not in form:
    form['interval'] = 50

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
#######################################################
##cuttable
def cutTable(pageNum, interval):
    printedString="";
    if 'pageNum' not in form:
        form['pageNum'] = 0
    table = "<table border='1'class='pure-table'>"
    if 'order' in form:
        lines=order(form['order'], form['direction'])
        for x in lines:
            table+="<tr>"
            for atom in x:
                table+="<td><font color='white'>" + str(atom) + "</font></td>"
            table+="</tr>"
        table+="</table>"
        if int(form['pageNum']) > 0 and 'analysis' not in form:
            printedString+= '<a href="dataproject.py?pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        elif int(form['pageNum']) > 0 and 'analysis' in form:
            printedString+= '<a href="dataproject.py?analysis=True&pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        ###########the buttons to sort
        upCaret="<button class='pure-button'><i class='fa fa-caret-up'></i></button>"
        downCaret="<button class='pure-button'><i class='fa fa-caret-down'></i></button>"

        printedString+= '<table border="1" class="pure-table"><thead>'
        printedString+= "<tr><th bgcolor='white'>Rank" + upCaret + downCaret +"</th><th bgcolor='white'>Nation " + upCaret + downCaret+"</th><th bgcolor='white'>Player Name " + upCaret + downCaret+" </th>"
        printedString+= "<th bgcolor='white'>Accuracy"+upCaret +downCaret+"</th><th bgcolor='white'>Play Count"+upCaret+downCaret+"</th><th bgcolor='white'>Performance Points"+upCaret+downCaret+"</th>"
        printedString+= "<th bgcolor='white'>Score Rank"+upCaret+downCaret+"</th><th bgcolor='white'>SS"+upCaret+downCaret+"</th><th bgcolor='white'>S"+upCaret+downCaret+"</th><th bgcolor='white'>A"+upCaret+downCaret+"</th></tr></thead><tbody>"
        blah = table.split("<tr>")
        
        x = blah.pop(0)
        currentPage = blah[1+(int(form['pageNum']) * int(form['interval'])) : 1 + int(form['interval'])+ (int(form['pageNum'])*int(form['interval']))]
        if int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' not in form:
            x= '<br><a href="dataproject.py?pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        elif int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' in form:
            x= '<br><a href="dataproject.py?analysis=True&pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        else:
            x=""
        return printedString+"<tr>".join(currentPage)+"</tbody></table>"+x
    else:
        lines= data.split("\n")
        for x in lines:
            table+="<tr>"
            molecule = x.split(",")
            for atom in molecule:
                table+="<td><font color='white'>" + str(atom) + "</font></td>"
            table+="</tr>"
        table+="</table>"
        if int(form['pageNum']) > 0 and 'analysis' not in form:
            printedString+= '<a href="dataproject.py?pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        elif int(form['pageNum']) > 0 and 'analysis' in form:
            printedString+= '<a href="dataproject.py?analysis=True&pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        printedString+= '<table border="1" class="pure-table"><thead>'
        printedString+= "<tr><th bgcolor='white'>Rank<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>Nation<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>Player Name<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th>"
        printedString+= "<th bgcolor='white'>Accuracy<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>Play Count<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>Performance Points<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th>"
        printedString+= "<th bgcolor='white'>Score Rank<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>SS<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>S<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th><th bgcolor='white'>A<button class='pure-button'><i class='fa fa-arrow-up'></i></button><button class='pure-button'><i class='fa fa-arrow-down'></i></button></th></tr></thead><tbody>"
        blah = table.split('<tr>')
        blah[-1] = '</tr>'
        x = blah.pop(0)
        currentPage = blah[1+(int(form['pageNum']) * int(form['interval'])) : 1 + int(form['interval'])+ (int(form['pageNum'])*int(form['interval']))]
        if int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' not in form:
            x= '<br><a href="dataproject.py?pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        elif int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' in form:
            x= '<br><a href="dataproject.py?analysis=True&pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        else:
            x=""
        return printedString +"<tr>".join(currentPage)+"</tbody></table>"+x

####################################################
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

tablestring = ""
##all tablecode goes under here
if 'pageNum' not in form:
    form['pageNum'] = 0
##basic landing table
    ##analysis in form here?
if form['order']=="Performance Points" and 'analysis' not in form and 'intermit' not in form and 'analyze' not in form:
    tablestring+= cutTable(int(form['pageNum']),int(form['interval']))
    tablestring+= '<br><br>'
    tablestring+= '<form name="analysis" action="dataproject.py" method="get">'
    tablestring+= '<input type="submit" name="analysis" value="Continue to Analysis (Just kidding this is a broken link)"></form>'
##if page state in ANALYSIS, print CUT table
if 'analysis' in form and 'intermit' not in form and 'analyze' not in form:
    ##selects intervals
    tablestring+= '<center><table border="2" class="pure-table"><tr><td height="300" width="705" bgcolor="white"><center>Results per page:'
    tablestring+= '<form name="analysis" action="dataproject.py" method="get">'
    tablestring+= '<select name="interval" onchange="this.form.submit()">'
    tablestring+= '<option value="' + str(form['interval']) + '" selected></option>'
    tablestring+= '<option value="5">5</option>'
    tablestring+= '<option value="10">10</option>'
    tablestring+= '<option value="25">25</option>'
    tablestring+= '<option value="50">50</option></select>'
    tablestring+= '<input type="hidden" name="pageNum" value="0"><hr>'
    tablestring+= '<input type="hidden" name="analysis" value="True">'
    tablestring+= '<input type="hidden" name="direction" value="' + str(form['direction']) + '">'
    tablestring+= 'Order by:'
    tablestring+= '<select name="order">'
    tablestring+= '<option value="' + str(form['order']) + '" selected></option>'
    tablestring+= '<option value="Score Rank">Score Rank</option>'
    tablestring+= '<option value="SS">SS</option>'
    tablestring+= '<option value="Performance Points">Performance Points</option></select><br>'
    ##radio disrupts
    tablestring+= '<input type="radio" name="direction1" value="up">Increasing<br>'
    tablestring+= '<input type="radio" name="direction1" value="down">Decreasing<br><br>'
    tablestring+= '<input type="submit" name="intermit" value="Organize!"></form>'
    tablestring+= '</td></tr></table>'
    #order info, submit here too
    tablestring+= '<h1><center><u>Analysis</u></h1><br><br>'
    tablestring+= cutTable(int(form['pageNum']),int(form['interval']))
    tablestring+= '<br><br><br>'
    tablestring+= '<font size="7"><a href="dataproject.py">Back to intro</a></font>'
    tablestring+= '<br><br><br>'
    tablestring+= '<form name="analyzing" action="dataproject.py" method="get">'
    tablestring+= '<input type="submit" value="View #thestruggle of this project" name="analyze"></form>'
if 'intermit' in form and 'pageNum' in form and 'direction' in form and 'order' in form:
    tablestring+='<head><script type="text/javascript">'
    tablestring+='function delayedRedirect(){window.location = "dataproject.py?analysis=True&pageNum=0' +'&order=' + str(form['order'])+ '&direction=' + str(form['direction1']) + '&interval=' + str(form['interval']) +'"}</script></head>'
    tablestring+='<body onLoad="setTimeout(\'delayedRedirect()\', 3000)"><br>'
    tablestring+='Refreshing...'


if 'analyze' in form:
    tablestring+='Old stuff:<br>'
    tablestring+="""My exploration didn't evolve in any way.<br>
    I just happened to remember that Osu's really competitive<br>
    to the extent where people play 24/7 and their skills are insane.<br>
    A trend in this information would be the nationalities, as many people<br>
    from Japan play osu!, since it was invented there in the first place.<br>
    Obstacles were the different types of numbers in each column.<br>
    The Performance Points had a pp in the way, so it needed a separate code.<br>
    I also wanted to know the amount of people who have no lives<br>
    in a certain nation<br>
    <br>
    >implying everyone<br>"""
    fi = open("data1.csv", "r")
    dataz = fi.read()
    lines1 = dataz.split("\n")
    D = {}
    index = lines1[0].split(",")
    for x in range(len(index)):
        index[x] = index[x].strip(' ')
    index = index.index("Nation")
    lines1 = lines1[1:-2]
    for x in lines1:
        s2l = x.split(",")
        nation = s2l[index].strip(' ')
        if nation not in D:
            D[nation] = 1
        else:
            D[nation] +=1
    keys = D.keys()
    tablestring+='Frequency of players in a nation:<br>'
    for x in keys:
        tablestring+=str(x) + ' : ' + str(D[x]) + '<br>'
    tablestring+="everyone's from Japan... lol<br><br>"

    tablestring+="""I've come to realize that most of the information is already vague, in a sense, as these games don't include their<br>
    specific scores. A more better way of stating this information would be like having a table in which there are many scores<br>
    under a name. This would include some of his best scores, and also their worst scores. The ranking system is also dependent<br>
    on whether or not the player wants to upload their score or not.<br><br>
    Also, to be good at a particular beatmap would mean that the person must've done the beatmap at least over a couple thousand<br>
    times, perfecting it (yes, no life, I did this too with touhou). It would be interesting to show the growth or progress the <br>
    player's making, whenever they come across a new beatmap they're unfamiliar with (thus having a not-so-perfect-score).<br><br>"""

    tablestring+='well, i tried limiting the paragraphs so no tl;dr"s would occur...<br>'
    

    tablestring+='<font size="7" color="white"><center>My struggles in Analysis V2</center></font>'
    tablestring+='What I cried over:<br>'
    tablestring+='<ul>'
    tablestring+='<li>Making a table cutting function for the original table and the analyzing table</li>'
    tablestring+='<li>Having the redirect javascript to keep keys/values in the form</li>'
    tablestring+='<li>Opening the file the next day, having forgotten what I did the previous day, and staring at the code for 2 hours.</li>'
    tablestring+='<li>Wasting 15+ hours playing Osu! rather than doing the actual analysis project about Osu!. Sad life is sad.</li>'
    tablestring+='<li>Doing only the bare minimum, with 3 analyzing factors.</li>'
    tablestring+='<li>Rushing the project to do for Friday, only to rush on the World History project over the weekend.</li>'
    tablestring+='<li>Not being able to play handball today (5/24/13)</li>'
    tablestring+='</ul><br><br>'


@app.route("/table")
def makeTablePage():
    return render_template("table.html",tablestr=tablestring)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.debug=True
    app.run()


