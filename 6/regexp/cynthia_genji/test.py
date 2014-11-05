import string
import re
import unittest

#class TestDemo(unittest.TestCase)

berries = open("./texts/berry.txt",'r').read().replace("\n","")
saw = open("./texts/saw.txt",'r').read().replace("\n","")
giver = open("./texts/giver.txt",'r').read().replace("\n","")
twilight = open("./texts/twilight.txt",'r').read().replace("\n","")
moon = open("./texts/new_moon.txt",'r').read().replace("\n","")
breaking = open("./texts/breaking_dawn.txt",'r').read().replace("\n","")
hunger = open("./texts/hunger_games.txt",'r').read().replace("\n","")
wiki = open("./texts/wiki_history_of_science.txt",'r').read().replace("\n","")

common_words_1000 = open("common_words_1000.txt",'r').read().splitlines()
common_words_10000 = open("common_words_10000.txt",'r').read().splitlines()
#A LIST WITH THE 1000 MOST COMMON WORDS: FROM http://www.giwersworld.org/computers/linux/common-words.phtml
#I DELETED 'MISS' FROM THE TXT FILE CUZ 'MISS WATSON'
#common_words_10000.txt comes from https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt

common_words_1000.extend(["PROJECT", "GUTENBERG", "LITERARY", "ARCHIVE", "INTERNAL", "REVENUE", "DIRECTOR", "PUBLIC", "DOMAIN", "PUSH", "SKY", "HARBOR", "PENINSULA", "SPORTS", "RABBIT", "PIG", "GOAT", "HUNGER", "GAMES"])
#I ADDED ADDITIONAL WORDS THAT ARE APPEAR IN BERRIES. ARE WE ALLOWED TO DO THAT?

common_cities = open("common_cities.txt",'r').read().replace(" ","\n").splitlines()

common_names_text = open("common_names.txt",'r').read()
#common_names.txt from http://names.mongabay.com/female_names.htm
#the text has names as well as numbers, so only get the names with regex
r = re.compile("[A-Z]+")
common_names = r.findall(common_names_text)

common_names.extend(["UNCLE", "SISTER", "AUNT", "JUDGE", "BROTHER"])


###The learned names
learned_names = open("learned_names.txt",'r').read().splitlines()


names = []
sortedNames = []
new_names = []

def findMatches(text):

    #################FIND MATCHES
    n = re.compile("[A-Z][a-z]+\040[A-Z][a-z]+")
    #names = n.match(text)
    #print names.group()
    names = n.findall(text)

    #################SORT MATCHES
    n = re.compile("[A-Z][a-z]+")
    for name in names:
        first_last = n.findall(name)
        first = first_last[0]
        last = first_last[1]
        #first check if first name or last name is in the list common_names
        if first.upper() in common_names or first in learned_names:
            #if first name is in common_names, check to see if the last name is a name,
            #then check if the last name is a common word or city. if not, add to sortedNames list
            if last.upper() in common_names or first in learned_names:
                sortedNames.append(name)
            elif last.upper() not in common_words_1000 and last.lower() not in common_words_10000 and last not in common_cities:
                sortedNames.append(name)
                new_names.append(last)
        elif last.upper() in common_names or last in learned_names:
            if first.upper() not in common_words_1000 and first.lower() not in common_words_10000 and first not in common_cities:
                sortedNames.append(name)
                new_names.append(first)
        #if first name and last name are NOT in common_names, check to see if they're regular words. if not, it's probably a name so add it to the sortedNames list
        elif first.upper() not in common_words_1000 and first.lower() not in common_words_10000 and first not in common_cities and last.upper() not in common_words_1000 and last.lower() not in common_words_10000 and last not in common_cities:
            sortedNames.append(name)
            new_names.append(first)
            new_names.append(last)
        else:
            print name
    print sortedNames
    print "###################################################################################"
    print new_names

def writeNewWords():
    ###Write all of the newly-learned names into a text file called new_names.txt
    append = open("learned_names.txt",'a')
    while new_names:
        name = new_names.pop()
        if name not in new_names:
            if name not in learned_names:
                append.write(name+"\n")
    append.close()
                
if __name__ == "__main__":
    findMatches(breaking)
    writeNewWords()
