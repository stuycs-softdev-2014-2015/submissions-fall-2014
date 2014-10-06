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
place_types = ['Road', 'Square', 'Street', 'Court', 'Avenue', 'Lodge', 'Yard', 'Place', 'Pool', 'Farm'
          'Dockyard', 'Bridge', 'Lane', 'St', 'Valley']
names = re.findall( r"([A-Z][a-z]*) ([A-Z][a-z]*)", text)
places_dict = {}
for string in names:
    if string[1] in place_types:
        place = string[0] + " " + string[1]
        if place in places_dict:
            places_dict[place] += 1
        else:
            places_dict[place] = 1 
    
if __name__=="__main__":
    
    print places_dict

