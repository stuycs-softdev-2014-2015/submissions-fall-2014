

def encode1(s,n):
    """
    Rotate the string by n characters, leaving spaces
    Done with blow by blow comments
    """
    r = ""
    for l in s:
        l = ord(l) # convert to ascii
        l = l - 97 # 'a' is 97 so we want to reduce so 'a'=0 'b'=1 etc
        l = l + n # add the offset
        l=l%26 # use mod so that we wrap around back to 'a' if we go past 'z'
        l=l+97 # and add back the 97
        r = r + chr(l)
    return r

def encode2(s,n):
    """
    Rotate the string by n characters, leaving spaces
    Done with blow by blow comments
    """
    r = [ chr(((ord(x)-97+n)%26)+97) if x!=' ' else x for x in s]
    return "".join(r)


import math
def dist(a,b):
    c = [pow(a[i]-b[i],2) for i in range(len(a))]
    total = sum(c)
    return math.sqrt(total)


def calcPercents(s):
    """
    Returns a list of 26 elements L[0] will be the frequency of 
    the letter a i the list, L[1] the letter b etc. 

    You can calculate the frequence by calculating 
    (# times the letter appears)/(total # of letters)
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    frequencies = [[1 for i in s if i == j] for j in alpha]
    length = len(s)
    return [float(sum(c))/float(length) for c in frequencies]  


f = open('GrimmsFairyTales.txt','r')
fairytales = f.read()
englishPercents = calcPercents(fairytales)

import random
s="this is a sample sentence for use in testing the ceasar cipher thing"
# This is encoded message
encmessage = encode2(s,random.randrange(26))
print "Encoded:", encmessage


distances = [dist(calcPercents(encode2(encmessage,i)),englishPercents) for i in range(0,26)]
print "Decoded:",encode2(encmessage, distances.index(min(distances)))

