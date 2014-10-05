import re

data = open("textnames", 'r')
text = data.read()
data.close()

match_twoNames = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', text)
match_titles = re.findall(r'([A-Z][a-z]+\. [A-Z][a-z]*)', text)

places = ['College', 'University', 'City', 'Library']
##print match_twoNames
##print match_titles

names = []
for name in match_twoNames:
    names.append(name)
for name in match_titles:
    names.append(name)
for name in names:
    first_name = name[:(name.find(' '))]
    last_name = name[(name.find(' ')) + 1:]
    if (name in places) or (first_name in places) or (last_name in places):
        names.remove(name)
print names
