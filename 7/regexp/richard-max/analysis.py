import unittest, re

def find_title_last(text):
    s=  re.findall(r'((Mr|Mrs|Ms|Dr|Miss)\.?\s[A-Z][a-z]+)', text) #//get first match group because match groups suck
    #print s
    return s

def first_last(text):
    s = re.findall(r'([A-Z]\w+\s([A-Z]\.?)?\s?[A-Z]\w+)', text)
    return s

def last_possessive(text):
    s = re.findall(r'[A-Z]\w+\'s', text)
    return s

def last_first(text):
    s = re.findall(r'[A-Z]\w+,\s[A-Z]\w+', text)
    return s

def name_vector_filter(text):
    data = []
    
    
    
    print data
def validate_title(names,num,test):
    #print names + "\n\n"
    return names[num][0]==test

def validate_first_last(names,num,test):
    return names[num][0]==test

def validate_last_first(names,num, test):
    return names[num] == test

def validate_last_possessive(names,num, test):
    return names[num] == test

class names(unittest.TestCase):
    def test_titles(self):
        self.assertEqual(validate_title(find_title_last("Recent studies by Dr. Tom and Mrs. John show stupid things"),1,"Mrs. John"),True)

    def test_first_last(self):
        self.assertEqual(validate_first_last(first_last("Johnathon Kim, Lester D. Lester, Mary Smith are going to the shopping mall."),0,"Johnathon Kim"),True)

    def test_last_first(self):
        self.assertEqual(validate_last_first(last_first("Commander: Bradley, Omar"), 0, "Bradley, Omar"), True)

    def test_possessive(self):
        self.assertEqual(validate_last_possessive(last_possessive("Richard's richard"),0,  "Richard's"), True)

    




        
if __name__=="__main__":
    #unittest.main()
    #So I compared the vectors of the dictionary and the list of male names
    #, and they are practically identical, so I cannot use a vector to distinguish
    # English words from English names. Oh well.
    """
    s = 'abcdefghijklmnopqrstuvwxyz'
    import math


    d = open('words.txt').readlines()
    datad = [x.rstrip() for x in d]
    dd={}
    for x in s:
        dd[x]=0
    for x in datad:
        for y in x:
            if y in dd:
                dd[y]+=1
    for x in xrange(len(dd)):
        print list(dd.viewkeys())[x] + " " + str(list(dd.viewvalues())[x])
    vector = math.sqrt(sum([x*x for x in dd.viewvalues()]))
    print vector/851.643234

    
    nm = open('males.txt').readlines()
    datam = [x.rstrip().lower() for x in nm]
    dm={}
    for x in s:
        dm[x]=0
    for x in datam:
        for y in x:
            dm[y]+=1
    for x in xrange(len(dm)):
        print list(dm.viewkeys())[x] + " " + str(list(dm.viewvalues())[x])
    vector = math.sqrt(sum([x*x for x in dm.viewvalues()]))
    print vector#569
            
    nf = open('females.txt').readlines()
    dataf = [x.rstrip().lower() for x in nf]
    df={}
    for x in s:
        df[x]=0
    for x in dataf:
        for y in x:
            df[y]+=1

    """
            
    f = open('data.txt', 'r')
    data = ''
    for x in f:
        data += x
    f.close()
    captures = [x[0] for x in first_last(data)]
    print captures
