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
        # turns the raw census databases of names into lists
	instream = open(filename,'r')
	fulllist = instream.read().replace("\n"," ").split()
	instream.close()
	return [fulllist[x] for x in range(len(fulllist)) if x%4==0]

def findPossibleNames(filetext):
        possiblenames = []
        # uses a regular expression to find groups of 2 or 3 consecutive words all beginning with caps
        for m in re.finditer(r"(([A-Z][a-z-]+){1,2}\s){2,3}", filetext):
                possiblename = ( '%02d-%02d: %s' % (m.start(), m.end(), m.group(0)) )
                if possiblename[-1] == " ": # gets rid of trailing whitespace
                        possiblename = possiblename[:-1]
                        possiblenames.append(possiblename)
        return possiblenames
        
def filterNames (possiblenames):
        justthenames = [x[x.find(":")+2:] for x in possiblenames]
        # the list of names that doesn't include the location marker

        validnames = []
        # a list of indices of elements of justthenames that pass the test

        femaleNames = makeList("femalenames.txt")
        maleNames = makeList("malenames.txt")
        validlasts = makeList("surnames.txt")
        validfirsts = femaleNames + maleNames
        #our lists of "real" names

        for fullname in justthenames:
                if (not fullname in validnames) and nameCheck(fullname, validfirsts, validlasts):
                # checks for duplicates and references database
                        validnames.append(justthenames.index(fullname))

        return [x for x in possiblenames if possiblenames.index(x) in validnames]

def nameCheck(fullname,validfirsts,validlasts):
        nameparts = fullname.upper().replace("-"," ").split(" ")

        if len(nameparts)==2:
                return nameparts[0] in validfirsts and nameparts[1] in validlasts
        else:
                a = nameparts[0] in validfirsts
                b = (nameparts[1] in validfirsts) or (nameparts[1] in validlasts)
                c = nameparts[2] in validlasts
                return a and (b or c)
                # a must be true to prevent words like "Is" and "By" from getting through


def findNames(filename):
        filetext = readText(filename)
        possiblenames = findPossibleNames(filetext)
        print "Location: Person's Name"
        for name in filterNames(possiblenames):
                print name
        

if __name__=="__main__":
	filename = raw_input("What file do you want to find people's names in?\n")
	try:
	       findNames(filename)
	except:
	       print "Filename invalid. Please try again."
