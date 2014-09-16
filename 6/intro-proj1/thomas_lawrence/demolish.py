inf = open("1.csv")

stats = ["Image","Name"]

inf.readline()
for i in range(18):
    stats.append(inf.readline().strip("\t\n"))

table = [stats]

for ln in inf.readlines():
    cur = ln.strip().split("\t")
    clean = []
    for item in cur:
        clean.append(item.strip())
    table.append(clean)

inf.close()

fixtable = []
for rownum in range(len(table)):
    currow = table[rownum]
    fixrow = currow[0].split(" ",1) + currow[1:]
    fixtable.append(fixrow)



#print stats
print fixtable
for row in fixtable:
    #print len(row)
    pass

outstr = ""
for row in fixtable:
    for item in row:
        outstr += item + ","
    outstr = outstr[:-1] + "\n"

outf = open("out.csv","w")
outf.write(outstr)
outf.close
