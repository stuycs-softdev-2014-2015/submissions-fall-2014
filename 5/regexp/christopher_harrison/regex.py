import re

def extract_names_regex(string):
    result = []
    re_caps = re.compile('^[A-Z][a-z]+.$')
    for word in string.split():
        if re_caps.match(word):
            result.append(word)
            print word
    return result

def extract_names_list(string):
    '''Matches each word against a list of names, and includes the word if it is found.'''
    pass

def extract_names_words(string):
    '''Matches each word against a list of words, and includes the word if it is NOT found.'''
    pass


f = open("test_files/secret_service.txt")
extract_names(f.read())
