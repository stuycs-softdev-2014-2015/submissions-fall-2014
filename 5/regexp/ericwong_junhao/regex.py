import re

one = open('huckleberryfin.txt', 'r')
book1 = one.read()
one.close()

def findname():
    namelist = []
    #split all text an only keep two words in a row that are both capitalized
    word1 = re.split("[A-Z]\w+ [A-Z]\w+", book1)

    #add all name pairs into namelist
    for name in word1:
        namelist.append(name)

    #find new first names
    #resplit by call caps + two characters behind it
    word2 = re.split("..[A-Z]\w+", book1)

    #filter only those that are not start of sentence (first character is not period)
    for name in word2:
        if not(".".in(name)):
            namelist.append()
    
    #extract first names from name pairs (first last)
    #will not find new first names, only count how many times name is mentioned
    first = []
    for name in namelist:
        first.append(re.search("[A-Z]\w+", name))
    

if __name__=="__main__":
    findname()
