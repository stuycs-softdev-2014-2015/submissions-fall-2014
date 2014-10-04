import re

#one = open('huckleberryfin.txt', 'r')
one = open('janeEyre.txt', 'r')
book = one.read().replace('\n',' ')
one.close()


### TO DO ###
# Account for UC (uppercase) words at start of sentence/start of quote,dialogue
# Titles such as: Mr., Ms., Mrs., Dr., Judge, Uncle, Aunt, King, Queen, Captain,
#                 Mister, Miss, Missus, Doctor, Captain, Lady, Lord, etc...


def findNames():
    #create a list with pairs of UC words
    #names = re.findall("[A-Z][a-z]+ [A-Z][a-z]+", book)

    #create a dict with key=name; value=occurrences 
    names = {}
    for match in re.finditer("(?<!\. )[A-Z][a-z]+ [A-Z][a-z]+", book):
        addToDict(match.group(),names)

    #debugging
    print names #debugging
    print "len: %d" % len(names)

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;


if __name__=="__main__":
    findNames()
