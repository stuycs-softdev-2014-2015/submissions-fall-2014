def getNames(text):
    import re

    firstname_file = open("firstnames.csv")
    firstname_text = firstname_file.read()
    firstname_file.close()

    firstnamesMaster = re.findall('[A-Z][A-Z]+',firstname_text,flags=0)

    lastname_file = open("lastnames.csv")
    lastname_text = lastname_file.read()
    lastname_file.close()

    lastnamesMaster = re.findall('[A-Z][A-Z]+',lastname_text,flags=0)

    textList = text.split()
    numfirstnames = 0
    numlastnames = 0
    numfullnames = 0

    firstnamesInText = []
    lastnamesInText = []
    fullnamesInText = []
    
    for num in range(0, len(textList)):
        currentWord = textList[num]
        end = num == len(textList) - 1
        if end != True: 
            nextWord = textList[num + 1]
        print currentWord
        if ((currentWord.upper() in firstnamesMaster) and (end != True) and (nextWord[0:1].isupper()) and ((currentWord + " " + nextWord) not in fullnamesInText)):
            fullnamesInText.append(currentWord + " " + nextWord)
            numfullnames += 1
            if (currentWord not in firstnamesInText):
                firstnamesInText.append(currentWord)
                numfirstnames += 1
            if (nextWord not in lastnamesInText):
                lastnamesInText.append(nextWord)
                numlastnames += 1
            num += 1
        elif ((currentWord.upper() in firstnamesMaster) and (currentWord not in firstnamesInText)):
            firstnamesInText.append(currentWord)
            numfirstnames += 1     
        elif ((currentWord.upper() in lastnamesMaster) and (currentWord not in lastnamesInText)):
            #print "last name" + x.upper()
            lastnamesInText.append(currentWord)
            numlastnames += 1
    print firstnamesInText
    print lastnamesInText
    print fullnamesInText

    for num in range(0, len(textList)):
        currentWord = textList[num]
        end = num == len(textList)-1
        if end != True:
            nextWord = textList[num+1]
            if ((currentWord.upper() in firstnamesMaster) and (nextWord[0:1].isupper()) and ((currentWord + " " + nextWord) not in fullnamesInText)):
                fullnamesInText.append(currentWord + " " + nextWord)
                numfullnames += 1
                if (currentWord not in firstnamesInText):
                firstnamesInText.append(currentWord)
                numfirstnames += 1
            if (nextWord not in lastnamesInText):
                lastnamesInText.append(nextWord)
                numlastnames += 1
            num += 1

    

getNames("This is just a test. Dennis is just testing code that Claire wrote. John Smith is a full name. But John is not. Neither is Smith. Alan Dehddgga, on the other hand, is a full name.")



        
