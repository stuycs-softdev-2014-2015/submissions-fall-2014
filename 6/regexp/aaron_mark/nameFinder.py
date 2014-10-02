
import re

reg1 = "(([DMS][ris]{1-3}[\.]? )?(Mr\. )?([A-Z][a-z]*)([\s-][A-Z][a-z]*))"
FL = "([A-Z][a-z]*)([\s-][A-Z][a-z]*)"
reg = "(((Mr\. )|(Mrs\. )|(Dr\. )|(Ms\. )|(Sir\. ){0,1})(([A-Z][a-z]*)([\s-][A-Z][a-z]*)))"
print re.findall(reg,"Mark Norwich hey Dr.  there Mr. Cooper Weaver hi how are Mr. you Sam-Mortenson")

