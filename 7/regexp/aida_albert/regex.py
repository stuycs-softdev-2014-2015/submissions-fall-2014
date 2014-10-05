import re


f = open("sherlockholmes.txt")
text = f.read().replace("\n"," ")
f.close()
## Finding all names
## names = re.findall( '[A-Z][a-z]*\s[A-Z][a-z]*(?:\s[A-Z][a-z]*)*', text, flags = 0 )
## Finding all 'Misses' in the story
misses = re.findall( 'Miss\s[A-Z][a-z]*(?:\s[A-Z][a-z]*)*',text,flags=0 )
misses_dict = {}
for miss in misses:
    if miss in misses_dict:
        misses_dict[miss] += 1
    else:
        misses_dict[miss] = 1
## Finding all 'Sirs' in the story 
sirs = re.findall( 'Sir\s[A-Z][a-z]*(?:\s[A-Z][a-z]*)*', text, flags=0 )
sirs_dict = {}
for sir in sirs:
    if sir in sirs_dict:
        sirs_dict[sir] += 1
    else:
        sirs_dict[sir] = 1

## Finding locations in the story (roads, avenues, etc.)
if __name__=="__main__":
    
    print sirs_dict

