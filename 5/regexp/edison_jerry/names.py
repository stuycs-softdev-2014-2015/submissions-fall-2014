#!/usr/bin/python
import re

txt = "asdfas asdf asdf Jerry Dai asdf a sfdfs"
txt2 = "Edison Shi"
txt3 = "Mr. Smith"
txt4 = "Mrs. Smith"
txt5 = "New York"

match = re.search( r'[A-Z][\w]*\s[A-Z][\w]*' , txt) 

if match:
    print match.group()
else:
    print "No matches"
