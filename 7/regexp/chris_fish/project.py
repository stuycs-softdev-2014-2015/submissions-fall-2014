import re

text = open('Test.txt', 'r')
book1 = text.read()
text.close()

def findname():
    m = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', book1)
    print m

if __name__=="__main__":
    findname()
