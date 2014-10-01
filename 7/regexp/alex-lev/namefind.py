import re

doc = "President Obama told Jerry that he should write his essay for Ms. Long."


m = re.findall('([A-Z][a-z]* [A-Z][a-z]*)|([A-Z][a-z]*)',doc)
print(m)
