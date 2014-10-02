import re

f = open("sherlockholmes.txt")
text = f.read()
f.close()

names = re.findall('[A-Z][a-z]+ [A-Z][a-z]+',text,flags=0)

if __name__=="__main__":
    print len(names)
    print names[156]
