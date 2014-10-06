
import re

reg = "((([DMS][ris]{1,3}\.? )?([A-Z]([a-z]*|\.)){1}([\s-][A-Z]([a-z]*|\.)){0,1}([\s-][A-Z][a-z]+){1}((,?[\s-][JjSs]r.)|([\s-][XIV]+)){0,1})|([DMS][ris]{1,3}\.?[\s-][A-Z][a-z]*))"


def run(filename):
    file  = open(filename, "r")
    ret = file.read()
    ret = re.findall(reg, ret )
    for x in ret:
        print x[0]

run("words.txt")
