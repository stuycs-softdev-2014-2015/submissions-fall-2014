#!/usr/bin/python

print "Content-Type:text/html\n"

print ""


title = "Per Game Analysis"
heading = "<h1>JR Smith vs Nate Robinson</h1>"
paragraph = "We were both avid basketball fans. We thought it would be cool to use this project to compare two Sixth Man of the Year candidates.  This function was intended to generate html code for a webpage with an analysis of any two players.  One of the obstacles we encountered was in recognizing whether the data supplied was a float number that could be subtracted. The data we received from the csv file was in strings, so if the string represented an actual string, and not a number, we would get an error if we tried to convert it into a float. "
analysis = "Nate Robinson is a freak of nature. However these players have very poor shot selection, the reason for their poor field goal percentage. In the opinion of Roman Szul, any field goal percentage below 46% is a poor field goal percentage. However, it appears JR Smith attempts more 3 point field goals, which means the difficulty of shots taken is relatively higher than the average difficulty of those taken by Nate Robinson. Due to this fact, it's reasonable for JR to have a lower field goal percentage. However it appears that Nate Robinson is a better free throw shooter than J.R. Smith. Also, Nate Robinson appears to be more of a team player, averaging more assists than JR. On the contrary J.R. is a much better rebounder, probably due to the fact he is almost a foot taller than Nate Robinson, who is only 5 foot 9 inches, J.R. Smith is 6 foot 6 inches. In the end, taking everything it to consideration, J.R. Smith still averages more points than Nate Robinson, which in my opinion(Roman Szul) is why J.R. Smith is the superior player of the two."


## A general purpose function for creating a webpage containing an analysis of data ##
def analyze(player1,player1CSV,player2,player2CSV,optionalwritetofile=None):
    file1 = open(player1CSV,'r')
    data1 = file1.readlines()
    file1.close()
    table = ""
    
    ## For specified title, heading, paragraph ##
    table = table + "<title>" + str(title) + "</title>"
    table = table + "<heading>" + str(heading) + "</heading>"
    table = table + "<p>" + str(paragraph) + "</p>"
    
    ## General Purpose Version ##
##    table = "<title>" + str(raw_input("What do you want the title to be?\n")) + "</title>"
##    table += "<heading>" + str(raw_input("What do you want the heading to be? \n")) + "</heading>"
##    table += "<p>" + str(raw_input("What do you want the descriptive paragraph to be?\n")) + "</p>"
    ##                         ##
    
    table += '<table border="1">\n<tr> \n'
    x = data1[0].split(',')
    table = table + "<th> Player Name </th>" # Adds a name category
    for line in x: # Table headers
        line=line.strip('\r\n') # Removes extra formatting characters
        table = table +  '\t<th> ' + line + '</th> \n'
    table += '</tr>\n<tr>\n'
    ## Stats for player 1 ##
    table = table + "<td><b>" + str(player1) + "</b></td>" # Adds player1 name under name category
    split1 = data1[-1].split(',')
    for i in split1: # Career stats data
        i=i.strip('\r\n')
        table = table +  '\t<td> ' + i + ' </td>\n'
    table = table + '</tr>\n<tr>\n'
    file2 = open(player2CSV,'r')
    data2 = file2.readlines()
    file2.close()
    ## Stats for player 2 ##
    table = table + "<td><b>" + str(player2) + "</b></td>" # Adds player2 name under name category
    split2 = data2[-1].split(',') # Career stats data
    for i in split2:
        i=i.strip('\r\n')
        table = table +  '\t<td> ' + i + ' </td>\n'
    table = table + '</tr>\n<tr>\n'
    ##Comparison##
    table = table + "<td><b> Difference </b></td>"
    for position,value in enumerate(split1):
        value=value.strip('\r\n')
        if value != "" and type(value) is str:
            try: # Finds the difference between stats in the same category for each player
                table = table + "<td>" + str(float(split1[position]) - float(split2[position])) + "</td>"
            except ValueError:
                table = table + "<td> </td>"
        else:
            table = table + "<td> </td>"   
        
    table += '</tr></table>'
    
    ## For specified analysis ##
    table += "<p>" + str(analysis) + "</p>"
    
    ## General Purpose Version ##
##    table += "<p>" + str(raw_input("What do you want the analytic paragraph to be?\n")) + "</p>"
    ##                         ##
    
    ##################Save Options##################
    if optionalwritetofile != None:
        x = open(optionalwritetofile,'w')
        x.write(table)
        x.close()
        print "The code has been saved to: " + str(optionalwritetofile)
    else:
        print table
        
analyze("JR Smith","JRSmith.csv","Nate Robinson","NateRobinson.csv")
print "<a href='data01.py'> Check out the full per game stats for JR Smith and Nate Robinson</a>"
print "<hr><p align='right'> Chesley Tan, Roman Szul </p>"

    
    
    
    
        
    
