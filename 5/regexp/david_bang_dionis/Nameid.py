import re, sys

def openfile(filename):
    f=open(filename,"r")
    j = f.read()
    f.close()
    return j

def dictionary(filename): #reads in a list of names or places (which will be removed for the name list)
    d= open (filename, "r")
    f = d.read()
    d.close()
    dic= re.findall ("[A-Z]+", f)
    namelist = []
    for i in dic:
        namelist.append( i.lower())
    return namelist

def name(d, dic): #either just a first or last name only, using a dictionary to compare.
    r= re.findall("[A-Z][a-z]*", d)
    namelist = []
    for i in r:
        s = i.lower()
        if s in dic:
            namelist.append(i)
    return namelist

def fullname(d): #first and last name only, will find things like Jr and Sr, but this can also be a last name
    r= re.findall( "[A-Z][a-z]+ [A-Z][a-z]+", d)
    return r

def middlename(d):# first, middle, and last name, will find things like Jr and Sr, but this can also be a last name
    r= re.findall("[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+", d)
    return r

def titles(d): # looks for names with titles such as Sir Mr. Mrs.
    r= re.findall( "[A-Z][a-z][a-z]?\. [A-Z][a-z]+", d)
    return r

def suffix(d): #finds names with a suffix such as Jr. Sr.
    r= re.findall( "[A-Z][a-z]+\s[A-Z][a-z]+\sJr|Sr", d)
    return r

def capstypo (d, dic): # if name happens to have more than 1 capital letter due to a typo or a strange mix of cap and lower case letters
    r= re.findall("[A-Z]+[a-z]*", d)
    namelist = []
    for i in r:
        s = i.lower()
        if s in dic:
            namelist.append(i)
    return namelist
    

def allnames(d): #will find multiple variations of the same name, for example Mr.Smith will be found as Mr. Simon  and Simon. To limit the search, get rid of specific methods, for example to get rid of all 3 length names, get rid of the middlename call
    dic = dictionary("namelist.txt")
    return fullname(d)+titles(d) + name(d, dic) + middlename(d) + suffix (d) + capstypo (d, dic)


for i in allnames(openfile("test.txt")):
    print i


if __name__ == "__main__":

    var = raw_input("\n\nPlease enter which type of name format you want to find\n1.first and last name\n2.names with titles\n3.first name or last name only(takes a long time on long texts)\n4.first,last and middle name\n5.Name with suffix\n6.All types of names (will get multiple printouts of the same name in different variations):\n")
    print ("you entered", var)
    if (var not in "123456"):
        print "enter a valid number"
    if (var in "123456"):
        var2 = raw_input("\nInput name of text document(sample would be test.txt, book.txt is also in this directory) you want to scan through:\n")
    try:
        if (var == "1"):
            for i in fullname(openfile(var2)):
                print i
        if (var == "2"):
            for i in titles(openfile(var2)):
                print i
        if (var == "3"):
            dic = dictionary("namelist.txt")
            for i in name(openfile(var2),dic):
                print i
        if (var == "4"):
            for i in middlename(openfile(var2)):
                print i
        if (var == "5"):
            for i in suffix(openfile(var2)):
                print i
        if (var == "6"):
            for i in allnames(openfile(var2)):
                print i
    except:
        print ("Not a valid file in the directory")




