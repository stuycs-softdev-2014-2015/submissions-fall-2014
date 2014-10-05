
import re

reg1 = "(([DMS][ris]{1,3}\.? )?([A-Z][a-z]*)([\s-][A-Z][a-z]*))"


reg = "(([DMS][ris]{1,3}\.? )?((([A-Z][a-z]*)([\s-][A-Z][a-z]*))|([A-Z][a-z]*([\s-]))))"

#ret = re.findall(reg, "Mark Norwich hey Dr. Mark  there Mr. Cooper Weaver hi how are Mr. you Dr. Sam Mortenson")


def run(filename):
    file  = open("filename", "r")
    ret = file.read()
    ret = re.findall(reg, ret )
    for x in ret:
        print x[0]
run("words.txt")
