import re


def find_names(string):
    pattern = re.compile("[A-Z][a-z]+ (?:(?:Mc|O')?[A-Z][a-z]+ )?(?:Mc|O')?[A-Z][a-z]+")
    return re.findall(pattern, string)
