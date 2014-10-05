import re
re.M

#Mr Ms Mrs Dr Jr Sr Prof Sir Lady Lord 


search = "(([A-Z][a-z]*|Mr.|Mrs.|Ms.|Dr.|Lady|Lord|Professor|Prof.)\s([A-Z][a-z]*\s?)+)"

#prepping the book
x = open("Elizabeth.txt", "r")
splitBook = x.read().split()
book = " ".join(splitBook) #fixes weird book formatting


#prepping the name/notName list
y = open("names.txt", "r")
names = y.read().replace("\t", "").split("\n")
z = open("notNames.txt", "r")
notName = y.read().replace("\t", "").split("\n")
x.close()
y.close()
z.close()


#find names
List = re.findall(search, book)

#remove for things that arent names
BookNamesInitial = []
for x in List:
    for word in x:
        if word in names:
            BookNamesInitial.append(x[0])

#removing thing that arent names part 2
for name in BookNamesInitial:
    if name in notName:
        BookNamesInitial.remove(name)
    

#removing repeats
BookNames = []
for x in BookNamesInitial:
    if x.strip() not in BookNames:
        BookNames.append(x.strip())


print BookNames
            
        
        


