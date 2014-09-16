#!/usr/bin/python

import os
import random

def data (filename):
    f = open(filename)
    s = f.readlines()
    s= "".join(s)
    s = s.split("\n")
    datalist = s[:len(s)-1]
    f.close()
    return datalist

def makeTable (x):
    print "<center>"
    print "<table> \n"
    print "<table border='2'>\n"
    for info in x:
        print "<tr>"
        splitted = info.split(",")
        count = 0
        while count < len(splitted):
            print "<td> " + splitted[count] + " </td>"
            count += 1
        print "</tr> \n"
    print "</table> \n"
    print "</center>"

print "Content-type: text/html\n"

print "<html>"
print "<title> PROJECT: BIG DATA </title>"
print "<head>"
print "Period 9"
print "<br>"
print "Jerry Dai"
print "<br>"
print "Omar Siddique"
print "<br>"
print "<h1> <center> NBA Championship Team Stat Comparison </center> </h1>"
print "<h2> <center> Question: What makes up a championship team? </center> </h2>"
print "</head>"

print "<body>"

print "<h1> Why? </h1>"

print "&nbsp&nbsp&nbsp&nbsp&nbspBelow is the data for the past five National Basketball Association (<b>NBA</b>) championship team seasons."
print "Included are the teams' average statitics for the year as well as their Final opponent average statistics."
print "We chose this data in order to answer the question: what makes up a championship team?"
print "We will compare the season averages of the winning team and the runner-up and see why one team won and why the other lost."


print "<h1> <center> The Raw Data </center> </h1>"

print "<h1> <center> Season Stats for Championship Teams and their Opponents </center> </h1>"

print "<h2> <center> MIAMI HEAT 2011-12 </center> </h2>"
print "<center> <img src='miami.jpeg'> </center>"
print "<br>"
makeTable(data("heat2011-12"))

print "<h2> <center> DALLAS MAVERICKS 2010-11 </center> </h2>"
print "<center> <img src='mavs.jpeg'> </center>"
print "<br>"
makeTable(data("mavs2010-11"))

print "<h2> <center> LOS ANGELES LAKERS 2009-10 </center> </h2>"
print "<center> <img src='lakers10.jpg'> </center>"
print "<br>"
makeTable(data("lakers2009-10"))

print "<h2> <center> LOS ANGELES LAKERS 2008-09 </center> </h2>"
print "<center> <img src='lakers09.jpeg'> </center>"
print "<br>"
makeTable(data("lakers2008-09"))

print "<h2> <center> BOSTON CELTICS 2007-08 </center> </h2>"
print "<center> <img src='celtics.jpeg'> </center>"
print "<br>"
makeTable(data("celtics2007-08"))

print "<h1> The Analysis </h1>"
print "<br>"
print "How do the championship teams' stats compare to those of their opponents?"

def openIt (filename):
    f = open(filename)
    s = f.read().strip(" ").split("\n")
    words = s[0].split(" ")
    words = words[0].split(",")
    return words
              
x = openIt("lakers2009-10")

def comparison (s):
    FG = x.index("FG%")
    TP = x.index("3P%")
    FT = x.index("FTA")
    RB = x.index("TRB")
    AS = x.index("AST")
    TN = x.index("TOV")
    PT = x.index("PTS/G")
    comparisonlist = [FG,TP,FT,RB,AS,TN,PT]
    return comparisonlist

indeces = comparison(x)

def data (filename):
    f = open(filename)
    s = f.readlines()
    s= "".join(s)
    s = s.split("\n")
    datalist = s[:len(s)-1]
    f.close()
    return datalist
      
def analysis (x):
    compare1 = []
    compare2 = []
    print "<center>"
    print "<table> \n"
    print "<table border='2'>\n"
    row1 = x[0].split(",")
    print "<tr>"
    print "<td> CATEGORY </td>"
    for n in indeces:
        value = row1[n]
        print "<td>" + value + "</td>"
    print "</tr> \n"
    row2 = x[1].split(",")
    print "<tr>"
    print "<td> Championship Team </td>"
    for n in indeces:
        value = row2[n]
        compare1.append(float(value))
        print "<td>" + value + "</td>"
    print "</tr> \n"
    row3 = x[3].split(",")
    print "<tr>"
    print "<td> Opponent </td>"
    for n in indeces:
        value = row3[n]
        compare2.append(float(value))
        print "<td>" + value + "</td>"
    print "</tr> \n"
    count = 0
    averages = []
    while count < len(compare1):
        x = compare1[count]
        y = compare2[count]
        z = x-y
        averages.append(str(z))
        count += 1
    print "<tr> \n"
    print "<td> Differential </td>"
    for data in averages:
        print "<td>" + data + "</td>"
    print "</tr> \n"
    print "</table> \n"
    print "</center>"

print "<h3> <center> MIAMI HEAT 2011-12: Analysis of Averages </center> </h3>"
print "<br>"

analysis(data("heat2011-12"))

print "<br>"
print "The 2011-12 Miami Heat were able to get to the free throw line 141 more times than their opponent,"
print "giving them more opportunites for free points (which is also reflected in their average points per game stat)."
print "The Heat also outrebounded their opponents by 122, important in keeping possessions alive and preventing the other team from gaining extra possessions."
print "The Heat had 105 fewer turnovers that season compared to their opponent, showing less sloppy play on the court."

print "<h3> <center> DALLAS MAVERICKS 2010-11: Analysis of Averages  </center> </h3>"
print "<br>"

analysis(data("mavs2010-11"))

print "<br>"
print "The 2010-11 Dallas Mavericks had 265 more assists than their opponent that season,"
print "showing that ball movement is key in winning a championship."

print "<h3> <center> LOS ANGELES LAKERS 2009-10: Analysis of Averages  </center> </h3>"
print "<br>"

analysis(data("lakers2009-10"))

print "<br>"
print "The 2009-10 Los Angeles Lakers saw less assists and less turnovers than their opponent."
print "However, they were able to get to the free throw line more often and were able to collect more rebounds."

print "<h3> <center> LOS ANGELES LAKERS 2008-09: Analysis of Averages  </center> </h3>"
print "<br>"

analysis(data("lakers2008-09"))

print "<br>"
print "The 2008-09 Los Angeles Lakers took more free throws, rebounded the basketball better, and turned the ball over far less times than their opponents."
print "The sloppy play from their opponents can be seen in the 7.6 point differential in games, as giving up the ball could lead to more points for the other team."

print "<h3> <center> BOSTON CELTICS 2007-08: Analysis of Averages  </center> </h3>"
print "<br>"

analysis(data("celtics2007-08"))

print "<br>"
print "The 2007-08 Boston Celtics had significantly more assists and had less turnovers than their opponent,"
print "revealing strong point guard play that shared the ball and protected it as well."
print "They also outrebounded their opponent, limiting possessions and gaining their own,"
print "all of which is reflected in their 10.2 point differential between the two teams."
print "<br>"

print "<h1> The Conclusion </h1>"

print "&nbsp&nbsp&nbsp&nbsp&nbspAs can be seen from the analysis above, the team with the lower field goal percentage, three-point percentage, free throw attempts, rebounds, assists, points per game, and more turnovers is usually the losing team."
print "One aspect to note is that the winning team generally has more free throw attempts and outscores the losing team by 4+ points per game, showing how crucial free throws are."
print "So, to answer the question proposed at the top, a championship team consists of a variety of things."
print "For example, the Dallas Mavericks had more turnovers than their opponent, but made up for it with more assists, rebounds, and a better field goal percentage."
print "The winning team generally had the same statistics, less turnovers, more rebounds, better field goal percentage, and more assists."
print "The combination of these characteristics is exactly what makes each team a championship team."

print "<br>"

print "<h1> Sources </h1>"

print "1. <a href='http://www.basketball-reference.com/leagues/'> NBA Leagues </a>"
print "<br>"
print "2. <a href='http://www.basketball-reference.com/teams/MIA/2012.html'> Miami Heat 2011-12 </a>" 
print "<br>"
print "3. <a href='http://www.basketball-reference.com/teams/DAL/2011.html'> Dallas Mavericks 2010-11 </a>"
print "<br>"
print "4. <a href='http://www.basketball-reference.com/teams/LAL/2010.html'> Los Angeles Lakers 2009-10 </a>"
print "<br>"
print "5. <a href='http://www.basketball-reference.com/teams/LAL/2009.html'> Los Angeles Lakers 2008-09 </a>"
print "<br>"
print "6. <a href='http://www.basketball-reference.com/teams/BOS/2008.html'> Boston Celtics 2007-08 </a>"

print "</body>"

print "</html>"
              
