import re

data = open("textnames", 'r')
text = data.read()
data.close()

matchNames = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', text)
print matchNames