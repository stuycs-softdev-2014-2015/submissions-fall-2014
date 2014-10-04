# Justin Strauss and Nadia Saleh
# Soft Dev Pd 7
# Project 3: Regex

import re



timeIndicators = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



def readText(filename):
	# reads a file and returns it as a string of content
	instream = open(filename,'r')
	text = instream.read().replace("\n"," ")
	instream.close()
	return text

<<<<<<< HEAD
def listPossibleNames(filename):
	# uses a regular expression to pass the text through the first layer of filtration
	# any group of 2, or 3 subsequent words beginning with caps will be added
	text = readText(filename)
	names = []
	for m in re.finditer(r"(([A-Z][a-z]+\s?)(-?)){2,}", text):
                possiblename = m.group(0)
                if possiblename[-1] == " ":
                        possiblename = possiblename[:-1]
                names.append(possiblename)

                #names.append( '%02d-%02d: %s' % (m.start(), m.end(), m.group(0)) ) ##why the start and end?
	print names
        print "\n"
        return names # returns a list 

def filterTwo(names):
=======
def makeList(filename):
	# turns the raw census databases of names into lists
	instream = open(filename,'r')
	fulllist = instream.read().replace("\n"," ").split()
	instream.close()
	return {fulllist[x] for x in range(len(fulllist)) if x%4==0}



def processTripleNames(text):
	# uses a regular expression to find groups of 3 consecutive words all beginning with caps
	triplenames = []
	for m in re.finditer(r"(([A-Z][a-z-]+){1,2}\s){2}([A-Z][a-z-]+){1,2}", text):
	     triplenames.append( '%02d-%02d: %s' % (m.start(), m.end(), m.group(0)) )
	justthenames = []
	for name in triplenames:
		justthenames.append( name[name.find(":")+2:] )
	return justthenames

def processDoubleNames(text):
	# uses a regular expression to find groups of 2 consecutive words both beginning with caps
	doublenames = []

def processSingleNames(text):
	# uses a regular expression to find words beginning with caps
	singlenames = []


def filterTwo():
	names = listPossibleNames("stateoftheunion.txt")
>>>>>>> 810fd033f1fb8f1f764a9be6db9c4f7a5cb9b4aa
	justthenames = []
	for name in names:
		justthenames.append( name[name.find(":")+2:] )
	return justthenames

	#possibleNames = re.match("[A-Z][a-z]+\s(([A-Z][a-z-]+){1,2})",text)
	#possibleNames.group(0)
	#return possibleNames

<<<<<<< HEAD
def filterThree (possiblenames):
        newList = []
        for name in possiblenames:
                hasTimeWord = False
                eachword = name.split(" ")
                for word in eachword:
                        if  word in timeIndicators:
                                hasTimeWord = True
                if not hasTimeWord:
                        newList.append(name)
                                
        print newList
        return newList
        

def findNames(filename):
	possiblenames = listPossibleNames(filename)
	#filterTwo(possiblenames)
        filterThree(possiblenames)

if __name__=="__main__":

	findNames("test.txt")


=======
if __name__=="__main__":
>>>>>>> 810fd033f1fb8f1f764a9be6db9c4f7a5cb9b4aa
	#filename = raw_input("What file do you want to find people's names in?\n")
	#try:
	print processTripleNames(readText(str("test.txt")))
	#except:
<<<<<<< HEAD
	#	print "Filename invalid. Please try again."
=======
	#	print "Filename invalid. Please try again."
>>>>>>> 810fd033f1fb8f1f764a9be6db9c4f7a5cb9b4aa
