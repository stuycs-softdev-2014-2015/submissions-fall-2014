#!/usr/bin/python
print "Content-Type: text/html\n"

heading = "Justin Strauss and James Xu (Team Dream) <br>"
heading += "IntroCS2 pd 6 <br>"
heading += "HW26 <br>"
heading += "2013-04-22"

intro = "<h3> Background: </h3>"
intro += "We chose basketball because the playoffs of the NBA just started. <br>"
intro += "We thought it would be interesting to compare the best players to <br>"
intro += "ever play the sport with each other. At first we were comparing the <br>"
intro += "Player Efficiency Rating and the regular stat line of the players, <br>"
intro += "but we realized that there would be no way to compare them. So we <br>"
intro += "just tried to determine who was the greatest player of all time <br>"
intro += "(G.O.A.T). An obstacle was manually transferring data into a csv <br>"
intro += "file, which was tedious because there were 100 players. <br>"

link = "Click <a href=" + str("data01.py") + ">here</a> to view Justin's "
link += "data file. <br> Click <a href=" + str("http://lisa.stuy.edu/~james.xu/data01.py")
link += ">here</a> to view James's data file. <br> <h3> Table of Summary Data: </h3>"

conc = "<h3> Conclusion: </h3>"
conc += "After we had finished with our code, we saw that the results of our <br>"
conc += "project generally created the same ranking order of the People's <br>"
conc += "Choice Ranking order. However, there were exceptions. For example, <br>"
conc += "Bill Russell, who was ranked by the People's Choice Ranking as the <br>"
conc += "3rd best player of all time. However, after factoring in the Career <br>"
conc += "Efficiency Value, Bill Russell ended up as 27th on our modified list. <br>"
conc += "His Efficiency ranking was 67, far from his People's Choice Ranking. <br>"
conc += "The Efficiency is a composite basketball statistic that theoretically <br>"
conc += "shows how good the player is. However, this rating is criticized for <br>"
conc += "not fairly weighing the defensive contribution as much as the <br>"
conc += "offensive contribution of a player. Bill Russell has been regarded as <br>"
conc += "the greatest defensive player in the history of the NBA, so our <br>"
conc += "results have supported the criticism of the unbalance of offensive <br>"
conc += "and defensive contributions of the player. Eventually, the NBA might <br>"
conc += "be able to come up with a better way to produce a ranking system. <br>"

def statcomparer(dataset1, dataset2):
    inStream = open(dataset1, "r") # creates file object (read buffer)
    rawdata1 = inStream.read() # stores results in rawdata variable
    inStream.close() # closes the buffer
    data1 = rawdata1.split("\n")
    inStream = open(dataset2, "r") # creates file object (read buffer)
    rawdata2 = inStream.read() # stores results in rawdata variable
    inStream.close() # closes the buffer
    data2 = rawdata2.split("\n")
    
    efflist = [] # a list containing the raw values for efficiency
    for eff in data2:
        if eff != "": # eliminates any possible "ghost cells"
            eff = eff.split(",")
            efflist.append(eff[1][:-2]) # efficiency is listed in the 2nd column

    i = 0
    comb = [] # combined people's choice + efficiency ranking
    for rank in data1:
        if rank != "": # eliminates any possible "ghost cells"
            rank = rank.split(",")
            comb.append(int(rank[0])+int(100-sorted(efflist).index(efflist[i])))
            # must be subtracted from 100 because a higher
            # efficiency yields a lower, or better, ranking
            i += 1 # keeping a counter is cleaner than using list.index()
            
    i = 0
    html = heading + "<br>" + intro + "<br>" + link # the opening html tags
    html += "<table border=" + str(1) + "> <td> Player Name </td> <td> People's"
    html += " Choice Ranking </td> <td> Efficiency Raw Value </td> <td>"
    html += "Efficiency Ranking </td> <td> People's Choice + Efficiency "
    html += " Ranking </td> <td> Overall Player Worth Ranking </td>"
    for rank in data1:
        if rank != "": # eliminates any possible "ghost cells"
            rank = rank.split(",")
            html += "<tr> <td>" + str(rank[1][:-1]) + "</td> <td>"
            html += str(rank[0]) + "</td> <td>" + str(efflist[i]) + "</td> <td>"
            html += str(100-sorted(efflist).index(efflist[i])) + "</td> <td>"
            html += str(int(rank[0])+int(100-sorted(efflist).index(efflist[i])))
            # combined people's choice + efficiency ranking (see above)
            html += "</td> <td>"+str((sorted(comb).index(comb[i]))+1)+"</td>"
            # 1 must be added because the list starts from index 0
            i += 1 # keeping a counter is cleaner than using list.index()
    html += "</table> <br>" + conc + "<br>" # the closing html tags
    print html

statcomparer("PlayerRank.csv", "PlayerEfficiency.csv")
