import re

fi = open("nick.txt","r")
content = fi.read()
fi.close()

#Start at 16484
fi2 = open("/usr/share/dict/words", "r")
dictionary = fi2.read()
words=dictionary.split("\n")
words=words[16484:]
fi2.close()


for i in range(len(words)):
    words[i]=words[i].upper()

firstPass = re.findall("[A-Z][A-Za-z'\-]*\s[A-Z][A-Za-z'\-]*", content)
fTitles = re.findall("(Mr|Mrs|Miss|Ms|Hon|Dr|Sir|Hon|Fr|Esq|King)(\.)?\s{0,1}([A-Z][A-Za-z'\-]*)?(\s[A-Z][A-Za-z'\-]*)?", content)

titles = []
for word in fTitles:
    fin = ""
    """if word[1] == '':
        word[1] = ' '"""
    #print word
    for part in word:
        fin += part
    #if word[2] != '' and word[3] != '':
    titles.append(fin)
    #else:
    #    titles.remove(word)
    #print word

firstPass.extend(titles)
secondPass = []
for word in firstPass:
    if "--" in word:
        names=re.findall("[\w]+",word)
    else:
        names=word.split(" ")
    check=True
    for name in names:
        if name.upper() in words:
            check=False
    if check:
        secondPass.append(word)


thirdPass = list(set(secondPass))

for word in thirdPass:
    print word + "\n"
    #pass

