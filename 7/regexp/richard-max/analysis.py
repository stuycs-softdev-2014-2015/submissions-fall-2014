import unittest, re, math



sl = 'abcdefghijklmnopqrstuvwxyz'


d = open('words.txt').readlines()
datad = [x.rstrip() for x in d]
dd={}
for x in sl:
    dd[x]=0
for x in datad:
    for y in x:
        if y in dd:
            dd[y]+=1

#print datad
for x in sl:
    dd[x]=dd[x]*100.0/484585
#for x in xrange(len(dd)):
#    print list(dd.viewkeys())[x] + " " + str(list(dd.viewvalues())[x])



nm = open('males.txt').readlines()
datam = [x.rstrip().lower() for x in nm]
dm={}
for x in sl:
    dm[x]=0
for x in datam:
    for y in x:
        dm[y]+=1
for x in sl:
    dm[x]=dm[x]*100.0/569
#for x in xrange(len(dm)):
    #print list(dm.viewkeys())[x] + " " + str(list(dm.viewvalues())[x])
nf = open('females.txt').readlines()
dataf = [x.rstrip().lower() for x in nf]
df={}
for x in sl:
    df[x]=0
for x in dataf:
    for y in x:
        df[y]+=1
for x in sl:
    df[x]=df[x]*100.0/596
#for x in xrange(len(df)):
    #print list(df.viewkeys())[x] + " " + str(list(df.viewvalues())[x])


def vectorize(l):
    return math.sqrt(sum(l))



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

def word_filter(text):
    #filtered = [x for x in text if (x.split()[0] not in datad or x.split()[1] not in datad)] #may take a while.
    filtered = []
    for x in text:
        y = x.split()
        for q in xrange(0,2):
            if y[q] not in datam and y[q] not in dataf:
                if y[q] not in datad:
                    filtered.append(y)
            else:
                filtered.append(y)
    return filtered

def name_vector_filter(text):
    data = {}
    
    result = []
    for t in text:
        t = t.lower()
        for x in sl:
            data[x]=0
        for x in t:
            if x in data:
                data[x]+=1
        for x in sl:
            data[x]=data[x]*100.0/len(t)
        #add not to the statement below to see what was removed
        if ((vectorize([ abs(data[x]-dd[x]) for x in sl]) > vectorize([abs(data[x] - df[x]) for x in sl])) or (vectorize([ abs(data[x]-dd[x]) for x in sl]) > vectorize([abs(data[x] - dm[x]) for x in sl]))):
            if "the " not in t:
                result.append(t)
    return word_filter(list(set(result)))


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
    
    
            
    #f = open('muricans.txt', 'r')
    f = open('data.txt','r')
    data = ''
    for x in f:
        data += x
    f.close()
    captures = [x[0] for x in first_last(data)]
    print (name_vector_filter(captures))
    #print captures
    """#On the spot testing
    while (True):
        ans = raw_input(">")
        print name_vector_filter([ans])
    """
    
