
import re

p = re.compile("(([A-Z][a-z]*)[\s-])([A-Z][a-z]*)")
print p.findall("Mark Norwich hey there Cooper Weaver hi how are you Sam Mortinson")

