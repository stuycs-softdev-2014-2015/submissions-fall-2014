import re

firstname_file = open("firstnames.csv")
firstname_text = firstname_file.read()
firstname_file.close()

firstnamesMaster = re.findall('[A-Z][A-Z]+',firstname_text,flags=0)

lastname_file = open("lastnames.csv")
lastname_text = lastname_file.read()
lastname_file.close()

lastnamesMaster = re.findall('[A-Z][A-Z]+',lastname_text,flags=0)

numfirstnames = 0
numlastnames = 0
numfullnames = 0

firstnamesInText = []
lastnamesInText = []
fullnamesInText = []
    
def getNames(text):

    #split the text into a list of words.
    textList = text.split()

    #The variable i will keep our place.
    i = 0

    while (i < len(textList)):
        currentWord = textList[i]
        if (currentWord.upper() in firstnamesMaster):
            firstnamesInText.append(currentWord)
            regex = currentWord + "((\s[A-Z][a-z]+)*)"
            fullnamesInText.append(re.findall(regex,text,flags=0)) 
        i+=1


    

getNames("This is just a test. Dennis is just testing code that Claire wrote. John Smith is a full name. But John is not. Neither is Smith. Alan Frederick Dehddgga, on the other hand, is a full name.")

print firstnamesInText
print fullnamesInText



        
