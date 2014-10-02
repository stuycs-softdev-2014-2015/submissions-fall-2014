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
    f = open('data.txt', 'r')
    data = ''
    for x in f:
        data += x
    f.close()
    captures = [x[0] for x in first_last(data)]
#    first_last(data)
    #print data
    print captures
