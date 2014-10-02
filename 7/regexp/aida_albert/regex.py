import re

f = open("sherlockholmes.txt")
text = f.read()
f.close()

misses = re.match('Miss [A-Z][a-z]+ [A-Z][a-z]+|Miss [A-Z][a-z]+',text,flags=0)

if __name__=="__main__":
    
    print misses.groups()
