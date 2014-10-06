import re
import csv

data = open("textnames", 'r')
text = data.read()
data.close()

match_twoNames = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', text)
match_titles = re.findall(r'([A-Z][a-z]+\. [A-Z][a-z]*)', text)

places = ['College', 'University', 'City', 'Library','Park']
##print match_twoNames
##print match_titles

names = []

csv_first = csv.reader(open("firstnames.csv","rU"),dialect=csv.excel_tab)
#first_names_file = open("firstnames.csv")
#csv_first = csv.reader(first_names_file) 

csv_last = csv.reader(open("lastnames.csv","rU"),dialect=csv.excel_tab)
#last_names_file = open("lastnames.csv")
#csv_last = csv.reader(last_names_file)

first_names_list = []
last_names_list = []
all_names_list = []

for row in csv_first: 
    first_names_list.append(row[0])
for row in csv_last: 
    last_names_list.append(row[0])

all_names_list = first_names_list + last_names_list


for name in match_twoNames:
    names.append(name)
for name in match_titles:
    names.append(name)
for name in names:
    first_name = name[:(name.find(' '))]
    last_name = name[(name.find(' ')) + 1:]
    if (name in places) or (first_name in places) or (last_name in places):
        names.remove(name)
    if first_name not in first_names_list and first_name not in last_names_list and name not in match_titles: 
        if last_name not in first_names_list and last_name not in last_names_list: 
            names.remove(name)
    elif ((first_name not in first_names_list and first_name not in last_names_list) or (last_name not in first_names_list and last_name not in last_names_list)):
        names.remove(name)

print names
