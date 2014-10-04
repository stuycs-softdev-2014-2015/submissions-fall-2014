import re

full = open("sherlock.txt", "r").read().split("\n")
first_names = open("all.txt", "r").read().split("\n") # Extract data from firstname database
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

def no_dupe(name_list):
	single = []
	for i in name_list:
		if i not in single:
			single.append(i)
	return single

if __name__ == "__main__":
	names = no_dupe(check_names(get_potential_names(full)))
	print names
	
