import re


f = open("sherlockholmes.txt")
text = f.read().replace("\n"," ")
f.close()

## Finding all names
names = re.findall( '[A-Z][a-z]*\s(?:\s[A-Z][a-z]*)*', text, flags = 0 )
## Finding all 'Misses' in the story
misses = re.findall( 'Miss\s[A-Z][a-z]*(?:\s[A-Z][a-z]*)*',text,flags=0 )
misses_dict = {}
for miss in misses:
    if miss in misses_dict:
        misses_dict[miss] += 1
    else:
        misses_dict[miss] = 1
        
leading_lady=""
for miss in misses_dict:
    if leading_lady == "" or misses_dict[miss] > misses_dict[leading_lady]:
        leading_lady  = miss
        
## Finding all 'Sirs' in the story 
sirs = re.findall( 'Sir\s[A-Z][a-z]*(?:\s[A-Z][a-z]*)*', text, flags=0 )
sirs_dict = {}
for sir in sirs:
    if sir in sirs_dict:
        sirs_dict[sir] += 1
    else:
        sirs_dict[sir] = 1

for sir in sirs_dict:
    if leading_man == "" or sirs_dict[sir] > sirs_dict[leading_man]:
        leading_man = sir
        
## Finding locations in the story (roads, avenues, etc.)
place_types = ['Road', 'Square', 'Street', 'Court', 'Avenue', 'Lodge', 'Yard', 'Place', 'Pool', 'Farm'
          'Dockyard', 'Bridge', 'Lane', 'St', 'Valley']
possible_places = re.finditer( r"([A-Z][a-z]*) (?P<place_type>[A-Z][a-z]*)", text)
places_dict = {}
for place in possible_places:
    if place.group('place_type') in place_types:
        if place.group(0) in places_dict:
            places_dict[place.group(0)] += 1
        else:
            places_dict[place.group(0)] = 1
leading_place = ""
for place in places_dict:
    if leading_place == "" or places_dict[place] > places_dict[leading_place]:
        leading_place = place

## Finding other Titles
if __name__=="__main__":
     
    print "The main man: " + leading_man
    print "The main dame: " + leading_lady
    print "Where it all goes down: " + leading_place


