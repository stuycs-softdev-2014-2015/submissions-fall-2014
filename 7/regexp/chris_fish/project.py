import re

text = open('Text.txt', 'r')
book1 = text.readlines()
text.close()

def findname()
    m = re.search('[A-Z][a-z]+ [A-Z][a-z]+', book1)

if __name__=="__main__":
    findname()
