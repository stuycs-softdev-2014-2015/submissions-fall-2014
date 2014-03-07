

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
    sum=0
    for i in range(len(a)):
        sum = sum + pow(a[i]-b[i],2)
    return math.sqrt(sum)

def dist2(a,b):
    return math.sqrt(sum([pow(a[i]-b[i],2) for i in range(len(a))]))
#   math.sqrt(sum([pow(x,y,2) for (x,y) in zip(a,b)]))

def calcPercents(s):
    """
    Returns a list of 26 elements L[0] will be the frequency of 
    the letter a in the list, L[1] the letter b etc. 

    You can calculate the frequence by calculating 
    (# times the letter appears)/(total # of letters)
    """
    L = [0.0 for x in range(26)]
    total = 0
    for x in range(len(s)-1):
        if s[x] == ' ':
            total = total + 1
        else:
            L[ord(s[x])-97] += 1   #count()
    L = [(x/total)*100 for x in L]
    return L
            
def decode(s):
    version = [calcPercents(encode2(s,i)) for i in range(26)]
    distances = [dist(englishPercents,i) for i in version]
    return encode2(s,distances.index(min(distances)))


englishPercents=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,
                 6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,
                 5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];
  

import random
s="this is a sample sentence for use in testing the ceasar cipher thing"
# This is encoded message
encmessage =encode2(s,random.randrange(26))

if __name__ == "__main__":
    print decode(encmessage)

# Your tasks
#1. Rewrite dist so that it uses a list comprehention
#2. Finish writing calcPercents
#
#3. For each of the 26 possible rotations of encmessage (the encoded message) 
#   see the distance between it and the englishPerents. The closest should
#   be the amount needed to decode the message
#
#4. Instead of using englishPercents, download a book from project Gutenberg
#   I'd say the Complete works of Shakespeare. Read it in and use it to 
#   calculate letter frequencies.

