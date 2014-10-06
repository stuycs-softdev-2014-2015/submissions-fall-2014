import re

_file = open("text.txt", "r")
text = _file.read()

regex = re.compile("((?:Mr\.\s)?[A-Z][a-z]+[ ]?(?:[A-Z][a-z]+)?)[\s!\?]")
print regex.findall(text)
