
def codify (s) :
    if len(s) % 2 != 0:
        s = s + "x"
    a = ""
    b = ""
    i = 0
    while i < len(s):
        if i%2 == 0:
            a = a + s[i]
        else: 
            b = b + s[i]
        i = i + 1
    return a + b

def decodify (s) :
    if len(s) % 2 != 0:
        return "this is not a picketfence code"
    a = s[0:len(s)/2]
    b = s[len(s)/2:len(s)]
    i = 0
    c = ""
    while i < len(s)/2:
        c = c + a[i] + b[i]
        i = i + 1
    return c
