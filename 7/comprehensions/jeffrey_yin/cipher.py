

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


def dlist(a,b):
    return math.sqrt(sum([pow(x - y, 2) for (x,y) in zip(a,b)]))
                     
test1 = [1,2,3,4]
test2 = [1,4,2,9]
print dist(test1,test2)
print dlist(test1,test2)

def calcPercents(s):
    #could do this using list comprehensions, but would not get a linear performance
    ans = [ 0 for x in range(0,26)] #clumsy way of generating list of 26 0s
    num=0 #keeps track of number of letters
    for l in s:
        l = ord(l)-97 #adjust letters so ascii value == the index number
        if l > 0 and l < 26: #discard non-letters
            num = num + 1 
            ans[l] = ans[l] + 1
    return [float(x)/num*100 for x in ans]
        
def calcPercentsLC(s):
    #shorter...but 26n performance. notsureifworth
    ans =  [ sum(1 for l in s if ord(l)-97 == n) for n in range(0,26)]
    return [float(x)/sum(ans)*100 for x in ans]
print "calc percents"    
print calcPercents("hello world")
print "with list comp"
print calcPercentsLC("hello world")

englishPercents=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,
                 6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,
                 5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];

def decode(s):
    ans = [ dist(calcPercents(encode2(s.lower(), n)),englishPercents) for n in range (0, 26)]
    return encode2(s,ans.index(min(ans)))
print (encode2("To be or not to be, that is the question",0))
print decode(encode2("To be or not to be, that is the question",3))

def genEnglishPercents(s):
    englishPercents = calcPercents(s)
    pass
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

