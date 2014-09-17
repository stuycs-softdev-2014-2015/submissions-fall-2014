def cutTable(pageNum, interval):
    printedString="";
    if 'pageNum' not in form:
        form['pageNum'] = 0
    table = "<table border='1'>"
    if 'order' in form:
        lines=order(form['order'], form['direction'])
        for x in lines:
            table+="<tr>"
            for atom in x:
                table+="<td bgcolor='white'>" + str(atom) + "</td>"
            table+="</tr>"
        table+="</table>"
        if int(form['pageNum']) > 0 and 'analysis' not in form:
            printedString+= '<a href="analysis.py?pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        elif int(form['pageNum']) > 0 and 'analysis' in form:
            printedString+= '<a href="analysis.py?analysis=True&pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        printedString+= '<table border="1">'
        printedString+= "<tr><td bgcolor='white'>Rank</td><td bgcolor='white'>Nation</td><td bgcolor='white'>Player Name</td>"
        printedString+= "<td bgcolor='white'>Accuracy</td><td bgcolor='white'>Play Count</td><td bgcolor='white'>Performance Points</td>"
        printedString+= "<td bgcolor='white'>Score Rank</td><td bgcolor='white'>SS</td><td bgcolor='white'>S</td><td bgcolor='white'>A</td></tr>"
        blah = table.split('<tr>')
        
        x = blah.pop(0)
        currentPage = blah[1+(int(form['pageNum']) * int(form['interval'])) : 1 + int(form['interval'])+ (int(form['pageNum'])*int(form['interval']))]
        if int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' not in form:
            x= '<br><a href="analysis.py?pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        elif int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' in form:
            x= '<br><a href="analysis.py?analysis=True&pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        else:
            x=""
        return printedString+"<tr>".join(currentPage)+"</table>"+x
    else:
        lines= data.split("\n")
        for x in lines:
            table+="<tr>"
            molecule = x.split(",")
            for atom in molecule:
                table+="<td bgcolor='white'>" + str(atom) + "</td>"
            table+="</tr>"
        table+="</table>"
        if int(form['pageNum']) > 0 and 'analysis' not in form:
            printedString+= '<a href="analysis.py?pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        elif int(form['pageNum']) > 0 and 'analysis' in form:
            printedString+= '<a href="analysis.py?analysis=True&pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        printedString+= '<table border="1">'
        printedString+= "<tr><td bgcolor='white'>Rank</td><td bgcolor='white'>Nation</td><td bgcolor='white'>Player Name</td>"
        printedString+= "<td bgcolor='white'>Accuracy</td><td bgcolor='white'>Play Count</td><td bgcolor='white'>Performance Points</td>"
        printedString+= "<td bgcolor='white'>Score Rank</td><td bgcolor='white'>SS</td><td bgcolor='white'>S</td><td bgcolor='white'>A</td></tr>"
        blah = table.split('<tr>')
        blah[-1] = '</tr>'
        x = blah.pop(0)
        currentPage = blah[1+(int(form['pageNum']) * int(form['interval'])) : 1 + int(form['interval'])+ (int(form['pageNum'])*int(form['interval']))]
        if int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' not in form:
            x= '<br><a href="analysis.py?pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        elif int(form['interval']) * (1 + int(form['pageNum'])) < 50 and 'analysis' in form:
            x= '<br><a href="analysis.py?analysis=True&pageNum=' + str(int(form['pageNum'])+1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Next</a>'
        else:
            x=""
        return printedString +"<tr>".join(currentPage)+"</table>"+x

##create var at top of analysis.py as tablestring;
##replace all print statments with all tablestring+= __________
##plce into {{tablestring}} using flask
