#!/usr/bin/python
print 'Content-type: text/html\n\n'
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()

def getcompare(filename,item1,item2):
    #for HORIZONTAL TABLE
    a=open(filename,'r')
    DATA=a.readlines()
    a.close
    #opens and stores csv lines data into DATA
    table='<table><tr>'
    for x in DATA[0].split(','):
            table += '<td bgcolor=pink>' + x + '</td>'
    table+='</tr>'
    #makes first row of the table the TOP ROW of the csv file
    table+='<tr>'
    for y in DATA:
        if y.split(',')[0] == item1:
            for n in y.split(','):
                table += '<td bgcolor=yellow>' + n + '</td>'
            table+='</tr>'
    #makes 2nd row of the table based on the row of item1
    table+='<tr>'
    for z in DATA:
        if z.split(',')[0] == item2:
            for n in z.split(','):
                table += '<td bgcolor=orange>' + n + '</td>'
            table+='</tr>'
    table+='</table>'
    #thrid row
    print table


def verttable(filename,itemlist):
    #for VERTICAL TABLE
    a=open(filename,'r')
    DATA=a.readlines()
    a.close
    #opens and stores csv lines data into DATA
    col1=DATA[0].split(',')  
    number=0
    table=''
    for champs in itemlist:
        for y in DATA:
            if y.split(',')[0] == itemlist[number]:
                count=0
                if number%2 == 0:
                    table+='<div style="left: 220px; top: 50px; position: absolute" align=right>'
                    table+='<table>'
                    while count< len(col1):
                        table+='<tr>'
                        table+='<td bgcolor=pink>'+col1[count]+'</td><td bgcolor=yellow>'+y.split(',')[count]+'</td>'
                        table+='</tr>'
                        count+=1
                else:
                    table+='<div style="right: 320px; top: 50px; position: absolute">'
                    table+='<table>'
                    while count< len(col1):
                        table+='<tr>'
                        table+='<td bgcolor=yellow>'+y.split(',')[count]+'</td><td bgcolor=pink>'+col1[count]+'</td>'
                        table+='</tr>'
                        count+=1
                table+='<table>'
        table+='</table><img src=resources/' + itemlist[number] + '.jpg width="500" height="400"> </center> <br></div>'
        number+=1
    #makes 2 tables 
    print table

def csvToTable(fiel,pagenumber):
    f=open(fiel,'r')
    data=f.readlines()
    f.close()
    table='<table border=1>'
    table+='<tr><td bgcolor=pink>'+data[0].replace(',','</td><td bgcolor=pink>').strip('\n')+'</td></tr>'
    for lines in data[pagenumber-9:pagenumber+1]:
        table+='<tr><td bgcolor=yellow>'+lines.replace(',','</td><td bgcolor=yellow>').strip('\n')+'</td></tr>'
    table+='''<tr><td bgcolor=orange>
    <form name="input" action='getcompare.py' method='get'>
    <input type="submit" name="pagenumber" value="'''+str(int(form['pagenumber'].value)-10)+'''">
    '''+('</td><td bgcolor=orange>'*18)+\
    '''<form name="input" action='getcompare.py' method='get'>
    <input type="submit" name="pagenumber" value="'''+str(int(form['pagenumber'].value)+10)+'''">
    '''+'</table>'
    print table

page='<html><body>'
#page+=str(getcompare('CHAMPION STATS2.csv', 'Ahri', 'Blitzcrank'))+
if 'Champ1' in form:
    page+=str(verttable('CHAMPION STATS2.csv', [form['Champ1'].value,form['Champ2'].value]))
else:
    page+=str(csvToTable('CHAMPION STATS2.csv',int(form['pagenumber'].value)))
page+='</body></html>'
