import re
'''
fname="book.txt"
f = open (fname, "r")
x= f.readlines () 
f.close ()
'''
x = "Cats are smarter than dogs. This is the opinion of Alex."
x = "abcdef"
x = "Mr. Stone found little Amy in Mr. Eric Smith's backyard."
def findname():
    '''
    m= re.search(r".[^ab]+",x) #bcdef
    m= re.search(r"[a-f]+",x) #abcdef
    '''
    m = re.findall(r"[A-Z][a-z\.]+",x)
    
    print m
   




findname()
