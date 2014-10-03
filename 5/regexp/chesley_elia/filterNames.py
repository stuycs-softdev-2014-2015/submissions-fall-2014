# We will use regexes to find surnames that are patronymic or toponymic 
# i.e. de Waal, or el-Fattah  
import time
import re
inputList = []
inputFile = "pg47010.txt"
nameList = []
namesListFile = "allNamesUppercase.txt"
results = set()

#def filterDirectMatches():
#    prefixes = ["Mr.", "Ms.", "Miss", "Mister", "Dr."]
#    suffixes = ["Phd", "Jr", "Sr", "MD"]

    
def getFilteredInputList():
    global wordList, inputList, results
    f = open(inputFile, 'r')
    #regex_split_delimiter = "\s+|-{2,}|,|\!|\?|\"|\'s|s\'"
    #regex_capital_words_chain = "(?!\s)((([A-Z][a-z]+) )+)"
    regex_capitals_with_surname_epithet = "(?!\s)([A-Z][a-z]+(( [A-Z][a-z]+)*)?(( ([a-z]{2,3}(?=\s))){1,2}( [A-Z][a-z]+)+)?)"
    regex = re.compile(regex_capitals_with_surname_epithet)
    words = regex.findall(f.read())
    for _tuple in words:
        if len(_tuple) > 0:
            word = _tuple[0]
            word = word.replace('\r', ' ')\
                    .replace('\n', ' ')
            word = word.strip()
            if word.find(' ') < 0:
                if (inNameList(word)):
                    #print "Matched: " + word
                    results.add(word)
            else:
                each_part_is_valid_name = True
                valid_parts = []
                for part in word.split(" "):
                    if (not inNameList(part)):
                        each_part_is_valid_name = False
                    else:
                        if len(part) > 0 and part[0].isupper():
                            valid_parts.append(part)
                if each_part_is_valid_name:
                    #print "Matched multiword: " + word
                    results.add(word)
                else:
                    for valid_part in valid_parts:
                        #print "Matched substring: " + valid_part;
                        results.add(valid_part)
    f.close()

def getNameList():
    startTime = time.time() * 1000
    global namesListFile, nameList
    f = open(namesListFile, 'r')
    for line in f.readlines():
        nameList.append(line.strip())
    f.close()
    print "Read all names (" + str(len(nameList)) + ") in " + str(time.time() * 1000 - startTime) + " ms"
    startTime = time.time() * 1000
    # Name list should be pre-sorted, but this is run just in case
    # If it is pre-sorted, the runtime of this sort will be negligible 
    nameList.sort()
    print "Sorted all names in " + str(time.time() * 1000 - startTime) + " ms" 

def inNameList(word):
    global nameList
    word = word.upper()
    low = 0
    high = len(nameList) - 1
    while (low <= high):
        middle = (low + high) / 2
        if (word > nameList[middle]):
            low = middle + 1;
        elif (word < nameList[middle]):
            high = middle - 1;
        else:
            return True
    return False

def removeDuplicates(a_list, target):
    return [value for value in a_list if value != target]

if __name__ == "__main__":
    getNameList()
    getFilteredInputList()
    print "\n==============================START=============================="
    print results
    print "==============================END=============================="


