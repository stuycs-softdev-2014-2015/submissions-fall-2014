#Victor and Lise's name search
#Returns dictionary of names based on a file with common first names
#There are some glitches as some of the listed first names may not be a name of a person in context
#
import re

def opentestfile(fname):
    f = open (fname, "r")
    x= f.read() 
    f.close ()
    return x
def firstname(string):
    s = string.split(" ")
    return s[0]
def midname(string):
    s = string.split(" ")
    return s[1]
def lastname(string):
    s = string.split(" ")
    return s[-1]

names= opentestfile("names.csv");
names= names.split()
#other files from the class
fname = "Test.txt" #chris_fish
#slight errors with oddly formatted txt
fname = "sample.txt" #Ling_BrianG
####################
fname = "testfile.txt"
fname="JackWinters.txt"

x = opentestfile(fname)
#test string (not a complete sentence....)
#x = "\"Zane said New York married Alaska and had a child country named Indonesia whose child was Australia... but Johnny Aaron Deep's was loved by Emily J. Jenkino and Mary's cat but not Jane Terrance but he is also loved by James! "
#print x
def findname():
    #matches all capitalized letters
    matches = re.findall("[A-Z][a-z]+",x)

    #matches  ('firstname', 'lastname')
    flmatches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)[\s]([A-Z][a-z]+[-]?[A-Z]?[a-z]+)[']?[s]?[\s][a-z]+",x)
    #matches with middle initials ('firstname','MI','lastname')
    mimatches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)[\s]([A-Z][\.])[\s]([A-Z][a-z]+[-]?[A-Z]?[a-z]+)[']?[s]?",x)    
    #matches with middle name
    midmatches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)[\s]([A-Z][a-z]+)[\s]([A-Z][a-z]+[-]?[A-Z]?[a-z]+)[']?[s]?",x)
    
    #matches = re.findall("[\s][a-z]+[\s]([A-Z][a-z|-]+[A-Z]?[a-z]+)[!\.,;\?][\s]",x) #gets all single capitalized words before a punctuation mark and a space -> but doesnt get words preceded by quotess

   
    FLmatches =[]
    for name in flmatches:
        if name[0] in names:
            FLmatches.append(name[0]+" " + name[1])
    print FLmatches
    MImatches = []
    for name in mimatches:
        if name[0] in names:
            MImatches.append(name[0] + " " + name[1] +" "+name[2])
    print MImatches
    MIDmatches = []
    for name in midmatches:
        if name[0] in names:
            MIDmatches.append(name[0] + " " + name[1] +" "+name[2])
    print MIDmatches
    numbnames={}
    '''
    adds all names in matches that match the first name list
    however there some lastnames that could count as the firstname-> this is solved in the dictmatches function
    '''
    for name in matches:
        if name in names:
            if name in numbnames:
                numbnames[name]+=1
            else:
                numbnames[name]=1


    allmatches = [FLmatches,MImatches,MIDmatches]
    for listm in allmatches:
        dictmatches(listm,numbnames)
    return numbnames   
   
#adds elements in list to dict while balancing dict so eliminated repeated names from the dictionary
def dictmatches(L,D):
    for name in L:
        if name in D:
            D[name] +=1
        else:
            D[name] = 1
        firstn = firstname(name)
        #checks to see if firstname of the name inputted is already in the dictionary; if so, subtracts it from the dictionary (b/c there would be one extra name included in the dictionary)
        if firstn in D:  
            D[firstn] -= 1
            if D[firstn] ==0:
                del D[firstn]
        
        try:
            #checks to see if lastname is a valid firstname but already in the dictionary; if so, subtracts it from the dictionary(b/c there would be one extra name included in the dictionary)
            lastn = lastname(name)
            if lastn in D and lastn in names:  
                 D[lastn] -= 1
                 if D[lastn] ==0:
                     del D[lastn]
            break
        except:
            try:
                #checks to see if middlename is a valid firstname but already in the dictionary; if so, subtracts it from the dictionary (b/c there would be one extra name included in the dictionary)
                midn = midname(name)
                if midn in D and midn in names:  
                    D[midn] -= 1
                    if D[midn] ==0:
                        del D[midn]
                break
            except:
                return D
    return D
    


#in dictionary form
print findname()

#prints names as list
#print findname().keys()

