import pickle

def makedict():
    s= "!ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    words = []
    for n in s:
        t = open("dict/" + n + " Words.csv")
        r = t.readlines()
        for i in xrange(len(r)-1):
            r[i] = r[i][:-1]
            r[i] = r[i].lower()
        words.extend(r)
        
        t.close()
    
    return words



wr = open('diction.txt', 'wb')
d= makedict()
pickle.dump(d,wr)
wr.close()
