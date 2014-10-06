import re

corpus = open('corpus.txt','r')
temp = corpus.read()
corpus_text = temp.replace('\n',' ')
corpus.close()

english = open('words.txt','r')
words = english.read()
english.close()

#corpus_text = "Mr. Michael Zamansky. This is a sentence, Eric." 
# Put the real corpus_text string here from the file later.
# Currently just a placeholder.

match_names = re.findall(r"((?!A|The|a|the)([A-Z][a-z]*. )?[A-Z][a-z]*(( (von )?(van )?(del )?(de la)?(de los )?(de las )?(d')?(Mc)?(Mac)?[A-Z][a-z]*))?)", corpus_text)

names = []

for name in match_names:
    item = name[0]
    l = item.split(" ")
    isEnglish = False
    isShort = False
    #print l
    for word in l:
        s = "\n"+word.lower()+"\n"
        if s in words:
            #print words.find(s)
            isEnglish = True
            #if (not isEnglish):
            #print isEnglish
    isShort = True
    if len(item) > 1:
        isShort = False
    if ((not isEnglish) and (not isShort)):
    #if (not isEnglish):
        names.append(item)

print names
