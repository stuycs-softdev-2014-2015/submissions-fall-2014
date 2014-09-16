#!/usr/bin/python
print 'Content-Type: text/html'
print

head = '''
    <!DOCTYPE HTML>
    <html>
    <head><title>NBA Analysis</title></head>
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
        Chose because: #basketballneverstops
        <center><h1>How Accurate are Mock Drafts for the 1st Round?</h1></center>
        <br>
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
        <br>'''

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
    for index in range(len(info)):
        line = info[index]
        line = line.replace('\r\n' , '')
        line = line.split(',')
        info[index] = line[0:12]
    return info

def tablify(info):
    ans = '<table border = "1"><tr>\n'
    tableinfo = formatdata(info)
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

body = '''
        <br>
        These are the actual results from the draft and their rookie season statistics:
        <br>'''
body += tablify(info1)
body += '''
        <br>
        These are the mock drafts created by Draft Express and NBAdraft.
        <br>
        <b>Draft Express:</b>
        <br>'''
body += tablify(info2)
body += '''
        <br>
        <b>NBAdraft:</b>
        <br>'''
body += tablify(info3)


foot = '''
    <br>
    For more in-depth analysis on these sets of data, visit
    <a href = "analysis.py">here</a>.
    </body>
</html>'''

webpage = head + body + foot

print webpage
        
        
