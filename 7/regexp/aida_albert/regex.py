import re


f = open("sherlockholmes.txt")
text = f.read().replace("\n"," ")
f.close()

## Finding all 'Misses' in the story, and putting them into a dict with their name as key and frequency as value
misses = re.findall( 'Miss\s[A-Z][a-z]*(?:\s[A-Z][a-z]*)*',text,flags=0 )
misses_dict = {}
for miss in misses:
    if miss in misses_dict:
        misses_dict[miss] += 1
    else:
        misses_dict[miss] = 1

## line = "Cats are smarter than dogs"

## matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

## if matchObj:
##    print "matchObj.group() : ", matchObj.group()
##    print "matchObj.group(1) : ", matchObj.group(1)
##    print "matchObj.group(2) : ", matchObj.group(2)
## else:
##    print "No match!!"


if __name__=="__main__":
    
    print misses_dict

