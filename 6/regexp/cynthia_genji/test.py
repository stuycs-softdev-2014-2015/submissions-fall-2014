import string
import re
import unittest

#class TestDemo(unittest.TestCase)

berries = open("berry.txt",'r').read().replace("\n","")
saw = open("saw.txt",'r').read().replace("\n","")
giver = open("giver.txt",'r').read().replace("\n","")
twilight = open("twilight.txt",'r').read().replace("\n","")
moon = open("new_moon.txt",'r').read().replace("\n","")
breaking = open("breaking_dawn.txt",'r').read().replace("\n","")
hunger = open("hunger_games.txt",'r').read().replace("\n","")

common_words = open("common_words.txt",'r').read().splitlines()
#A LIST WITH THE 1000 MOST COMMON WORDS: FROM http://www.giwersworld.org/computers/linux/common-words.phtml
#I DELETED 'MISS' FROM THE TXT FILE CUZ 'MISS WATSON'

common_words.extend(["PROJECT", "GUTENBERG", "LITERARY", "ARCHIVE", "INTERNAL", "REVENUE", "DIRECTOR", "PUBLIC", "DOMAIN", "PUSH", "SKY", "HARBOR", "PENINSULA", "SPORTS", "RABBIT", "PIG", "GOAT", "HUNGER", "GAMES"])
#I ADDED ADDITIONAL WORDS THAT ARE APPEAR IN BERRIES. ARE WE ALLOWED TO DO THAT?

common_cities = open("common_cities.txt",'r').read().replace(" ","\n").splitlines()


names = []
sortedNames = []

def findMatches(text):

    #################FIND MATCHES
    n = re.compile("[A-Z][a-z]+\040[A-Z][a-z]+")
    #names = n.match(text)
    #print names.group()
    names = n.findall(text)
    print names

    #################SORT MATCHES
    n = re.compile("[A-Z][a-z]+")
    for name in names:
        first_last = n.findall(name)
        first = first_last[0]
        last = first_last[1]
        if first.upper() not in common_words and last.upper() not in common_words and first not in common_cities and last not in common_cities: #all the words in the fileare in capital letters
            sortedNames.append(name)
        else:
            print name
    print sortedNames
                
if __name__ == "__main__":
    findMatches(hunger)
    
    #print common_words
