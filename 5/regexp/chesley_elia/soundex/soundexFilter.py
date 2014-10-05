import time
import re
inputList = []
inputFile = "pg2147.txt"
nameList = []
soundex_nameList = []
#namesListFile = "allNamesUppercase.txt"
namesListFile = "yob2013.txt"
results = set()


def freqMatcher():
	f = open(inputFile, 'r')
	words = []
	for word in f:
		word = word.split('\n')
		word = word[0]
		word = word.split(' ')
		words = words+word
		
	#print words
	if len(words) < 5000:
		print None
	print 'STARTING'
	for word in words:
		word1 = " ".join(re.findall("[a-zA-Z]+", word))
		word1 = word1.split(" ")
		for sww in word1:
			if isName_soundex(sww):
				print sww
	
	print 'DONE'


def isName_soundex(poss_nam):
	global soundex_nameList
	soundex_poss_name = convert_soundex(poss_nam)
	if len(soundex_poss_name) < 4:
		return False
	#print soundex_poss_name
	if soundex_poss_name in soundex_nameList:
		return True
	return False

def convert_namelist_to_soundex():
	global nameList, soundex_nameList
	for nam in nameList:
		soundex_nam = convert_soundex(nam)
		if not (soundex_nam in soundex_nameList):
			soundex_nameList.append(soundex_nam)
	#print soundex_nameList

def convert_soundex(word):
	if len(word) < 6:
		return ''
		
	word = word.lower()
	#print word
	#print word
	f = word[0]
	rem = word[1:]
	p1 = re.compile('b|f|p|v')
	p2 = re.compile('c|g|j|k|q|s|x|z')
	p3 = re.compile('d|t')
	p4 = re.compile('l')
	p5 = re.compile('m|n')
	p6 = re.compile('r')
	code = []
	for lt in rem:
		if not not p1.findall(lt):
			code.append('1')
		elif not not p2.findall(lt):
			code.append('2')
		elif not not p3.findall(lt):
			code.append('3')
		elif not not p4.findall(lt):
			code.append('4')
		elif not not p5.findall(lt):
			code.append('5')
		elif not not p6.findall(lt):
			code.append('6')
	
	if len(code) > 3:
		code = code[0:3]
	if len(code) < 3:
		code = code +['0']*(3-len(code))
	
	code = ''.join([f]+code)
	return code

def getNameList():
    global namesListFile, nameList
	
    startTime = time.time() * 1000
    f = open(namesListFile, 'r')
    for line in f.readlines():
		line = line.split(',')
		line = line[0]
		line = line.lower()
		nameList.append(line)
    f.close()
    print "Read all names (" + str(len(nameList)) + ") in " + str(time.time() * 1000 - startTime) + " ms"
    startTime = time.time() * 1000
    # Name list should be pre-sorted, but this is run just in case
    # If it is pre-sorted, the runtime of this sort will be negligible 
    nameList.sort()
    #print nameList
    print "Sorted all names in " + str(time.time() * 1000 - startTime) + " ms" 
	
# getNameList()
# convert_namelist_to_soundex()
# print isName_soundex('Alannah')
# print isName_soundex('Elizabeth')
# print isName_soundex('Jacqueline')
# print isName_soundex('Isabella')
# print isName_soundex('Hypervitaminosis')
# print isName_soundex('Gedankenexperiment')
# print isName_soundex('Triskaidekaphobia')

getNameList()
convert_namelist_to_soundex()
freqMatcher()	