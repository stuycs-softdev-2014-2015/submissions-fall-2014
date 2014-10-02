import re

f = open("this_has_text.txt")
s = f.read()
f.close()

f = open("name_list.csv")
name_list_raw = f.read()
f.close()

f = open("address_abbreviations.txt")
address_abbreviations = f.read()
f.close()

name_list = []
name_list_raw = name_list_raw.split("\n")
for name in name_list_raw[1:]:
	name = name.split(",")
	name_list.append(name[0])
del name_list[len(name_list) - 1]

names = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+", s)
titled_names = re.findall("(Mr|Ms|Mrs|Dr|Drs|Sir|Madam)?[A-Z][a-z]+\s[A-Z][a-z]+", s)

i = 0
while (i < len(names)):
	#print names[i]
	#(names[i].split(" ")[0].upper() not in name_list)
	first_name = names[i].split(" ")[0]
	last_name = names[i].split(" ")[1]
	if ((last_name.upper() in address_abbreviations) or ((last_name.upper() not in name_list))):
		#print names[i]
		del names[i]
		i -= 1
	i += 1

#titles = ["Mister", "Miss", "Mr", "Mrs", "Ms", "Mr.", "Mrs.", "Ms."]

print names
