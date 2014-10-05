# Justin Strauss and Nadia Saleh
# Soft Dev Pd 7
# Project 3: Regex

import re

def readText(filename):
	# reads a file and returns it as a string of content
	instream = open(filename,'r')
	text = instream.read().replace("\n"," ").replace("\r"," ")
	instream.close()
	return text

def makeList(filename):
        #turns the raw census databases of names into lists
	instream = open(filename,'r')
	fulllist = instream.read().replace("\n"," ").split()
	instream.close()
	return [fulllist[x] for x in range(len(fulllist)) if x%4==0]



def findPossibleNames(filetext):
        possiblenames = []
        for m in re.finditer(r"(([A-Z][a-z]+\s?)){2,}", filetext):
                possiblename = m.group(0)
                if possiblename[-1] == " ":
                        possiblename = possiblename[:-1]
                possiblenames.append(possiblename)
        return possiblenames
        
def filterNames (possiblenames):
        femaleNames = makeList("femalenames.txt")
        maleNames = makeList("malenames.txt")
        surnames = makeList("surnames.txt")
        firstNames = femaleNames + maleNames

        names = []

        for name in possiblenames:
                if not name in names and nameCheck(name,firstNames,surnames):
                        names.append(name)
        return names

def nameCheck(name, firsts, lasts):
        eachword = name.split(" ")
        firstName = eachword[0].upper()
        secondName = eachword[1].upper()
        if firstName in firsts:
                return True
        elif secondName in firsts or secondName in lasts:
                return True
        elif len(eachword) == 3:
                thirdName = eachword[2].upper()
                return True
        return False


def findNames(filename):
        filetext = readText(filename)
        possiblenames = findPossibleNames(filetext)
        print(filterNames(possiblenames))
        

if __name__=="__main__":
        findNames("prideandprejudice.txt")
	#filename = raw_input("What file do you want to find people's names in?\n")
	#try:
	#print processTripleNames(readText(str("test.txt")))
	#except:
	#	print "Filename invalid. Please try again."
