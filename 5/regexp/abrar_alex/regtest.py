import re

f1 = open ("test.txt", "r")
f2 = open ("names", "r")
f3 = open ("words", "r")
s = f1.read()
names = f2.readlines();
words = f3.readlines();
#print s
f1.close()
f2.close()

#s2 = re.findall('[A-Z][a-z]+\.?\s[A-Z][a-z]+\.?\s' , s)
s2 = re.findall('[A-Z][a-z]+\s[A-Z][a-z]+' , s)
for name in s2:
    for commonName in names:
        if "'" not in commonName:
            firstName = name.split(" ")[0]
            if firstName == commonName.strip("\n"):
                print name
                break;
    if firstName == "Mr." or firstName == "Mrs." or firstName == "Ms.":
        print name
    else :
        isWord = False;
        for word in words:
            if firstName.lower() == word.strip("\n") or name.split(" ")[1] == word.strip("\n"):
                isWord = True;
        if not isWord:
            print name
