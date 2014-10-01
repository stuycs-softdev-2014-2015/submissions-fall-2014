import math
import random

def encode1(s,n):
    r = ""
    for l in s:
        l = ord(l) 
        l = l - 97 
        l = l + n 
        l=l%26 
        l=l+97 
        r = r + chr(l)
    return r

def encode2(s,n): 
    r = [ chr(((ord(x)-97+n)%26)+97) if x!=' ' else x for x in s]
    return "".join(r)

def dist(a,b):
    return math.sqrt(sum([pow(a[i]-b[i],2) for i in range(len(a))]))
    #return math.sqrt(sum([ (a[i] - b[i]) ** 2 for i in range(len(a)) ]))

def calcPercents(s):
#    no_ws = "".join([c for c in s.lower() if 'a' <= c <= 'z'])
#   return [ (float(s.count(c)) / float( len( no_ws ) ) ) * 100.0 for i in range(ord('a'), ord('z') + 1) for c in [chr(i)] ]
    return[float(s.count(chr(a))/len(s) for a in range (97,120))]

"""
englishPercents=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,
                 6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,
                 5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];
"""

def decode(s):
#    dists = [(dist(calcPercents(a), englishPercents), a) for i in range(1, 27) for a in [encode2(s, i)]]
#    return sorted(dists, key=lambda tup: tup[0])[0][1]  
    dists = [dist(calcPercents(encode2(encmessage,x)), englishPercents) for x in range(0,26)]
    return dists.index(min(dists)) 


s="this is a sample sentence for use in testing the ceasar cipher thing"
encmessage = encode2(s,random.randrange(26))

shake = open('shakespeare.txt')
englishPercents = calcPercents(shake.read())
shake.close()

print decode(encmessage)
