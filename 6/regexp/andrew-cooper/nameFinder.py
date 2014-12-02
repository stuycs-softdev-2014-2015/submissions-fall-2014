import re

################################
###### RegExp Name Finder ######
# Andrew Fischer,Cooper Weaver #
################################

test = open("tomSawyer.txt").read()

names = open("names.txt").readlines()
names = [ name.strip().title() for name in names]
    
def findName(str):
    names = {}
    regexp = "([A-Z][a-z]+)[\s-]([A-Z][a-z]+)"
    ans = re.findall(regexp, str)
    i = 0
    while i < len(ans):
        name = ans[i]
        if not checkName(name[0]):
            ans.remove(name)
        else:
            i += 1

    print ans
    return ans

def checkName(str):
    if str not in names:
        return False
    else:
        return True

findName(test)
