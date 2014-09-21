inf = open("winrate.txt")

stats = ["No.","Name","Win Rate","Matches","Wins","Losses"]

table = [stats]

datalist = []
for ln in inf.readlines():
    cleanln=ln.strip()
    if len(cleanln):
        cleanln=cleanln.replace(",","")
        if cleanln.find(" \t")>0:
            nameline = cleanln.split(" \t")
            datalist.append(nameline[0])
            datalist.append(nameline[1])
        else:
            datalist.append(cleanln)
        
inf.close()

#print datalist

n = 1
currow = []
for item in datalist:
    currow.append(item)
    if n%6==0:
        table.append(currow)
        currow = []
    n+=1

for row in table:
    print row

outstr = ""
for row in table:
    for item in row:
        outstr += item + ","
    outstr = outstr[:-1] + "\n"

outf = open("winrate.csv","w")
outf.write(outstr)
outf.close
