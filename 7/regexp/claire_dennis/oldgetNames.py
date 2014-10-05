import re

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
