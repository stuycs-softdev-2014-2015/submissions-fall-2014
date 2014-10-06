import re
first = [name.strip() for name in open('first.txt', 'r').read().split('|')]
last = [last for last in open('last.txt', 'r').read().split('|')]
firstAdd, lastAdd = [], []

test = """Dear my boy John Smith, 
     You have a very typical name, it should get recognized on the first run.
However, Hubert Puszklewicz or Eric Morgenstern won't be detected a first because of their last names. However, on the second run through, their names should be
matched. The same can apply with names where the last name is recognized, but first isn't. Lastly, Mr. Lester Smith should be taken care of as well.
Sincerely,
Hubert"""

def findNames(text, n=2):
    possibleFull=re.findall("((([A-Z][a-z]+)|M([rs]|rs)\.)( [A-Z][a-z]+)+)",text)
    L = []
    for k in possibleFull:
        L.append(k[0])
    print L

findNames(test)



