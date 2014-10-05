import re

mytext = "These are a bunch of names: Claire Burghard is a name Will Cameron Burghard is also a name  Virginia Woolf is once again a name  Cecilia Marie Janie Evans is a long name and my parents names are Chuck and Laurie"
firstnames = ["Claire","Will","Virginia","Cecilia","Chuck","Laurie"]
lastnames = []
middlenames = []
fullnames = []

def get_names(text):
    textList = text.split();
    for num in range(0, len(textList)-1):
        currentWord = textList[num]
        print currentWord
        end = num ==len(textList)-1
        if end != True:
            if currentWord in firstnames:
                regex = currentWord + "(\s[A-Z][a-z]+)*"
                fullnames.append(re.findall(regex,text,flags=0))

get_names(mytext)
print fullnames
    
