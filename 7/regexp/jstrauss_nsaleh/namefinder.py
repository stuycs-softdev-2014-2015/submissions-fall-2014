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
	justthenames = []
	for name in names:
		justthenames.append( name[name.find(":")+2:] )
	return justthenames

	#possibleNames = re.match("[A-Z][a-z]+\s(([A-Z][a-z-]+){1,2})",text)
	#possibleNames.group(0)
	#return possibleNames

if __name__=="__main__":
	#filename = raw_input("What file do you want to find people's names in?\n")
	#try:
	print processTripleNames(readText(str("test.txt")))
	#except:
	#	print "Filename invalid. Please try again."