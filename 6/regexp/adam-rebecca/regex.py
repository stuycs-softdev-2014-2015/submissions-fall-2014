#!/usr/bin/python
import re

text = open("doctor_who_wiki.txt", "r")
test = text.read()
text.close()

match = re.findall( r'[A-Z][a-z]* [A-Z][a-z]*|Mrs?. [A-Z][a-z]*|Dr. [A-Z][a-z]*' , test)

print match
