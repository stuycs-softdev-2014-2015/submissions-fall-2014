import re

def fill(dicti, filename):
    for word in open(filename).read().split():
        dicti[word] = 0
    return dicti

d_words = {}
fill(d_words, "words.txt")

d_names = {}
fill(d_names, "names.txt")

def extract_names_regex(string):
    result = []
    re_caps = re.compile('^[A-Z][a-z]+.$')
    for word in string.split():
        if re_caps.match(word):
            result.append(word)
    return result

def extract_names_names(string, d_names):
    '''Matches each word against a list of names, and includes the word if it is found.'''
    result = []
    for word in string.split():
        print word
        if word in d_names:
            result.append(word)
    return result
        

def extract_names_words(string, d_words):
    '''Matches each word against a list of words, and includes the word if it is NOT found.'''
    result = []
    for word in string.split():
        if not(word in d_words):
            result.append(word)
    return result

def test(filename):
    f_read = open("test_files/" + filename + ".txt", "r")
    f_write_regex = open("test_results/" + filename + "_regex", "w")
    f_write_names = open("test_results/" + filename + "_names", "w")
    f_write_words = open("test_results/" + filename + "_words", "w")

    f_write_regex.write(str(extract_names_regex(f_read.read())))
    f_write_names.write(str(extract_names_names(f_read.read(), d_names)))
    f_write_words.write(str(extract_names_words(f_read.read(), d_words)))

test("secret_service")
