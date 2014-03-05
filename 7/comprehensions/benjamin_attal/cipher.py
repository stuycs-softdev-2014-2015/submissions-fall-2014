
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
    return math.sqrt(sum([ (a[i] - b[i]) ** 2 for i in range(len(a)) ]))

    

def calcPercents(s):
    """
    Returns a list of 26 elements L[0] will be the frequency of 
    the letter a i the list, L[1] the letter b etc. 

    You can calculate the frequence by calculating 
    (# times the letter appears)/(total # of letters)
    """
    no_ws = "".join([c for c in s.lower() if 'a' <= c <= 'z'])
    return [ (float(s.count(c)) / float( len( no_ws ) ) ) * 100.0 for i in range(ord('a'), ord('z') + 1) for c in [chr(i)] ]


def decode(s):
    dists = [(dist(calcPercents(a), englishPercents), a) for i in range(1, 27) for a in [encode2(s, i)]]
    return sorted(dists, key=lambda tup: tup[0])[0][1]
  

import random
s="this is a sample sentence for use in testing the ceasar cipher thing"
# This is encoded message
encmessage = encode2(s,random.randrange(26))

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

shake = open('shakespeare.txt')
englishPercents = calcPercents(shake.read())
shake.close()

print decode(encmessage)
