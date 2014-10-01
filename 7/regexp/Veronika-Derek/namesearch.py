import re

file = open("janeausten.txt", "r")
text = file.read()
file.close()

names = []
with open("names_list.txt") as f:
    for line in f:
        names.append(line.split()[0].capitalize())
file.close()

#test prints
#print(text[:100])
#print names[:10]

search = "Jane Austen"
print re.findall(search,  text)
