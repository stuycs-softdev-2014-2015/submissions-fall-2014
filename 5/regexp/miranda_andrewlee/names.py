import re
#SET UP DICTIONARY
dictionary= open("words.txt").readlines()
i=0
for x in dictionary:
    dictionary[i]= x.strip("\n")
    i+=1

#OPEN FILE TO BE PROCESSED
f= open("names.txt")
text= f.read().strip("\n");

#REGEX THE FILE
regex= "(([A-Z]\w*|Mr.|Mrs.|Ms.|Dr.)\s([A-Z]\w*\s?)+)"
results = re.findall(regex,text)

#GO THROUGH AND ADD ALL RESULTS IN WHICH BOTH NAMES ARE NOT WORDS TO THE LIST
names=[]
for result in results:
    if result[1].lower().strip(',!?" ') not in dictionary or result[2].lower().strip(',!?" ') not in dictionary :
        if result[0].strip().replace("\n"," ") not in names:
            names.append(result[0].strip().replace("\n"," "))

#CHECK TO SEE IF IT IS THE NAME OF A PLACE
locations=["street","alley","avenue","place","st","ave","manor","house","school","tower","building","road","city","state","nation"]
for name in names:
    for part in name.split(" "):
        if part.lower().strip(',!?"') in locations or "," in part:
            names.remove(name)



print names


    
