import re

one = open('huckleberryfin.txt', 'r')
book1 = one.readlines()
one.close()

def findname():
    #first/last name only - look for captialized words then exclude any that are not normal starts of sentences
    
    #first and last
    m = re.search('[A-Z][a-z]+ [A-Z][a-z]+', book1)
    
    #labels before/after - look for sir/brother/king/something before or after name
    


if __name__=="__main__":
    findname()
