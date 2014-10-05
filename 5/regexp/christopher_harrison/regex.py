import re

def extract_names(string):
    '''Takes a string and returns a list of all names in the string.'''
    names = []
    for word in string.split():
        word = letters_only(word)
        if is_name(word):
            names.append(word)
    return names

def letters_only(string):
    '''Takes a string and returns a new string comprising all the letters of the old string.'''
    result = []
    for char in string:
        if re_letter.match(char):
            result.append(char)
    return "".join(result)

def is_name(string):
    '''Takes a string and returns True if the string is a name; and false otherwise.'''
    return ( (re_caps.match(string)) and
             ( (string.upper() in d_names) or
               not (string.upper() in d_words)))

def fill(dicti, filename):
    for word in open(filename).read().split():
        dicti[word] = 0
    return dicti

#----------------------------------------------------------------

d_words = {}
fill(d_words, "words.txt")
d_names = {}
fill(d_names, "names.txt")

re_letter = re.compile("([a-z])|([A-Z])")
re_caps = re.compile('^[A-Z][a-z]+.$')

def test(filename):
    f_read = open("test_files/" + filename + ".txt", "r")
    f_write = open("test_results/" + filename + ".nam", "w")
    f_write.write( "\n".join(extract_names( f_read.read() )))
    f_read.close()
    f_write.close()

test("secret_service")
