import re

def rmdup(L):
    newL = L
    i=0
    while i<len(newL):
        while(newL.count(L[i]) >= 2):
            newL.remove(L[i])
        i+=1
    return newL

def run(s):
    f = open(s, 'r')
    book = f.read()
    f.close()

    a = re.findall(r"([A-Z][a-zA-Z'-]+) ([A-Z][a-zA-Z'-]+)?", book)
    a1 = [i[0] for i in a]
    a2 = [i[1] for i in a]
    b = re.findall(r"[A-Z][a-zA-Z'-]+", book)
    c = re.findall(r"\. ([A-Z][a-zA-Z'-]+)", book)
    d = re.findall(r"(Mr|Mrs|Ms|Miss)\. ([A-Z][a-z]+)", book)
    d = [i[1] for i in d]
    
    i = 0
    while i < len(b):
        if b[i] in c: #or b[i].lower() in dic: //Only check dic for words after periods
            b.remove(b[i])
        else:
            i=i+1

    i = 0

    while i < len(c):
        if c[i].lower() in dic:
            c.remove(c[i])
        else:
            i=i+1

    ans = b + c

    while i < len(a):
        if a1[i] in ans and a2[i] in ans and len(a2[i]) > 0:
            ans = [x for x in ans if (x != a1[i] and x != a2[i])]
            i=i+1
        else:
            a.remove(a[i])

    newa = [x[0] + " " + x[1] for x in a]
    ans = ans + newa
    ans = ans + d
    
    return rmdup(ans)


f = open("wordsEn.txt", 'r')
dic = f.read().split("\n")
f.close()

print(run("nytimes.txt"))
print(run("Dreamy Hollow.txt"))
