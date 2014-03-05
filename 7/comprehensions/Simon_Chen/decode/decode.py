def getFreq(path):
    txt = str(open(path).read())
    #gets all the letters in the piece
    t = [ x for x in txt if x >= 'a' if x <= 'z']
    #gets the lettercount
    i = len(t)
    #makes an alphaphet list
    a = [chr(ord('a') + n) for n in range(26)]
    #gets the freq
    f = [float(t.count(l))/i for l in a]
    #combines the alphaphet and frequencies
    lf = zip(a,f)
    #print "This is the " +path+ " letter frequency table"
    #print lf

    #nested loop slow
    #test = [[x for x in txt if x >= 'a' if x <= 'z'].count(l) for l in a]
    return f 

    
tf = getFreq("ivanhoe.txt")

import math                      
def dist(a,b):
    s = math.sqrt(sum([pow(i - j,2) for i in a for j in b]))
    #print s
    return s

#a = [1.,2.,3.,4.,5.]
#b = [15.,46.,347.,3.]
#dist(a,b)

def encode2(s,n):
    """
    Rotate the string by n characters, leaving spaces
    Done with blow by blow comments
    """
    r = [ chr(((ord(x)-97+n)%26)+97) if x!=' ' else x for x in s]
    return "".join(r)

#Calc
def calcPercents(s,f):
    #gets all the letters in the string
    t = [ x for x in s if x >= 'a' if x <= 'z']
    #gets the lettercount
    i = len(t)
    #makes an alphaphet list
    a = [chr(ord('a') + n) for n in range(26)]
    #gets the freq
    sf = [float(t.count(l))/i for l in a]
    ans = dist(sf,f)
    return ans


import random
s="this is a sample sentence for use in testing ceasar cipher encoding"
# encmsg = encode2(s,random.randrange(26))
# print encmsg

englishPercents=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,
                 6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,
                 5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];

#main
def main():
    i = random.randrange(26)
    encs = [encode2(s, (i+x) % 26) for x in range(26)]
    enct = [calcPercents(encode2(s, (i+x) % 26),tf) for x in range(26)]
    decode = zip(enct,encs)
    decode.sort()
    print decode
    
main()
