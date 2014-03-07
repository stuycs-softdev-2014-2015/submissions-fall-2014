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
    return math.sqrt(sum([pow(x[0]-x[1],2) for x in zip(a,b)]))

def calcPercents(s):
    l = [c for c in s]
    x = [l.count(c) for c in "abcdefghijklmnopqrstuvwxyz"]
    total = sum(x)
    return [100*float(i)/total for i in x]
    """
    Returns a list of 26 elements L[0] will be the frequency of
    the letter a i the list, L[1] the letter b etc.

    You can calculate the frequence by calculating
    (# times the letter appears)/(total # of letters)
    """
   



def decode(s):
    ssf = calcPercents(open('pg100.txt','r').read())
    sents = [encode2(s,i) for i in range(26)]
    dists = [dist(calcPercents(n),ssf) for n in sents]
    return sents[dists.index(min(dists))]


import random
s="math is number one"
# This is encoded message
encmessage = encode2(s,random.randrange(26))

print decode(encmessage)

# Your tasks
#1. Rewrite dist so that it uses a list comprehention
#2. Finish writing calcPercents
#
#3. For each of the 26 possible rotations of encmessage (the encoded message)
#   see the distance between it and the englishPerents. The closest should
#   be the amount needed to decode the message
#n
#4. Instead of using englishPercents, download a book from project Gutenberg
#   I'd say the Complete works of Shakespeare. Read it in and use it to
#   calculate letter frequencies.
