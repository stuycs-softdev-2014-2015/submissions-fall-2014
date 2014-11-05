import re

with open ("PrideandPrej.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

s = "I am Andreas Wang and my partner is Ms. Quispe. CAPITAL THINGS DO NOT DESTROY US. Mr. Charles Dickens should show some class when looting the City of Troy.Unfortunately we do not provide support for Bartolome de las Casas."

f = "((([A-Z][a-z]+)|M([rs]|rs)\.)( [A-Z][a-z]+)+)"

res = re.findall(f, data)
L = []
for k in res:
    L.append(k[0])
print L

