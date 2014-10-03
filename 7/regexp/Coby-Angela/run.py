import string
import re
import unittest

stream1 = open("nytimes.txt",'r')
nytimes = stream1.read().replace("\n", " ")
stream1.close()

#stream to read our first names file
stream2 = open("firstnames.csv",'r')
read2 = stream2.read().replace("\n"," ")
stream2.close()

#stream to read surnames file
stream3 = open("surnames.csv",'r')
read3 = stream3.read().replace("\n"," ")
stream3.close()

def readTimes():
    firstList = [] #will be list of first names that we find in our text files
    firstDic = {} #using dictionary for efficiency => constant runtime for finding?
    names = re.findall("[A-Z][a-z]+", nytimes)
    
    fullNames = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",nytimes)
    firstNames = read2.split() #all first names via our database
    firstDic = dict.fromkeys(firstNames, firstNames)
    
    #smith = re.findall("[A-Z][a-z]+\sSmith",nytimes)
    for a in names:
        if a in firstDic:
            firstList.append(a)
    print firstList
    #####################################

    surnameList = []
    surnameDic = {}
    surnames = read3.split()
    for a in surnames:
        surnameDic[a.title()] = a.title()

    for a in names:
        if a in surnameDic:
            surnameList.append(a)
    print surnameList
    
    
            
if __name__ == "__main__":
    readTimes()
