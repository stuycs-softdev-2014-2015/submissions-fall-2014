#!/usr/bin/python
print 'Content-Type: text/html\n\n'

import cgi, cgitb, os
cgitb.enable()
F=cgi.FieldStorage()
    
if 'pg' in F:
    f=open('data1.csv','r')
    pitchers=f.read()
    f.close()
    pitchers=pitchers.split()
    pitchers=pitchers[1:]
    D1={}
    for n in range(len(pitchers)):
        pitchers[n]=pitchers[n].split(',')
        if float(pitchers[n][1]) in D1:
            D1[float(pitchers[n][1])]+=[float(pitchers[n][2])]
        else:
            D1[float(pitchers[n][1])]=[float(pitchers[n][2])]

    g=open('data2.csv','r')
    batters=g.read()
    g.close()
    batters=batters.split()
    batters=batters[1:]
    D2={}
    for n in range(len(batters)):
        batters[n]=batters[n].split(',')
        if float(batters[n][1]) in D2:
            D2[float(batters[n][1])]+=[float(batters[n][2])]
        else:
            D2[float(batters[n][1])]=[float(batters[n][2])]
            
    def average(L):
        i=0.0
        for n in L:
            i+=n
        i/=len(L)
        return i

    def convertData(D):
        for x in D:
            D[x]=[average(D[x]),len (D[x])]
        return D

    convertData(D1) 
    convertData(D2) 
    Pi=[]
    for n in sorted(D1):
        Pi+=[[n]+D1[n]]
        
    Ba=[]
    for n in sorted(D2):
        Ba+=[[n]+D2[n]]

    print '''<html>
    <head><title>Age's Effect on Baseball, Part Two</title><link rel="shortcut icon" href="http://bart.stuy.edu/~aaron.mortenson/muffins/moop.ico"></head>

    <body style=
    "background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#808080), to(#660505), color-stop(.2,#808080));background-image: -moz-linear-gradient(19% 75% 90deg,#660505, #808080, #808080 100%)" bgcolor="grey">
    Mortenson, Aaron MKS22 Period 7
    <center>
    <h1>Age's Effect on Baseball, Part Two</h1>
    <a href="analisys26.py">Press here to see the raw data used to generate these tables.</a></br>
    <table bordercolor="black" width=95% bgcolor="white"><tr><td>
    </br>
    <p style="text-indent: 5em;">
    Once I had converted the raw data into a python dictionary, the biggest difficulty in analyzing the data was
    showing that the data is significant and that there are trends in it.
    I knew right away that there were trends after graphing the raw data in Microsoft Office Excel and having trendlines drawn.
    When viewed as just numbers, however, my data looked pretty meaningless. The problem dictated how I analyzed the data.
    What I ended up doing was creating a list of lists to hold each data set. Each small list had three elements: A given average age, 
    the average number of runs scored or allowed per game by all teams that shared that average player age, and the number of times that average age occured.
    From this, I was able to extract meaningful data by displaying the average number of runs scored or allowed by teams with certian average ages.
    The average ages I did display data from ended up being determined by number of times that average age occured.
    </p>
    <p style="text-indent: 5em;">
    Upon revising the page, I had to change a lot in order to make the raw data sortable. To start with,
    I added the year and team name to my data and simplified the data by combining the two data sets into one.
    This way, there was only one form and one table, and there were no issues with one data table being reset every time the other is sorted.
    Once I had condensed the two data sets into one, the filters were fairly simple,
    but the sorting function required some thought and a lot of tweaking.
    </p>
    <p style="text-indent: 5em;">
    As a note, the raw data value of average player age is weighted based on how much each person played. For example, a 20-year-old rookie
    who only played in 30 of 162 games would count less towards a team's average age than a 35-year-old vet who played in all 162 games.
    This was not done by me, but by the providers of the raw data.
    </p>
    <p style="text-indent: 5em;">
    The processed data seen here displays the overall average number of runs per game scored by all teams with a given average hitter age,
    as well as the overall average number of runs per game allowed by teams with a given average pitcher age.
    For the sake of precision, data is only included from average ages that occur 8 or more times in teams in the raw data set,
    so that teams like the 1998 Florida Marlins, whose young yet terrible pitching staff gave up an average of 5.70 runs per game 
    while being the only pitching staff in the last 20 years to have an average age of 24.5 years old, don't throw off the data too much.
    For example, if there are 12 teams in the data set with an average hitter age of 28.3 years old, the average number of runs scored per game
    by each of those teams is displayed next to the number 28.3. However, if there are only 5 teams in the data set with an average hitter age of 31.4 years old,
    there will be no data displayed for teams with average hitter ages of 31.4 years old.
    </p>'''
    print '''<center>
    <table><tr>
    <td width="5%"></td>
    <td width="20%"><center>
    This table shows how the average age of a team's pitchers affects the number of runs scored against them in a game. Looking closely, 
    one can notice a general trend; the older the pitchers, the fewer runs a team gives up. While teams with an average pitcher age of between 28 and 30 
    display no obvious trends, the oldest and youngest teams do. While teams whose average pitcher is under the age of 28 give up somewhere between
    4.7 and 4.9 runs on average, teams whose average pitcher is older than 30 give up between 4.3 and 4.6 runs per game on average, significantly fewer.
    </center></td>
    <td width="3%"></td>
    <td width="20%"><table border=1 style=
    "background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#808080), to(#660505), color-stop(.2,#808080));background-image: -moz-linear-gradient(19% 75% 90deg,#660505, #808080, #808080 100%)" bgcolor="grey">
    <tr><td>Average Pitcher Age</td><td>Average Runs Allowed per Game</td>'''
    for n in Pi:
        if n[2]>=8:
            print '<tr><td>'+str(n[0])+'</td><td>'+str(int(10*(n[1]+.05))/10.0)+'</td></tr>'
    print '''</table></td>
    <td width="4%"></td>
    <td width="20%"><table border=1 style=
    "background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#808080), to(#660505), color-stop(.2,#808080));background-image: -moz-linear-gradient(19% 75% 90deg,#660505, #808080, #808080 100%)" bgcolor="grey">
    <td>Average Batter Age</td><td>Average Runs Scored per Game</td>'''
    for n in Ba:
        if n[2]>=8:
            print '<tr><td>'+str(n[0])+'</td><td>'+str(int(10*(n[1]+.05))/10.0)+'</td></tr>'
    print '''</table></td>
    <td width="3%"></td>
    <td width="20%"><center>
    With batters, a similar trend can be observed. This time, however, it is much more clear. With a few exceptions, the typical team with an average batter age of
    younger than 29 score an average of <b>fewer</b> than 4.8 runs per game. Typical teams with an average batter age of older than 29, with suprisingly few exceptions,
    average 4.8 <b>or more</b> runs per game. This trend is much more apparent than the trend amongst pitchers.
    </center></td>
    <td width="5%"></td>
    </tr></table>
    </center>
    <p style="text-indent: 5em;">
    While these tables show trends with different levels of clarity, the trends are consistent with each other;
    older teams tend to give up fewer runs and score more runs than younger ones, meaning that while it is frustrating that the Yankees have
    so few young, exciting players, their age may be a good thing rather than a bad thing. While a gutsy rookie may be more interesting to watch
    than a knowlegable veteran past his prime, experience is more valuable than youth in baseball. As Yogi Berra famously said,
    "Baseball is 90% mental, the other half is physical," and though a 25-year-old rookie may be more athletic than his 40-year old self,
    He will always learn more about the game and grow more mentally prepared as he gets older and continues to play. 
    </p>
    </br>
    </table></center>
    </body></html>'''

else:
    url = os.environ["REQUEST_URI"]
    f=open('data1.csv','r')
    pitchers=f.read()
    f.close()
    pitchers=pitchers.split()

    g=open('data2.csv','r')
    batters=g.read()
    g.close()
    batters=batters.split()
    players=[]
    for n in range(len(batters)):
        pitchers[n]=pitchers[n].split(',')
        batters[n]=batters[n].split(',')
        players.append([pitchers[n][0],batters[n][3],pitchers[n][1],pitchers[n][2],batters[n][1],batters[n][2]])
    pi='<table border=1>'
    if 'p' in F:
        p=int(F['p'].value)
    else:
        p=1
    if 'boxes' in F and 'team' in F and 'year' in F and 'hilo' in F and 'sort' in F:
        if str(F['sort'].value)=='runs':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][5]=players[n][5],players[n][0]
            players.sort()
            if str(F['hilo'].value)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][5],players[n][0]=players[n][0],players[n][5]
            players.insert(0,first)
            
        if str(F['sort'].value)=='runa':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][3]=players[n][3],players[n][0]
            players.sort()
            if str(F['hilo'].value)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][3],players[n][0]=players[n][0],players[n][3]
            players.insert(0,first)
            
        if str(F['sort'].value)=='bage':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][4]=players[n][4],players[n][0]
            players.sort()
            if str(F['hilo'].value)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][4],players[n][0]=players[n][0],players[n][4]
            players.insert(0,first)
            
        if str(F['sort'].value)=='page':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][2]=players[n][2],players[n][0]
            players.sort()
            if str(F['hilo'].value)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][2],players[n][0]=players[n][0],players[n][2]
            players.insert(0,first)

        if str(F['sort'].value)=='yr':
            first=players[0]
            players.remove(players[0])
            for n in range(len(players)):
                players[n][0],players[n][1]=players[n][1],players[n][0]
            players.sort()
            if str(F['hilo'].value)=='hi':
                players=players[::-1]
            for n in range(len(players)):
                players[n][1],players[n][0]=players[n][0],players[n][1]
            players.insert(0,first)

        if str(F['sort'].value)=='tm':
            first=players[0]
            players.remove(players[0])
            players.sort()
            if str(F['hilo'].value)=='lo':
                players=players[::-1]
            players.insert(0,first)
            
        if str(F['team'].value)=='Tm' and str(F['year'].value)=='Yr':
            i=0
            for n in range(len(players)):
                if i<=int(F['boxes'].value)*p:
                    if i>int(F['boxes'].value)*(p-1) or i==0:
                        pi+='<tr><td>'+str(players[n][0])+'</td><td>'+str(players[n][1])+'</td><td>'+str(players[n][2])+'</td><td>'+str(players[n][3])+'</td><td>'
                        pi+=str(players[n][4])+'</td><td>'+str(players[n][5])+'</td></tr>'
                    i+=1
            pi+='</table>'
        elif str(F['year'].value)=='Yr':
            i=0
            for n in range(len(players)):
                if i<=int(F['boxes'].value)*p and (n==0 or str(F['team'].value)==str(players[n][0])):
                    if i>int(F['boxes'].value)*(p-1) or i==0:
                        pi+='<tr><td>'+str(players[n][0])+'</td><td>'+str(players[n][1])+'</td><td>'+str(players[n][2])+'</td><td>'+str(players[n][3])+'</td><td>'
                        pi+=str(players[n][4])+'</td><td>'+str(players[n][5])+'</td></tr>'
                    i+=1
            pi+='</table>'
        elif str(F['team'].value)=='Tm':
            i=0
            for n in range(len(players)):
                if i<=int(F['boxes'].value)*p and (n==0 or str(F['year'].value)==str(players[n][1])):
                    if i>int(F['boxes'].value)*(p-1) or i==0:
                        pi+='<tr><td>'+str(players[n][0])+'</td><td>'+str(players[n][1])+'</td><td>'+str(players[n][2])+'</td><td>'+str(players[n][3])+'</td><td>'
                        pi+=str(players[n][4])+'</td><td>'+str(players[n][5])+'</td></tr>'
                    i+=1
            pi+='</table>'
        else:
            i=0
            for n in range(len(players)):
                if i<=int(F['boxes'].value)*p and (n==0 or (str(F['year'].value)==str(players[n][1]) and str(F['team'].value)==str(players[n][0]))):
                    if i>int(F['boxes'].value)*(p-1) or i==0:
                        pi+='<tr><td>'+str(players[n][0])+'</td><td>'+str(players[n][1])+'</td><td>'+str(players[n][2])+'</td><td>'+str(players[n][3])+'</td><td>'
                        pi+=str(players[n][4])+'</td><td>'+str(players[n][5])+'</td></tr>'
                    i+=1
            pi+='</table>'
    else:
        i=0
        for n in range(len(players)):
            if i<=20*p:
                if i>20*(p-1) or i==0:
                    pi+='<tr><td>'+str(players[n][0])+'</td><td>'+str(players[n][1])+'</td><td>'+str(players[n][2])+'</td><td>'+str(players[n][3])+'</td><td>'
                    pi+=str(players[n][4])+'</td><td>'+str(players[n][5])+'</td></tr>'
                i+=1
        pi+='</table>'


    print '''<html>
    <head><title>Age's Effect on Baseball, Part One</title><link rel="shortcut icon" href="http://bart.stuy.edu/~aaron.mortenson/muffins/moop.ico"></head>

    <body style=
    "background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#808080), to(#660505), color-stop(.2,#808080));background-image: -moz-linear-gradient(19% 75% 90deg,#660505, #808080, #808080 100%)" bgcolor="grey">
    Mortenson, Aaron MKS22 Period 7
    <center>
    <h1>Age's Effect on Baseball, Part One</h1>
    <a href="analisys26.py?pg=1">Press here to see an analisys of this data.</a></br>
    <table bordercolor="black" width=95% bgcolor="white"><tr><td>
    </br>
    <p style="text-indent: 5em;">
    As a Yankees fan this season, I became frustrated with my beloved team for signing old players this year who are mostly past their primes, 
    instead of going for young prospects. In fact, the Yankees are the oldest team in the major leagues this year, with the average age of a player on their 
    roster being 30.9 years old, more than two years older than the league average of 28.8. All this attention to player ages got me wondering: 
    Does age actually affect the performance of major league baseball teams, and if so, how? Is there a correlation between the average ages of players on
    a team and how well that team does?
    </p>
    <p style="text-indent: 5em;">
    To find out, I took data from every major league season over the last 20 years (1993-2012) with the exception of 1994 and 1995. 
    The season was cut short in 1994 to about 114 of 162 games due to a strike of the players' union, and in 1995, the season was cut to 
    144 games because of revamped scheduling. Since these two seasons were shortened, data from them is not as precise as data from other seasons, 
    and for this reason data from those years is not included. I compared the average age of each team's hitters in a given year
    to the average number of runs it produced per game that year, and I compared the average age of each team's pitchers in a given year to the average number of runs
    scored by opposing teams per game that year.  This is the raw data I managed to find after it has been run through a script to add the year to the end of each line:
    </p>'''
    print'<table width="100%"><tr><td width="50%"><center>'
    print '''<table bordercolor="black" bgcolor="grey"><tr><td>
        <form name="input" action="analisys26.py" method="get">
	Filters:

	<select name="team">

	<option value="Tm">---------Any team---------</option>

	<option value="ANA">Anahiem Angels</option>

	<option value="ARI">Arizona Diamondbacks</option>

	<option value="ATL">Atlanta Braves</option>

	<option value="BAL">Baltimore Orioles</option>

	<option value="BOS">Boston Red Sox</option>

	<option value="CAL">California Angels</option>

	<option value="CHC">Chicago Cubs</option>

	<option value="CHW">Chicago White Sox</option>

	<option value="CIN">Cincinatti Reds</option>

	<option value="CLE">Cleveland Indians</option>

	<option value="COL">Colorado Rockies</option>

	<option value="DET">Detroit Tigers</option>

	<option value="FLA">Folrida Marlins</option>

	<option value="HOU">Houston Astros</option>

	<option value="KCR">Kansas City Royals</option>

	<option value="LAA">Los Angeles Angels</option>

	<option value="LAD">Los Angeles Dodgers</option>

	<option value="MIA">Miami Marlins</option>

	<option value="MIL">Milwalkee Brewers</option>

	<option value="MIN">Minnesota Twins</option>

	<option value="MON">Montreal Expos</option>

	<option value="NYM">New York Mets</option>

	<option value="NYY">New York Yankees</option>

	<option value="OAK">Oakland Athletics</option>

	<option value="PHI">Philadelphia Phillies</option>

	<option value="PIT">Pittsburgh Pirates</option>

	<option value="SDP">San Diego Padres</option>

	<option value="SEA">Seattle Mariners</option>

	<option value="SFG">San Fransisco Giants</option>

	<option value="STL">Saint Louis Cardinals</option>

	<option value="TBD">Tampa Bay Devil Rays</option>

	<option value="TBR">Tampa Bay Rays</option>

	<option value="TEX">Texas Rangers</option>

	<option value="TOR">Toronto Blue Jays</option>

	<option value="WSN">Washington Nationals</option>

	</select>



	<select name="year">

	<option value="Yr">Any year</option>

	<option value="2012">2012</option>

	<option value="2011">2011</option>

	<option value="2010">2010</option>

	<option value="2009">2009</option>

	<option value="2008">2008</option>

	<option value="2007">2007</option>

	<option value="2006">2006</option>

	<option value="2005">2005</option>

	<option value="2004">2004</option>

	<option value="2003">2003</option>

	<option value="2002">2002</option>

	<option value="2001">2001</option>

	<option value="2000">2000</option>

	<option value="1999">1999</option>

	<option value="1998">1998</option>

	<option value="1997">1997</option>

	<option value="1996">1996</option>

	<option value="1993">1993</option>

	</select><br><br>

	Sort By:

	<select name="sort">

	<option value="yr">Year</option>
	<option value="runs">Runs Scored</option>
	<option value="runa">Runs Allowed</option>
	<option value="bage">Batter Age</option>
	<option value="page">Pitcher Age</option>
        <option value="tm">Team</option>

	</select>



	<select name="hilo">

	<option value="hi">High to Low</option>

	<option value="lo">Low to High</option>

	</select><br><br>



	Display up to 

	<select name="boxes">

	<option value="10">10</option>

	<option value="20" selected>20</option>

	<option value="30">30</option>

	<option value="40">40</option>

	<option value="50">50</option>

	</select>

	results per page

	<input type="submit" value="Go">

	</form>



	</td></tr></table>'''
    if 'p' in F:
        urlplus=url.replace('p='+str(F['p'].value),'p='+str(int(F['p'].value)+1))
        if int(F['p'].value)>=2:
            urlminus=url.replace('p='+str(F['p'].value),'p='+str(int(F['p'].value)-1))
            print '<a href="http://bart.stuy.edu'+urlminus+'">previous page</a>'
    else:
        if len(F)==0:
            urlplus=url+'?p=2'
        else:
            urlplus=url+'&p=2'
    print '<a href="http://bart.stuy.edu'+urlplus+'">next page</a>'
    print pi
    print '</center></td></tr></table>'
    print '''</br>
    </table></center>
    All data used is from baseball-reference.com, and can be found from 
    <a href="http://www.baseball-reference.com/leagues/MLB/2012.shtml">here.</a></br> 
    Data from all seasons in between 2012 and 1996 as well as data from 1993 was used,
    and data from each of those seasons can be easily found using the link above.</br>
    <a href="data1.csv">Press here to download pitching data.</a></br>
    <a href="data2.csv">Press here to download hitting data.</a></br>
    </body></html>'''
    
#Updates:
    #17:
        #Added team name, year to raw data
        #combined analisys and data into one file
    #18:
        #Tweaked page system so that navigating to http://.../analisys18.py without a value for 'pg' will not cause an error.
        #Added (non-working) forms to the top of each data table
        #Combined the two data tables into one
        #Added functionality to 'display up to n results per page' menu
    #19:
        #Added filter functionality
        #Changed information about data collected slightly to reflect new data (team name, year).
    #20:
        #Added 'sort by' functionality. All options on how to display raw data are now functional.
    #22:
        #Changed formatting on page displaing data analisys so that it displays the two data tables side by side.
        #Added a section (in the analisys page) about the problems encountered during the revision of the project.
    #26:
        #Added 'next page' and 'previous page' options to raw data table
