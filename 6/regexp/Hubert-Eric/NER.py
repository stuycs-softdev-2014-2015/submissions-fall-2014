import re, timeit, enchant

d = enchant.Dict("en_us")

def findNames(text):
    pattern = "[^The]((([A-Z][a-z]+)|M([rs]|rs)\.|Dr\.)((\s[A-Z]\.)?\s[A-Z][a-z]+-?[A-Z]?[a-z]+)+)"
    result = [name[0] for name in re.findall(pattern, text)]
    if len(text) < 4000:
        return set(result)
    else:
        return set([name for name in result if not inDict(name)])

def inDict(name):
    parts = name.split(' ')
    for part in parts:
        if not d.check(part):
            return False
    return True

if __name__ == '__main__':
    f = raw_input("File name (+location if not in same directory): ")
    tlq = open(f, 'r').read()
    print("\nResults from input file:\n " + str(findNames(tlq)) + "\n\n")

    test = """Hello John Smith,
That's a very typical name. Can I filter out Dr. Brown? How about Mrs. Floyd. How about Dr. Bowman-brown. How about this Version:
Mr. Bowman-Hal. Heywood R. Floyd works as well!!! Finally. This is a SPmannnenea NAmenmaneme, that probably won't be filtered out.
Some more stuff.
    Sincerely, Dave Bowman"""

    print("This is the default test:\n " +  str(findNames(test)))



