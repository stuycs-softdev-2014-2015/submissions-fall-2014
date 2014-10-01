import re

#infilename = "whatever.txt"
#inf = open(infilename)
#instr = inf.read()
#inf.close()

def find_names(string):
    pattern = re.compile("[A-Z][a-z]+ [A-Z][a-z]+")
    return re.findall(pattern,string)

if __name__ == "__main__":
    print(find_names("Bob Jamal desu chin Senpai McKohai"))
