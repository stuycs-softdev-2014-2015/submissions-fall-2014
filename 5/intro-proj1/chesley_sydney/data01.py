#!/usr/bin/python

print "Content-Type:text/html\n"

print ""

##TEAM ROMANLOSTTHEBET
##MEMBERS: Roman Szul, Chesley Tan
##MKS22-pd4
##HW25
##
##DATASET: JRSmith.csv, NateRobinson.csv (per game stats)
##DATA SOURCE: www.basketball-reference.com
##Chosen because JR Smith recently won the Sixth Man of the Year award
##for his pivotal contributions off the bench to the NY Knicks this season

title = "JR Smith's and Nate Robinson's Season per game records"
heading = "JR Smith's per game stats"
paragraph = "Notes: Tm = Team; Lg = League; G = Games; GS = Games Started; MP = Minutes Played; FG = Field Goals; FGA = FG attempts; 3P = Three Point FG; 3PA = 3P FGA; FT = Free Throws; ORB = Offensive Rebounds; DRB = Defensive Rebounds; TRB = Total Rebounds; AST = Assists; STL = Steals; BLK = Blocks; TOV = Turnovers; PF = Personal Fouls; PTS = Points"



def genTable(fileName,optionalwritetofile=None):
    f=open(fileName,'r')
    data=f.readlines()
    f.close()
    table = ""
    ## Specific Version ##
    table = table + "<title>" + str(title) + "</title>"
    table = table + "<heading>" + str(heading) + "</heading>"
    table = table + "<p>" + str(paragraph) + "</p>"
    
    ## General Purpose Version ##
##    table = "<title>" + str(raw_input("What do you want the title to be?\n")) + "</title>"
##    table += "<heading>" + str(raw_input("What do you want the heading to be? \n")) + "</heading>"
##    table += "<p>" + str(raw_input("What do you want the descriptive paragraph to be?\n")) + "</p>"
    ##                         ##
    
    table += '<table border="1">\n<tr> \n'
    x = data[0].split(',')
    for line in x: # Table headers
        line=line.strip('\r\n') # Removes extra formatting characters
        table = table +  '\t<th> ' + line + '</th> \n'
    table= table + '</tr>\n<tr>\n'
    for y in data[1:]: # Table body
         z = y.split(',')
         for i in z:
              i=i.strip('\r\n')
              table = table +  '\t<td> ' + i + ' </td>\n'
         table = table + '</tr>\n<tr>\n'
    table =  table + '</table>'
    if optionalwritetofile != None:
        x = open(optionalwritetofile,'w')
        x.write(table)
        x.close()
        print "The code has been saved to: " + str(optionalwritetofile)
    else:
        print table

        
print "<p> This data set was chosen because JR Smith recently won the Sixth Man of the Year award for his pivotal contributions off the bench to the NY Knicks this season.  Nate Robinson was another player who also contributed heavily to his team. </p>"

genTable("JRSmith.csv")
heading = "Nate Robinson's per game stats"
genTable("NateRobinson.csv")
print "<a href='http://www.basketball-reference.com/players/s/smithjr01.html'> CSV data for JR Smith found here </a><br>"
print "<a href='http://www.basketball-reference.com/players/r/robinna01.html'> CSV data for Nate Robinson found here </a><br>"
print "<a href='analysis01.py'> Check out the analysis of JR Smith vs Nate Robinson</a>"
print "<hr><p align='right'> Chesley Tan, Roman Szul </p>"
#######NOTE########
# To test, use "JR Smith's Season per game records" as the title
# Use "JR Smith's per game stats" as the heading
# And use:
#"Notes: Tm = Team; Lg = League; G = Games; GS = Games Started; MP = Minutes Played; FG = Field Goals; FGA = FG attempts; 3P = Three Point FG; 3PA = 3P FGA; FT = Free Throws; ORB = Offensive Rebounds; DRB = Defensive Rebounds; TRB = Total Rebounds; AST = Assists; STL = Steals; BLK = Blocks; TOV = Turnovers; PF = Personal Fouls; PTS = Points
# As the description    
