##cuttable
def cutTable(pageNum, interval):
    printedString="";
    if 'pageNum' not in form:
        form['pageNum'] = 0
    table = "<table border='1' class='pure-table'>"
    if 'order' in form:
        lines=order(form['order'], form['direction'])
        for x in lines:
            table+="<tr>"
            for atom in x:
                table+="<td><font color='white'>" + str(atom) + "</font></td>"
            table+="</tr>"
        table+="</table>"

        ##useless ordering?
        '''
        if int(form['pageNum']) > 0 and 'analysis' not in form:
            printedString+= '<a href="dataproject.py?pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
        elif int(form['pageNum']) > 0 and 'analysis' in form:
            printedString+= '<a href="dataproject.py?analysis=True&pageNum=' + str(int(form['pageNum'])-1)+ '&direction=' + str(form['direction']) +'&order='+str(form['order'])+'&interval=' + str(int(form['interval'])) +'">'+'Back</a>'
'''

        ###########the buttons to sort
        upCaret="<button class='pure-button' type='submit' name='"
        upCaret2="' value='up'><i class='fa fa-caret-up'></i></button>"
        downCaret="<button class='pure-button' type='submit' name='"
        downCaret2="' value='down'><i class='fa fa-caret-down'></i></button>"

        printedString+= '<table border="1" class="pure-table"><thead><form method="get">'
        printedString+= "<tr><th bgcolor='white'>Rank<br>" + upCaret+ "Rank"+upCaret2+ downCaret+"Rank"+downCaret2 +"</th><th bgcolor='white'>Nation<br>" + upCaret + "Nation" + upCaret2 + downCaret + "Nation" + downCaret2 +"</th><th bgcolor='white'>Player Name<br>" + upCaret +"Player Name" + upCaret2 + downCaret + "Player Name" + downCaret2 +" </th>"
        printedString+= "<th bgcolor='white'>Accuracy<br>"+upCaret + "Accuracy" + upCaret2 +downCaret+ "Accuracy" + downCaret2+"</th><th bgcolor='white'>Play Count<br>"+upCaret+"Play Count" + upCaret2 +downCaret + "Play Count" + downCaret2+"</th><th bgcolor='white'>Performance Points<br>"+upCaret+ "Performance Points" + upCaret2 + downCaret+"Performance Points"+downCaret2+"</th>"
        printedString+= "<th bgcolor='white'>Score Rank<br>"+upCaret+"Score Rank"+upCaret2+downCaret+"Score Rank"+downCaret2+"</th><th bgcolor='white'>SS<br>"+upCaret+"SS"+upCaret2+downCaret+"SS"+downCaret2+"</th><th bgcolor='white'>S<br>"+upCaret+"S"+upCaret2+downCaret+"S"+downCaret2+"</th><th bgcolor='white'>A<br>"+upCaret+"A"+upCaret2+downCaret+"A"+downCaret2+"</th></tr></form></thead><tbody>"
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
            printedString+= "<tr><th bgcolor='white'>Rank<br>" +  upCaret + "R"+upCaret2+ downCaret+"R"+downCaret2 +"</th><th bgcolor='white'>Nation<br>" + upCaret + "N" + upCaret2 + downCaret + "N" + downCaret2 +"</th><th bgcolor='white'>Player Name<br>" + upCaret +"P" + upCaret2 + downCaret + "P" + downCaret2 +" </th>"
            printedString+= "<th bgcolor='white'>Accuracy<br>"+upCaret + "Acc" + upCaret2 +downCaret+ "Acc" + downCaret2+"</th><th bgcolor='white'>Play Count<br>"+upCaret+"Count" + upCaret2 +downCaret + "Count" + downCaret2+"</th><th bgcolor='white'>Performance Points<br>"+upCaret+ "PP" + upCaret2 + downCaret+"PP"+downCaret2+"</th>"
            printedString+= "<th bgcolor='white'>Score Rank<br>"+upCaret+"Score"+upCaret2+downCaret+"Score"+downCaret2+"</th><th bgcolor='white'>SS<br>"+upCaret+"SS"+upCaret2+downCaret+"SS"+downCaret2+"</th><th bgcolor='white'>S<br>"+upCaret+"S"+upCaret2+downCaret+"S"+downCaret2+"</th><th bgcolor='white'>A<br>"+upCaret+"A"+upCaret2+downCaret+"A"+downCaret2+"</th></tr></thead><tbody>"
            blah = table.split("<tr>")
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
