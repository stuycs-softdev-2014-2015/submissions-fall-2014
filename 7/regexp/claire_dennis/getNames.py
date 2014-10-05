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

        #checks if the currentWord is a first name.
        if (currentWord.upper() in firstnamesMaster):

            #adds that first name to our list of first names in the text.
            firstnamesInText.append(currentWord)

            #regular expression that includes this first name plus any capitalized
            #names after it (gets the full name, if there is one). 
            regex = "(" +  currentWord + "((\s[A-Z][a-z]+)+)" + ")"

            #this part isolates the longest version of the full name that is found, in three steps..
            step1 = (re.findall(regex,text,flags=0))
            print "Step 1:"
            print step1
            if step1:
                step2 = step1.pop()
                print "Step 2:"
                print step2
                step3 = step2[0]
                print "Step 3:"
                print step3
                if (step3 not in fullnamesInText):
                    fullnamesInText.append(step3)
                    
                
        i+=1


    

getNames("This is just a test. Dennis is just testing code that Claire wrote. John Smith is a full name. But John is not. Neither is Smith. Alan Frederick Dehddgga, on the other hand, is a full name.")

print firstnamesInText
print fullnamesInText



        
