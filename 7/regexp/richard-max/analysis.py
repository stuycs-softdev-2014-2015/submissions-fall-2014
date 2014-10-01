import unittest, re

def find_title_last(text):
    s=  re.findall(r'((Mr|Mrs|Ms|Dr|Miss)\.?\s[A-Z][a-z]+)', text) #//get first match group because match groups suck
    print s
    return s

def validate_title(names,num,test):
    #print names + "\n\n"
    return names[num][0]==test

class names(unittest.TestCase):
    def test_titles(self):
        self.assertEqual(validate_title(find_title_last("Recent studies by Dr. Mandler and Mrs. John show stupid things"),1,"Mrs. John"),True)




if __name__=="__main__":
   unittest.main()
   #pass

