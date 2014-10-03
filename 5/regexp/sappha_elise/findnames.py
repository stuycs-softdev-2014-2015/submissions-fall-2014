import re

data = open("textnames", 'r')
text = data.read()
data.close()

match_twoNames = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', text)
match_titles = re.findall(r'([A-Z][a-z]+\. [A-Z][a-z]*)', text)
print match_twoNames
print match_titles
