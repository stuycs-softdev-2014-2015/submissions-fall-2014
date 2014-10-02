import re

def extract_names(string):
    result = []
    re_caps = re.compile('[A-Z][a-z]+')
    for word in string.split():
        if re_caps.match(word):
            result.append(word)
            print word
    return result
        
f = open("test/secret_service/secret_service.txt")
extract_names(f.read())
