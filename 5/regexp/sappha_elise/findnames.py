import re
import csv

data = open("aroundworldin80days.txt", 'r')
text = data.read()
data.close()

dict_f = open("dictionary.txt",'r')
dictionary =  dict_f.read()
dict_f.close()

match_twoNames = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', text)
match_titles = re.findall(r'([A-Z][a-z]+\. [A-Z][a-z]*)', text)

places = ['College', 'University', 'Institution', 'City', 'Library','Park','Street','Island','Creek','Railroad','Islands','Territory','Valley','House','River','Mountain','Mountains','Railway','Yard','Fort','Peak','Hotel','Lake', 'Camp', 'Row', 'New', 'Gate']

starting_words = ['But', 'On', 'From', 'Then', 'Down', 'To', 'A', 'An', 'The', 'In', 'Left', 'East', 'West', 'South', 'North', 'Last']
##print match_twoNames
##print match_titles

names = []
names_final= []

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
    to_add = True
    first_name = name[:(name.find(' '))]
    last_name = name[(name.find(' ')) + 1:]
    first_name_l = first_name.lower()
    last_name_l = last_name.lower()        
    if (name in places) or (first_name in places) or (last_name in places):
        #names.remove(name)
        to_add = False
    if (first_name in starting_words):
        to_add = False
    elif first_name not in first_names_list and first_name not in last_names_list and name not in match_titles:
        if first_name_l in dictionary: # first name isnt common and IS in dictionary
            #names.remove(name)
            to_add=False
    elif first_name_l in dictionary and last_name_l in dictionary and (first_name not in first_names_list or last_name not in last_names_list): 
        #names.remove(name)
        to_add = False
    else: 
        if to_add == True and names_final.count(name)<1: 
            names_final.append(name)

#for name in names: 
 #   if names_final.count(name)<1: 
  #      names_final.append(name)
print names_final
