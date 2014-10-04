# Justin Strauss and Nadia Saleh
# Soft Dev Pd 7
# Project 3: Regex

import re

def readText(filename):
	# reads a file and returns it as a string of content
	instream = open(filename,'r')
	text = instream.read()
	instream.close()
	return text

def listPossibleNames(filename):
	# uses a regular expression to pass the text through the first layer of filtration
	# any 
	text = readText(filename)
	re.

def findNames(filename):
	print listPossibleNames(filename)

if __name__=="__main__":
	filename = raw_input("What file do you want to find people's names in?")
	findNames(filename)