import re

text_file = open("NameList", "r")
raw_text = text_file.read()
text_file.close()
spaceless_text = raw_text.split();

#this is the list of names to be checked with
name_list = [x for x in spaceless_text if not x[0].isdigit()]

#Takes a file name and returns a dictionary of names that are found in name_list and their frquencies
def search_for_names(filename):
    
    read_text = open(filename, "r")
    read_raw = read_text.read()
    read_text.close()

    #find all strings that start with a capital letter and end with lowercase letters
    capped_words = re.findall("[A-Z][a-z]+", read_raw)
    matched_names = [x for x in capped_words if x in name_list]

    #names found and their frequencies
    found_names= {}
    for x in matched_names:
        if x in found_names:
            found_names[x]+= 1
        else:
            found_names[x] = 1
    
    return found_names

print search_for_names("text.txt")               

