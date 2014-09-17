#!/usr/bin/python
import cgi, cgitb
cgitb.enable()

def getFieldData():
    HTML_HEADER = 'Content-type: text/html\n\n'
    page = HTML_HEADER
    page+='<html><body>'
    form = cgi.FieldStorage()
    f = open('Champion Win Rate.csv', 'r')
    d = f.readlines()
    f.close()
    b = 0
    y = 0
    z = ""
    for x in d[0].split(','):
            z += '<td bgcolor=pink>' + x + '</td>'
    z += '</tr>'
    if 'Champ1' in form.keys() and 'Champ2' in form.keys():
        page += '<table border="1"> <tr>' + z
        for x in d[1:]:
            if x.split(',')[0] == form['Champ1'].value:
                page += '<tr>'
                for n in x.split(','):
                    page += '<td bgcolor=yellow>' + n + '</td>'
                page += '</tr> </table>'
                page += '<br> <center> <img src=resources/' + form['Champ1'].value + '.jpg width="500" height="400"> </center> <br>'
                if y == 1:
                    y = 2
                else:
                    page += '<table border="1"> <tr>' + z
                b = b + 1
            if x.split(',')[0] == form['Champ2'].value:
                page += '<tr>'
                for n in x.split(','):
                    page += '<td bgcolor=lightblue>' + n + '</td>'
                page += '</tr> </table>'
                page += '<br> <center> <img src=resources/' + form['Champ2'].value + '.jpg width="500" height="400"> </center> <br>'
                if b == 1:
                    b = 2
                else:
                    page += '<table border="1"> <tr>' + z
                y = y + 1
    else:
        page += 'boop'
    page += '</body> </html>'
    print page
getFieldData()
            
        
    

