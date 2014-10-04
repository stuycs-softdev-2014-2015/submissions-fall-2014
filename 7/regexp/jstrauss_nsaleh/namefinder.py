# Justin Strauss and Nadia Saleh
# Soft Dev Pd 7
# Project 3: Regex

import re

def readText(filename):
	# reads a file and returns it as a string of content
	instream = open(filename,'r')
	text = instream.read().replace("\n"," ")
	instream.close()
	return text

def listPossibleNames(filename):
	# uses a regular expression to pass the text through the first layer of filtration
	# any group of 1, 2, or 3 subsequent words beginning with caps will be added
	text = readText(filename)
for "." in 
	names = []
	for m in re.finditer(r"(([A-Z][a-z-\.]+){1,2}\s?){1,3}", text):
	     names.append( '%02d-%02d: %s' % (m.start(), m.end(), m.group(0)) )
	return names # returns a list 

def filterTwo():
	names = listPossibleNames("test.txt")
	justthenames = []
	for name in names:
		justthenames.append( name[name.find(":")+2:] )
	return names

	#possibleNames = re.match("[A-Z][a-z]+\s(([A-Z][a-z-]+){1,2})",text)
	#possibleNames.group(0)
	#return possibleNames

def findNames(filename):
	listPossibleNames(filename)
	filterTwo()

if __name__=="__main__":
	findNames("test.txt")
	#filename = raw_input("What file do you want to find people's names in?\n")
	#try:
	#	findNames(str(filename))
	#except:
	#	print "Filename invalid. Please try again."

timeIndicators = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",
				  "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]