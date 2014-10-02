import string
import re
import unittest

stream1 = open("nytimes.txt",'r')
nytimes = stream1.read().replace("\n", " ")
stream1.close()

stream2 = open("firstnames.csv",'r')
read2 = stream2.read().replace("\n"," ")
stream2.close()

def readTimes():
    firstList = [] #will be list of first names that we find in our text files
    firstDic = {} #using dictionary for efficiency
    first = re.findall("[A-Z][a-z]+", nytimes) 
    allNames = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",nytimes)
    firstNames = read2.split() #all first names via our database
    firstDic = dict.fromkeys(firstNames, firstNames)
    #print firstDic
        
    #smith = re.findall("[A-Z][a-z]+\sSmith",nytimes)
    #print allNames
    
    for a in first:
        if a in firstDic:
            firstList.append(a)
    print firstList
    
    for a in first:
        if a in firstDic:
            firstList.append(a)
    #print firstList

            
if __name__ == "__main__":
    readTimes()
