#!/usr/bin/python
def findpercentages(data):
    percentages=open(data).readlines()
    result=[]
    for x in percentages:
        result.append(x[3:-2])
    finalresult=[]
    superfinalresult=[]
    for x in result:
        finalresult.append(x.replace("|",",").replace(" ",""))
    for x in finalresult:
        superfinalresult.append(x.split(','))
    return superfinalresult
OU=findpercentages("percentagesOU.txt")
UU=findpercentages("percentagesUU.txt")
RU=findpercentages("percentagesRU.txt")
NU=findpercentages("percentagesNU.txt")


def tableallthestuff():
    print "<h1> OU </h1>"
    print "<table border=1>"
    print "<tr><td>Rank<td>Pokemon<td>Percentage"
    for x in OU:
        print "<tr>"
        for y in x:
            print "<td>"
            print y
    print "</table>"
    print "<br>"
    print "<h1> UU </h1>"
    print "<table border=1>"
    print "<tr><td>Rank<td>Pokemon<td>Percentage"
    for x in UU:
        print "<tr>"
        for y in x:
            print "<td>"
            print y
    print "</table>"
    print "<h1> RU </h1>"
    print "<table border=1>"
    print "<tr><td>Rank<td>Pokemon<td>Percentage"
    for x in RU:
        print "<tr>"
        for y in x:
            print "<td>"
            print y
    print "</table>"
    print "<h1> NU </h1>"
    print "<table border=1>"
    print "<tr><td>Rank<td>Pokemon<td>Percentage"
    for x in NU:
        print "<tr>"
        for y in x:
            print "<td>"
            print y
    print "</table>"

print "Content-type: text/html"
print
print "<pre>"
tableallthestuff()
print "</pre>"
    
        
