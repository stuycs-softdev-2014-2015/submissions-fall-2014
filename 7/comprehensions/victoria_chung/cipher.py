
def encode1(s,n):
    """
    Rotate the string by n characters, leaving spaces
    Done with blow by blow comments
    """
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
    """
    Rotate the string by n characters, leaving spaces
    Done with blow by blow comments
    """
    r = [ chr(((ord(x)-97+n)%26)+97) if x!=' ' else x for x in s]
    return "".join(r)


import math
def dist(a,b):
    sum=0
    for i in range(len(a)):
        sum = sum + pow(a[i]-b[i],2)
    return math.sqrt(sum)

def dist2(a,b):
    return math.sqrt(sum([(pow(a[i]-b[i],2)) for i in range(len(a))]))


def calcPercents(s):
    """
    Returns a list of 26 elements L[0] will be the frequency of 
    the letter a i the list, L[1] the letter b etc. 

    You can calculate the frequence by calculating 
    (# times the letter appears)/(total # of letters)
    """
    return [(float(s.count(chr(i+97)))*100)/float(len(s.replace(" ",""))) for i in range(26)]

englishPercents=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,
                 6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,
                 5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];
  

from operator import itemgetter
def decode(s):
    l=[dist2(calcPercents(encode2(s,x)),englishPercents) for x in range(26)]
    pos=min(enumerate(l), key=itemgetter(1))[0]
    return encode2(s,pos)

import random
s="as;dlkfja;slkrgj;alkerjt;alksemral;ksmdc;lkasegoi a;sedkjfa;s"
# This is encoded message
enccodedddd = encode2(s,random.randrange(26))


text=open("shakespeare.txt")
percentage=calcPercents(text.read())
text.close()
