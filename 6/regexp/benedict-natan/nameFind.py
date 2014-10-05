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

secondPass = []
for word in firstPass:
	names=re.findall("[\w]+",word)
	#names=word.split(" ")
	check=True
	for name in names:
		if name.upper() in words:
			check=False
	if check:
		secondPass.append(word)

thirdPass = list(set(secondPass))

for word in thirdPass:
    print word + "\n"
