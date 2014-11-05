import re


def find_names(string):
    pattern = re.compile("(?:(?:M(?:r|s|rs).?|The) )?(?!The|M(?:r|s|rs).?)[A-Z][a-z]+ (?:(?:Mc|O')?[A-Z][a-z]+)+")
    return re.findall(pattern, string)
