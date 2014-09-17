#!/usr/bin/python
print 'Content-Type: text/html'
print

head = '''
    <!DOCTYPE HTML>
    <html>
    <head><title>NBA Analysis</title></head>
    <body>
        <center><h1>How Accurate are Mock Drafts for the 1st Round?</h1></center>
        <br>
        <b>Evolution of my analysis</b>
        <br>
        <br>
        My initial analysis of the data was to compare the college statistics of
        players selected in the first round and how it played a role in their
        placement among other potential draft picks.
        <br>
        I was also planning initially to see how the first round draft picks
        adapted to the competitive competition in the NBA thorugh a comparision
        of their college and rookie season statistics.
        <br>
        However, this proved extremely difficult because there was no single
        source for the set of data needed for the analysis.
        <br>
        In the end, my analysis evolved into a comparision of mock drafts created
        by various websites for the 1st round and how accurate they were compared
        to the actual proceedings of the draft.
        <br>
        Lastly, I decided to find the player efficiency rating (PER) of the first
        round picks and based on these findings, determine if the order in which
        they were picked mirrors their placement in the draft.
        <br>
        <br>
        <b>Obstacles faced</b>
        <br>
        <br>
        Finding the necessary data to complete the analysis I want to perform was
        definitly an obstacle that I faced because there is no website with the
        exact data set I needed.
        <br>
        Another obstacle that I faced was finding a way to concatanate the table so
        that I could produce the table I want.
        <br>
        '''
        
one = open('2012draft.csv', 'r')
info1 = one.readlines()
one.close()

two = open('2012draftexpress.csv', 'r')
info2 = two.readlines()
two.close()

three = open('2012NBAdraft.csv', 'r')
info3 = three.readlines()
three.close()

def formatdata(info):
    newdata = []
    for index in range(len(info)):
        line = info[index]
        line = line.replace('\n' , '')
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

def tablify():
    info = getanalysisinfo()
    ans = '<table border = "1">\n<tr>'
    #headers
    ans += '<th></th><th>Actual Draft</th><th>draftexpress</th><th>NBAdraft</th>'
    ans += '<tr>\n'
    ans += '<tr>'
    ans += '<th>Pk</th><th>Player</th><th>Player</th><th>Player</th>'
    ans += '<tr>\n'
    ans += '<tr>'
    for key in range(2, 32):
        ans += '<tr>'
        ans += '<td>' + info[key][0] + '</td>'
        ans += '<td>' + info[key][1] + '</td>'
        ans += '<td>' + info[key][2] + '</td>'
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
                
def getplayerlist():
    ans = {}
    info = formatdata(info1)
    for key in range(0, 31):
        ans[info[key][2]] = info[key][4:]
    return ans

def PERcalculator(player):
    if player == 'Royce White' or not(player in getplayerlist()):
        return 0
    MPindex = 1
    PTSindex = 2
    TRBindex = 3
    ASTindex = 4
    FGindex = 5
    FTindex = 7
    MP = float(getplayerlist()[player][MPindex])
    PTS = float(getplayerlist()[player][PTSindex])
    TRB = float(getplayerlist()[player][TRBindex])
    AST = float(getplayerlist()[player][ASTindex])
    FG = float(getplayerlist()[player][FGindex])
    FT = float(getplayerlist()[player][FTindex])
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
    if draft == 'draft':
        for key in range(2, 32):
            ans += '<tr>'
            ans += '<td>' + info[key][0] + '</td>'
            ans += '<td>' + info[key][1] + '</td>'
            ans += '<td>' + str(PERcalculator(info[key][1])) + '</td>'
            ans += '</tr>\n'
    elif draft == 'draftexpress':
        for key in range(2, 32):
            ans += '<tr>'
            ans += '<td>' + info[key][0] + '</td>'
            ans += '<td>' + info[key][2] + '</td>'
            ans += '<td>' + str(PERcalculator(info[key][2])) + '</td>'
            ans += '</tr>\n'
    else:
        for key in range(2, 32):
            ans += '<tr>'
            ans += '<td>' + info[key][0] + '</td>'
            ans += '<td>' + info[key][2] + '</td>'
            ans += '<td>' + str(PERcalculator(info[key][3])) + '</td>'
            ans += '</tr>\n'
    ans += '</table>'
    return ans

body = '''  <br>
            Here is a table to shows the discrepencies between the two mock
            drafts and the actual draft results pick by pick.
            <br>
            <br>'''

body += tablify()

body += ''' <br>
            As it can be seen there are only 2 cases in which all three draft
            results match, the first and sixth pick.
            <br>
            It is no surprise that both mock drafts was correct in picking
            Anthony Davis as the first pick seeing as to how he was already
            a favorite from the beginning.
            <br>
            Both drafts were not very accurate in correcting predicitng the outcome
            of the draft.
            <br>
            NBAdraft had '''

body += str(howmanysame('draftexpress'))

body += ''' predictions that
            matched the actual results and similarly, draftexpress had '''

body += str(howmanysame('NBAdraft'))

body += ''' correct predictions.
            <br>
            Both of these numbers are not very high thus proving the difficult
            nature of guessing draft results.
            <br>
            An interesting observation was that in the NBAdraft mock draft, there
            were predictions in which those players were never picked in the first
            round, and had players being drafted to teams at times when it wasn't
            their turn to draft.
            <br>
            This was very confusing because I had thought that all these websites
            knew what draft pick each team had.
            <br>
            Besides these obstacles, the biggest of all was coming up with a
            function to calculat the PER for each of the draft picks.
            <br>
            Coming up with a function that incorporated basically all of each
            players statistics was not easy and took a long time to figure out
            the correct way to extract the correct information.
            <br>
            Nonetheless, I was able to accomplish my goal and the final feeling
            of defeating these obstacles was well worth the fight.'''
                                                                                
body += ''' <br>
            The next phase of my analysis delt with comparing the PER (player efficiency rating)
            of the first round draft picks based on their rookie season statistics
            and determine which draft out of the three makes the most sense.
            <br>
            <br>
            Here is how the PER of the actual draft results came out to be:
            <br>
        '''

body += tablifyPER('draft')

body += ''' <br>
            Here is how the PER of draftexpress's moxk draft results came out to be:
            <br>
        '''

body += tablifyPER('draftexpress')

body += ''' <br>
            Here is how the PER of NBAdraft's moxk draft results came out to be:
            <br>
        '''

body += tablifyPER('NBAdraft')

body += ''' <br>
            As it can be seen from the three tables above, there are major
            descrepencies as to the order in which the players were picked
            and their resepective PER scores.
            <br>
            It would have been expected that the higher a player was picked,
            the higher their PER should be.
            <br>
            However, this was not the overall trend seeing how the chart's PER
            column looked like a rollercoaster ride from high to low then back to
            high and sometimes plummeting down.
        '''

foot = '''
        <br>
        <br>
        <b>Areas of Improvement</b>
        <br>
        My choice of comparison, PER, is also not a very accurate reflection of the
        value of a player because it solely accounts for numerical statistics and
        not others like hustle, defensive efforts, and just their overall attitude
        for the game.
        <br>
        The official PER formula that is used is extremely complicated and therefore,
        I chose to use a simpler formula that I found <a href = "http://wagesofwins.com/2012/03/04/wayne-winston-simplifies-pers/">here</a>.
        <br>
        This simplified version, compounded with the already flawed nature of PER
        made the results relatively askew.
        <br>
        Disregarding its inaccuracy on some level, PER does give fans a great general
        overview on how each player is doing when compared to the league averages.
        <br>
        In addition, there were some players who either did not play this entire season
        due to psychological issues or were not even picked in the first round incorporated
        into the set of data.
        <br>
        The latter part of the group is due some of the mock drafts incorrectly placing
        players higher up that they were actually picked and because the rookie season
        statistics that I downloaded only referred to those actually picked in the
        first round, those players were unaccounted for.
        <br>
        As to make my calculations easier, I decided to designate these players with a
        PER of 0.
        <br>
        Lastly, it is unfair to determine whether each pick made better sense based
        solely on PER because for some teams they are lacking depth in certain
        positions and thus, must pick a player that is best suited for their team,
        not the best of the remaining players.
        <br>
        Because of this, some teams may have skipped over players who have more skill
        but do not play the right position they need for their team that year.
        <br>
        To make a further, and more accurate analysis, I would need to incorporate
        more aspects of the game into my calculations to get a fuller picture of
        each player's impact on the game.
        <br>
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
        <br>
        To find the data that I had used, visit <a href = "data.py">here</a>.
        </body>
    </html>'''

webpage = head + body + foot

print webpage
