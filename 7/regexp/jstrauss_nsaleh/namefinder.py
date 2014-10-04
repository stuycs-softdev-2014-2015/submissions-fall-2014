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

def listPossibleNames():
	print text

def findNames():
	readText("test.txt")
	listPossibleNames()
	print "This is test 1:"

if __name___="__main__":
	findNames()