import re
#To finish read file of common names, put them in a list then print only the names if they are also on list. 


def analyzing_cube(text_file):
	fi= open(text_file,'r')	
	a = fi.read()
	m = re.findall(r"[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+",a)
	print m
	
if __name__ == "__main__":
	the_file = raw_input("What is the file you want to read?:")
	analyzing_cube(the_file)