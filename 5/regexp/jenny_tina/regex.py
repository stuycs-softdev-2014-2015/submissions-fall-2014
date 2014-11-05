import re

f = open('text.txt', 'r')
#f = open('text2.txt', 'r')
rawtext = f.read() #test is a string
f.close()

rawtext = rawtext.replace("\xe2\x80\x9d", '\"');
rawtext = rawtext.replace("\xe2\x80\x99s", "\'");

words = rawtext.split()
pairs = []

i = 1
while i < len(words):
    new = words[i-1] + " " +  words[i]
    pairs.append(new.strip(",!?.;:\"\'"))
    i = i + 1

reg = re.compile('[A-Z]([a-z|\-|\'])+ [A-Z]([a-z|\-|\'])+')
names = []

#error once the '#' is removed
#Doesn't always work
nonNames = ["Dear", "College", "University", "Street", "Avenue", "Boulevard", "School", "City", "He ", "His ", "She ", "Her ", "The ", "And ", "But", "This "]#, "So ", "Yet "]

j = 0
while j < len(pairs):
    if ( reg.match(pairs[j]) != None and pairs[j] not in names):
            names.append(pairs[j])
    j = j + 1

k = 0
while k < len(names):
    for each in nonNames:
        if names[k].find(each) > -1:
    #if (names[k].find("Dear") > -1 or names[k].find("College") > -1
        #or names[k].find("University") > -1 or names[k].find("Street") > -1
        #or names[k].find("Avenue") > -1 or names[k].find("Boulevarrd") > -1
        #or names[k].find("School") > -1 or names[k].find("City") > -1
        #or names[k].find("He ") > -1 or names[k].find("His ") > -1
        #or names[k].find("She ") > -1 or names[k].find("Her ") > -1
        #or names[k].find("The ") > -1 or names[k].find("And ") > -1
        #or names[k].find("But ") > -1 ):
            names.pop(k)
    k = k + 1


print names
