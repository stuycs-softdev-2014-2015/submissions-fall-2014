import re
name=[]
def dictionary(filename):
    temp=open("resources/"+filename,"r")
    global name
    for i in temp.readlines():
        name+=[i.strip("\n")]
    temp.close()
fname="None"
def fullname(d):
    r= re.findall( "[A-Z][a-z]+ [A-Z][a-z]+", d)
    return namefilter(check(r),0)
def titles(d):
    r= re.findall( "[A-Z][a-z][a-z]?\. [A-Z][a-z]+", d)
    return namefilter(check(r),1)
def partname(d):
    r= re.findall("[A-Z][a-z]*", d)
    return namefilter(check(r),0)
def middlename(d):
    r= re.findall("[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+", d)
    return namefilter(check(r),0)
def suffix(d):
    r= re.findall( "[A-Z][a-z]+\s[A-Z][a-z]+\sJr|Sr", d)
    return namefilter(check(r),0)
def allnames(d):
    return fullname(d)+titles(d)+partname(d)+middlename(d)+suffix(d)
def check(d):
    temp=[]
    clone=False
    for i in d:
        for a in temp:
            if(i == a):
                clone=True
        if(not clone):
            temp+=[i]
        clone=False
    return temp
def namefilter(d,index):
    temp=[]
    for i in d:
        for a in name:
            if(i.split(" ")[index].lower()==(a.lower())):
                temp+=[i]
                break
    return temp
#    def names(d,filename):
#    r=namefilter(fullname(d))+titles(d)
#    f=open((filename+"(result).txt"),"w")
#    for i in r:
#        print(i)
#        f.write(i+"\n")
#    f.close()
if __name__ == "__main__":

    var = raw_input("\n\nPlease enter which type of name format you want to find\n1.first and last name\n2.names with titles\n3.first name or last name only(takes a long time on long texts)\n4.first,last and middle name\n5.Name with suffix\n6.All types of names (will get multiple printouts of the same name in different variations):\n")
    print ("you entered", var)
    if (var not in "123456"):
        print "enter a valid number"
    if (var in "123456"):
        var2 = raw_input("\nInput name of text document(sample would be test.txt, book.txt is also in this directory) you want to scan through:\n")
        var3= raw_input("common(c) or uncommon(u) names (uncommon may cause words to come up)\n")
        if(var3=="c"):
            dictionary("lite.txt")
        elif(var3=="u"):
            dictionary("names.txt")
        else:
            print "invalid input"
    try:
        f=open(var2,"r")
        d=f.read()
        f.close()
    except:
        print ("Not a valid file in the directory")
    print("\nStarted finding names in "+var2+"!\n")
    if (var == "1"):
        for i in fullname(d):
            print i
    if (var == "2"):
        for i in titles(d):
            print i
    if (var == "3"):
        for i in partname(d):
            print i
    if (var == "4"):
        for i in middlename(d):
            print i
    if (var == "5"):
        for i in suffix(d):
            print i
    if (var == "6"):
        for i in allnames(d):
            print i
    print("\nFinished finding names in "+var2+"!\n\n")
