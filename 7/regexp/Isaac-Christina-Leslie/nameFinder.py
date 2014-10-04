import re

full = open("names.txt", "r").readlines()
first_names = open("CSV_Database_of_First_Names.csv", "r").readlines()[0].split("\r") # Extract data from firstname database
first_names = {x:x for x in first_names} # Make a dictionary out of the firstname database 

def get_potential_names(text):
	"""Obtain potential names from a file.
	Just finds words where both the first and second word are capitalized."""
   	names = []
   	exp = "[A-Z]\w+\s[A-Z]\w+"
	for i in text:
		names += re.findall(exp, i)
	return names

def check_names(potential_names):
	"""Checks the potential names against a first name database."""
	checked_names = []
	for i in potential_names:
		first = i.split(" ")[0]
		if first in first_names:
			checked_names.append(i)
	return checked_names

if __name__ == "__main__":
	names = get_potential_names(full)
	checked = check_names(names) 
	print checked
