import re

f = open("doc.txt",'r');
doc = f.read();
f.close();

m = re.findall('(?:[^\.\?] )((?:Mr. )?(?:Ms. )?(?:Mrs. )?[A-Z][a-z]+(?: [A-Z][a-z]+)?)',doc)
print(m)
