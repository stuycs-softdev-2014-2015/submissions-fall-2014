#!/usr/bin/python
import re

txt = open("book.txt", "r")
txt = txt.read()

match = re.findall( r'[A-Z][a-z]* [A-Z][a-z]* | Mrs?. [A-Z][a-z]* | Dr. [A-Z][a-z]*' , txt)


if match:
    print match
else:
    print "No matches"
