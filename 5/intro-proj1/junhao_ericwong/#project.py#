#!/usr/bin/python
print 'Content-type: text/html'
print

###################################################################################
    #getting all that basic info first

import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()

page = '''<html>
    <head><title>NBA Analysis Upgrade</title></head>
    <body>
    Wong, Eric
    <br>
    MKS22-6
    <br>
    Period-04
    <br>
    DATASET: First Round Picks and Mock First Round Picks and PER (Player Efficiency Rating)
    <br>
    DATASOURCE: Actual Picks and Rookie Stats:<a href = "http://www.basketball-reference.com/draft/NBA_2012.html">here</a>
                Mock Drafts: <a href = "http://nbadraft.net/2012mock_draft">NBAdraft</a> and
                            <a href = "http://www.draftexpress.com/nba-mock-draft/2012/">Draft Express</a>
    <br>
    <h1><center>Should we Trust Mock Drafts?</center></h1>'''

#################################################################################
    #defining them fuctions

def formatdata(info):
    newdata = []
    for index in range(len(info)):
        line = info[index]
        line = line.strip('\r\n')
        line = line.split(',')
        newdata.append(line)
    return newdata

def getanalysisinfo():
    analysis = {}
    draft = formatdata(info1)
    draftexpress = formatdata(info2)
    NBAdraft = formatdata(info3)
    for pick in range(1, 32):
        index = pick - 1
        analysis[pick] = [draft[index][0], draft[index][2], draftexpress[index][2], NBAdraft[index][2]]
    return analysis

def tablifydraft(draft):
    ans = '<table border = "1"><tr>\n'
    if draft == 'draft':
        tableinfo = formatdata(info1)
    if draft == 'draftexpress':
        tableinfo = formatdata(info2)
    if draft == 'NBAdraft':
        tableinfo = formatdata(info3)
    #getting headers
    for x in tableinfo[0]:
            ans += '<th>' + str(x) + '</th>'
    ans += '</tr>\n'
    ans += '<tr>'
    for row in tableinfo[1:]:
        for data in row:
            ans += '<td>' + str(data) + '</td>\n'
        ans += '</tr>\n'
    ans += '</table>'
    return ans

def tablifypick(draft):
    info = getanalysisinfo()
    ans = '<table border = "1">\n<tr>'
    #headers
    ans += '<th></th><th>' + draft + '</th>'
    ans += '<tr>\n'
    ans += '<tr>'
    ans += '<th>Pk</th><th>Player</th>'
    ans += '<tr>\n'
    ans += '<tr>'
    for key in range(2, 32):
        ans += '<tr>'
        ans += '<td>' + info[key][0] + '</td>'
        if draft == 'draft':
            ans += '<td>' + info[key][1] + '</td>'
        if draft == 'draftexpress':
            ans += '<td>' + info[key][2] + '</td>'
        if draft == 'NBAdraft':
            ans += '<td>' + info[key][3] + '</td>'
        ans += '</tr>\n'
    ans += '</table>'
    return ans

def howmanysame(draft):
    ans = 0
    data = getanalysisinfo()
    if draft == 'draftexpress':
        for pick in range(2, 30):
            if data[pick][1] == data[pick][2]:
                ans += 1
    else:
        for pick in range(2, 30):
            if data[pick][1] == data[pick][3]:
                ans += 1
    return ans 

def PERcalculator(player):
    if not(player in playerinfo):
        return 0
    MPindex = 1
    PTSindex = 2
    TRBindex = 3
    ASTindex = 4
    FGindex = 5
    FTindex = 7
    MP = float(playerinfo[player][MPindex])
    PTS = float(playerinfo[player][PTSindex])
    TRB = float(playerinfo[player][TRBindex])
    AST = float(playerinfo[player][ASTindex])
    FG = float(playerinfo[player][FGindex])
    FT = float(playerinfo[player][FTindex])
    if MP == 0.0:
        return 0
    ans = 45.75*(PTS/MP)+22.55*(TRB/MP)+32.8*(AST/MP)+58.2*((0.00383*TRB)/MP)-48.65*((0.017*AST)/MP) -39.73*((100*(1-FG))/MP) -20.6*((100*(1-FT))/MP)+38.37*((.0035*AST)/MP)-18.68*((0.02*AST)/MP)
    return ans

def tablifyPER(draft):
    info = getanalysisinfo()
    ans = '<table border = "1">\n<tr>'
    #headers
    ans += '<th></th><th>' + draft + '</th><th></th>'
    ans += '<tr>\n'
    ans += '<tr>'
    ans += '<th>Pk</th><th>Player</th><th>PER</th>'
    ans += '<tr>\n'
    ans += '<tr>'
    for key in range(2, 32):
        ans += '<tr>'
        ans += '<td>' + info[key][0] + '</td>'
        if draft == 'draft':
            ans += '<td>' + info[key][1] + '</td>'
            ans += '<td>' + str(PERcalculator(info[key][1])) + '</td>'
        if draft == 'draftexpress':
            ans += '<td>' + info[key][2] + '</td>'
            ans += '<td>' + str(PERcalculator(info[key][2])) + '</td>'
        if draft == 'NBAdraft':
            ans += '<td>' + info[key][3] + '</td>'
            ans += '<td>' + str(PERcalculator(info[key][3])) + '</td>'
        ans += '</tr>\n'
    ans += '</table>'
    return ans

########################################################################################
    #using the form information to alter data taken.

year = '2010'

if 'year' in form:
    if form['year'].value == '2011':
        year = '2011'
    if form['year'].value == '2012':
        year = '2012'

one = open(year + 'draft.csv', 'r')
info1 = one.readlines()
one.close()

two = open(year + 'draftexpress.csv', 'r')
info2 = two.readlines()
two.close()

three = open(year + 'NBAdraft.csv', 'r')
info3 = three.readlines()
three.close()

def getplayerlist():
    ans = {}
    info = formatdata(info1)
    for key in range(0, 31):
        ans[info[key][2]] = info[key][4:]
    return ans

playerinfo = getplayerlist()

if 'type' in form:
    if form['type'].value == 'stat':
        if not 'PTS' in form:
            for player in playerinfo:
                playerinfo[player][2] = '0'
        if not 'TRB' in form:
            for player in playerinfo:
                playerinfo[player][3] = '0'
        if not 'AST' in form:
            for player in playerinfo:
                playerinfo[player][4] = '0'
        if not 'FG' in form:
            for player in playerinfo:
                playerinfo[player][5] = '0'
        if not 'FT' in form:
            for player in playerinfo:
                playerinfo[player][7] = '0'

######################################################################################
    #actual website pages

if len(form) == 0:
    page += '''
    <br>
    With the 2012-2013 NBA playoffs coming to an end and the 2013 draft
    coming up, it is, once again, time to flock to those mock draft sites
    and predict each player's fortunes.
    <br>
    However, which site should we use? Which site can we trust with our hopes for the new draft class? Is Nerlen Noels going to be picked first and how will Shabazz Mohammed fair in his NBA dreams?
    <br>
    In this analysis, we will be taking the draft results and mock drafts from draftexpress and NBAdraft to determine which of the two mocks are better.
    <br>
    Another wonder that has haunted many NBA fans who watch little known college players being taken higher in the draft than their idol from Kentucky.
    <br>
    This analysis will also use a custom PER calculation to determine how each player has done in the debut in the NBA to see if they deserved that high spot in the draft.
    <br>
    To find what you want without wasting precious time away from the exciting NBA playoffs, you can choose what you want to be compared:
    <br>
    <br>
    <table border='1'>
    <form name='input' action='project.py' method='get'><br>
    <tr><td>
    By Statistics <input type='radio' name='type' value='stat'>
    </td><td>
    What statistics do you want included?<br>
    <input type='checkbox' name='PTS'>PTS(Points Scored)<br>
    <input type='checkbox' name='TRB'>TRB(Rebounding)<br>
    <input type='checkbox' name='AST'>AST(Assist)<br>
    <input type='checkbox' name='FG'>FG(Field Goal Percentage)<br>
    <input type='checkbox' name='FT'>FT(Free Throw Percentage)<br>
    </td></tr>
    <tr><td>
    By Draft <input type='radio' name='type' value='draft'>
    </td><td>
    Which drafts do you want to compare?<br>
    <input type='checkbox' name='draftexpress'>draftexpress.com<br>
    <input type='checkbox' name='NBAdraft'>NBAdraft.com<br>
    </td></tr>
    <tr><td>
    <input type='submit' name='compare' value='Compare!'>
    <input type='hidden' name='year' value='2010'>
    <input type='hidden' name='actualdraft' value='on'>
    </td></tr>
    </table><br>
    </form>'''

if 'compare' in form:
    if not 'type' in form:
        page += 'Please choose a type of comparison.'
    else:
        page += '''
            Every year, with the NBA draft approaching, basketball fans from all
            over begin to scour the internet for draft predictions.
            <br>
            These websites such as <a href = "NBAdraft.com">NBAdraft</a> and
            <a href = "www.draftexpress.com">Draft Express</a>
            base their predictions on the skills, physical attribution, and
            performance in college and how these sets of information would place
            them in the NBA draft.
            <br>
            Although the various sites that provide this service are not always in
            agreement with each other, they do provide a broad and agreeable prediction
            for each player that has taken into account the needs of the teams and
            how each player would be able to adjust to the higher competition in the
            NBA.
            <br>
            Being a basketball fan myself, I have found myself in that position often
            but I never really knew, or cared to find out, until now, how accurate
            these sites are.
            <br>
            In my study, I plan to find out the accuracy of several websites that
            produces mock drafts. I will select the three websites mentioned above
            and compare their predictions to the actual draft results for 2012. I
            will then determine whether the mock draft or actual draft was the one
            that seems more sensible by comparing the rookie season statistics of
            the players.
            <br>
            <hr>
            <br>'''
        if form['type'].value == 'stat':
            page += '''
            <br>
            These are the first round drafts from the actual NBA draft, the mock draft
            of draftexpress and NBAdraft.
            <br>'''
            page += '<b>Draft</b><br>' + tablifydraft('draft') + '<br>'
            page += '<b>draftexpress</b><br>' + tablifydraft('draftexpress') + '<br>'
            page += '<b>NBAdraft</b><br>' + tablifydraft('NBAdraft') + '<br>'
            page += '''
            <br>
            <hr>
            <br>
            Here is a table that shows the discrepencies between the two mock drafts and the
            actual draft results pick by pick.
            <br>
            <table>'''
            page += '<tr><td>' + tablifypick('draft') + '</td><td>' + tablifypick('draftexpress') + '</td><td>' + tablifypick('NBAdraft') + '</td></tr>'
            page += '''
            </table>
            <br>
            It is not surprising to see how inaccurate the mock drafts were at predicting
            the outcome of the draft due to the trades teams may make during the draft, the
            performance each potential draft pick gives during the draft workouts, and the
            needs of certain teams.
            <br>
            Therefore, it is no surprise that drafexpress only had '''
            page += str(howmanysame('draftexpress'))
            page += ' correct predictions and NBAdraft only had '
            page += str(howmanysame('NBAdraft'))
            page += ' correct predicitons.'
            page += '''
            <br>
            <hr>
            <br>
            Here is a table that displays the player efficiency rating (PER) of each first
            round draft picks in using their rookie season statistics.
            <table>'''
            page += '<tr><td>' + tablifyPER('draft') + '</td><td>' + tablifyPER('draftexpress') + '</td><td>' + tablifyPER('NBAdraft') + '</td></tr>'
            page += '''
            </table>
            <br>
            From the data above, it can be seen that for the drafts, none of them had a
            list in which the PER showed a decreasing trend and the PER flucuated greatly from
            one pick to the next.
            <br>
            <hr>
            <br>
            <b>Conclusion</b>
            <br>
            <br>
            From my analysis of the data, there is no webstie that is truly accurate
            their predictions of the draft results.
            <br>
            This is entirely understandable because it is practically impossible to
            determine the exact proceedings of the evening due to sudden changes in
            mind, new scouting reports, and inconsistency of humans.
            <br>
            As to which draft list made the most sense when each player's PER was taken
            into account, the conclusion is the same.
            <br>
            In addition, there is no "perfect draft" where the best players based on talent
            will be picked on after the other because sometimes, a team does not need four
            starting-caliber point guards
            <br>
            The conclusion that I am able to reach after performing this anaylsis
            is that all websites are just as good to use as sources of information
            for predicted draft results and you might as well as just use whatever
            you are comfortable with.
            <br>'''
        if form['type'].value == 'draft':
            page += '''
            <br>
            These are the first round drafts from the actual NBA draft '''
            if 'draftexpress' in form and 'NBAdraft' in form:
                page += ', draftexpress, and NBAdraft.'
            if 'draftexpress' in form:
                page += 'and draftexpress'
            if 'NBAdraft' in form:
                page +=  'and NBAdraft.'
            page += '<br>'
            page += '<b>Draft</b><br>' + tablifydraft('draft') + '<br>'
            if 'draftexpress' in form:
                page += '<b>draftexpress</b><br>' + tablifydraft('draftexpress') + '<br>'
            if 'NBAdraft' in form:
                page += '<b>NBAdraft</b><br>' + tablifydraft('NBAdraft') + '<br>'
            page += '''
            <br>
            <hr>
            <br>
            Here is a table that shows the discrepencies between the mock drafts and the
            actual draft results pick by pick.
            <br>
            <table><tr>'''
            page += '<td>' + tablifypick('draft') + '</td>'
            if 'draftexpress' in form:
                page += '<td>' + tablifypick('draftexpress') + '</td>'
            if 'NBAdraft' in form:
                page += '<td>' + tablifypick('NBAdraft') + '</td>'
            page += '''
            </tr></table>
            <br>
            It is not surprising to see how inaccurate the mock drafts were at predicting
            the outcome of the draft due to the trades teams may make during the draft, the
            performance each potential draft pick gives during the draft workouts, and the
            needs of certain teams.
            <br>
             Therefore, it is no surprise that '''
            if 'draftexpress' in form and 'NBAdraft' in form:
                page += 'drafexpress only had '
                page += str(howmanysame('draftexpress'))
                page += ' correct predictions and NBAdraft only had '
                page += str(howmanysame('NBAdraft'))
                page += ' correct predicitons.'
            if 'draftexpress' in form:
                page += 'drafexpress only had '
                page += str(howmanysame('draftexpress'))
                page += ' correct predictions.'
            if 'NBAdraft' in form:
                page += 'drafexpress only had '
                page += str(howmanysame('NBAdraft'))
                page += ' correct predictions.'
            page += '''
            <br>
            <hr>
            <br>
            Here is a table that displays the player efficiency rating (PER) of each first
            round draft picks in using their rookie season statistics.
            <table><tr>'''
            if 'actualdraft' in form:
                page += '<td>' + tablifyPER('draft') + '</td>'
            if 'draftexpress' in form:
                page += '<td>' + tablifyPER('draftexpress') + '</td>'
            if 'NBAdraft' in form:
                page += '<td>' + tablifyPER('NBAdraft') + '</td>'
            page += '''
            <tr></table>
            <br>
            From the data above, it can be seen that in all of the drafts, none of them had a
            list in which the PER showed a decreasing trend and the PER flucuated greatly from
            one pick to the next.
            <br>
            <hr>
            <br>
            <b>Conclusion</b>
            <br>
            <br>
            From my analysis of the data, there is no webstie that is truly accurate
            their predictions of the draft results.
            <br>
            This is entirely understandable because it is practically impossible to
            determine the exact proceedings of the evening due to sudden changes in
            mind, new scouting reports, and inconsistency of humans.
            <br>
            As to which draft list made the most sense when each player's PER was taken
            into account, the conclusion is the same.
            <br>
            In addition, there is no "perfect draft" where the best players based on talent
            will be picked on after the other because sometimes, a team does not need four
            starting-caliber point guards
            <br>
            The conclusion that I am able to reach after performing this anaylsis
            is that all websites are just as good to use as sources of information
            for predicted draft results and you might as well as just use whatever
            you are comfortable with.
            <br>'''
        page += '''
            <br>
            If this draft's analysis did not satisfy you enough, click below to choose
            a different draft.
            <br>'''
        url = 'http://bart.stuy.edu/~eric.wong/analysisV2/project.py?'
        if 'compare' in form:
            url += 'compare=Compare!&'
            if 'type' in form:
                if form['type'].value == 'stat':
                    url += 'type=stat&'
                if form['type'].value == 'draft':
                    url += 'type=draft&'
            if 'PTS' in form:
                url += 'PTS=on&'
            if 'TRB' in form:
                url += 'TRB=on&'
            if 'AST' in form:
                url += 'AST=on&'
            if 'FG' in form:
                url += 'FG=on&'
            if 'FT' in form:
                url += 'FT=on&'
            if 'actualdraft' in form:
                url += 'actualdraft=on&'
            if 'draftexpress' in form:
                url += 'draftexpress=on&'
            if 'NBAdraft' in form:
                url += 'NBAdraft=on&'
        if form['year'].value == '2010':
            page += "<a href='" + url + "year=" + str(int(form['year'].value) + 1) + "'>" + "<p align='right'>" + str(int(form['year'].value) + 1) + "</p></a>"
        if form['year'].value == '2011':
            page += "<a href='" + url + "year=" + str(int(form['year'].value) + 1) + "'>" + "<p align='left'>" + str(int(form['year'].value) - 1) + "</p></a>"
            page += "<a href='" + url + "year=" + str(int(form['year'].value) + 1) + "'>" + "<p align='right'>" + str(int(form['year'].value) + 1) + "</p></a>"
        if form['year'].value == '2012':
            page += "<a href='" + url + "year=" + str(int(form['year'].value) - 1) + "'>" + "<p align='left'>" + str(int(form['year'].value) - 1) + "</p></a>"
        page += '</form>'
        page += "To choose a return to the form, click <a href='http://bart.stuy.edu/~eric.wong/analysisV2/project.py'> here</a>."
page += '</body></html>'

print page

#21 - Today, I wrote out the basic intoductory form page that I would like to
#use in my new analysis. I have chosen to have my website allow the viewer to
#choose in three different catagories what information they would like to be
#compared. The problem that I am debating right now is whether or not to have
#everything on one py file or to have two where one will write code and the other
#just read what the other writes... a problem to be solved tomorrow when I have
#more time :( PEACE OUT


#22 - Today, I combined the coding that I had from the analysisV1 to have both the
#data and analysis on the same page. I also, started creating some alternative
#pages for when the form is not filled out completely or incorrectly like when
#they decided to compare one player to himself. Now that I have the bulk of my
#code in this python file, the option of making this two py files look tempting
#but I still have not decided if I should do this yet. Well... PEACE OUT

#23 - Today, I added onto my introduction page to have a way to narrow down the
#information I get from my form to make utilizing the information much easier.
#I also wrote out some basic code that will the bases for the rest of the
#code as to how to use the information from the form to get only the data the user
#wants in their analysis. One thing that I would like to do is to have more detailed
#choices to only appear if they want to compare, lets say, stats. I will need to look
#into what tags and coding is needed to make this affect in html. As of now, this code
#is really repetitive and can probably become more robust as I realize what I can
#take out of the code and still have it to work in the same way. The function of my
#website is still the same as last time but I now have the foundation for using the
#form. Well... PEACE OUT

#24 - Today, I found two more years worth of draft picks and their respective mock
#drafts and converted them into csv files. I also fixed up some of the code as
#well so that it would work more flexibly so that it can change depending on the
#options that were selected in the form. I have also decided to change up my form
#a little bit because by choosing what year you want to compare as opposed to
#choosing which players you want to compare is more practical and makes more sense.
#This way, it should be much easier to transition from my old analysis to this new one.
#I also decided to take out the old analysis so that it will not clog up my coding
#and make this py file look more elegant and reformatted the py file so that it
#is much more pleasing and clear to me now. Well... PEACE OUT
