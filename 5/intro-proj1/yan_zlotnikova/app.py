from flask import Flask,render_template

app = Flask(__name__)

images=["static/img/chick.jpeg",
        "static/img/cow.jpg",
        "static/img/milk.gif",
        "static/img/pig.jpg",
        "static/img/sheep.jpg",
        "static/img/turkey.jpg",
    ]

@app.route("/")
def home():   
    import random
    num = random.randrange(0,4)
    f = open("templates/home.html",'r') 
    tableNeeded = True
    for line in f.readlines():
        if ("Hawaii" in line):
            tableNeeded = False
    if (tableNeeded): 
        f.close()
        f = open("templates/home.html",'a')
        f.write(table())
        f.close()
    return render_template("home.html", 
                           img = images[num])


def table():
    data=report()
    result_list=[]
    #L=s.split("\n")
    #for item in L:
        #if item=='<data>':
    rank=range(1,51,1)
    for info in data:
        x='<td><center>'+str(rank[0])+'</center></td>'+'\n'+'<td><center>'+ info[0]+ '</center></td>'+'<td><center>'+str(info[1])+ '</center></td>'+"\n"+'<td><center>'+str(info[2])+ '</center></td>'+"\n"+'<td><center>'+ str(info[3])+ '</center></td>'+"\n"+'<td><center>'+ str(info[4])+ '</center></td>'+"\n"+'<td><center>'+ str(info[5])+ '</center></td>'+"\n"+'<td><center>'+ str(info[6])+ '</center></td>'+"\n"+'<td><center>'+ str(info[7])+ '</center></td><tr>'
        result_list.append(x)
        rank.remove(rank[0])
    result="\n".join(result_list)
    result=result+ "\n" + "<tr>" + "\n" +  "</table>" + "\n" + "</div>" + "\n" + "</body>"
    return result


def open_data(filename):
    L=[]
    for item in open(filename).readlines():
        L.append(item.strip().split(","))
    return L

def healthiest_state(filename):
    healthy=[]
    book={}
    book2={}
    book2r={}
    L=[]
    D=[]
    h=[]
    x=[]
    y=[]
    for item in open(filename).readlines():
        L.append(item.strip().split(","))
    for a in L:
        D.append(float(a[1]))
    for b in L:
        h.append(b[2])
    for item in h:
        if float(item)<0:
            x.append(float(item))
        elif float(item)>=0:
            y.append(float(item))
    x.sort()
    y.sort()        
    x.reverse()
    y.reverse()
    h=y+x
    D.sort()
#from decreasing health (so increasing death)
    for s in L:
        book[s[0]]=[h.index(float(s[2])),D.index(float(s[1]))]
    for k in book.keys():
        book2[k]=sum(book[k])
    book2['Georgia']=81.8
    book2['Utah']=9.9
    book2['South Carolina']=81.9
    book2['North Dakota']=27.9
    book2['Connecticut']=18.9
    book2['Wisconsin']=26.9
    book2['Rhode Island']=27.8
    book2['Delaware']=58.9
    book2['Wyoming']=61.9
    book2['Ohio']=62.9
    for k in book2.keys():
        book2r[book2[k]]=k
    value=[]
    for v in book2.values():
        value.append(v)
    value.sort()
    for item in value:
        healthy.append(book2r[item])
    return healthy

def redvswhite(filename):
#state,beef,milk,other,hogs,sheep,total (of the red meats),hen,broilers,turkeys,other,total(of pooultry),other animals
    L=[]
    d={}
    for item in open(filename).readlines():
        L.append(item.strip().split(","))
    for s in L:
        for item in s:
            if len(s)>=12:
                try:
                    d[s[0]]=[float(int(s[6])),float(int(s[11]))]
                except:
                    d[s[0]]=[s[6], s[11]]
    return d

def percentred(fname):
    data = redvswhite(fname)
    percent = 0
    dict = {}
    d = {}
    for key in data.keys():
        if key == 'Tennessee':
            dict[key] = [0.0,0.0]
        elif data[key][0] == ' ' and data[key][1] == ' ':
            dict[key] = [0.0,0.0]
        elif data[key][0] == ' ' or data[key][0] == '':
            dict[key] = [0.0,data[key][1]]
        elif data[key][1] == ' ' or data[key][1] == '':
            dict[key] = [data[key][0],0.0]
        else:
            value = data[key]
            dict[key] = value
        if (int(dict[key][0]) + int(dict[key][1])) == 0:
            percent = 0
        else:
            percent = float(dict[key][0])/(int(dict[key][0]) + int(dict[key][1])) * 100
        d[key] = percent
    return d


def percentwhite(fname):
    data = redvswhite(fname)
    percent = 0
    dict = {}
    d = {}
    for key in data.keys():
        if key == 'Tennessee':
            dict[key] = [0.0,0.0]
        elif data[key][0] == ' ' and data[key][1] == ' ':
            dict[key] = [0.0,0.0]
        elif data[key][0] == ' ' or data[key][0] == '':
            dict[key] = [0.0,data[key][1]]
        elif data[key][1] == ' ' or data[key][1] == '':
            dict[key] = [data[key][0],0.0]
        else:
            value = data[key]
            dict[key] = value
        if (int(dict[key][0]) + int(dict[key][1])) == 0:
            percent = 0
        else:
            percent = float(dict[key][1])/(int(dict[key][0]) + int(dict[key][1])) * 100
        d[key] = percent
    return d


#State,Beef,Cows,2007,Rank,Milk,Cows,2007,Rank,Beef,Cows/Sqm,Farm
def organicvsreg(filename):
    d={}
    L=[]
    data=open_data('US_certified_organic_livestock_08.csv')
    a=[]
    for x in data:
        a.append(x[1])
    for item in open(filename).readlines():
        L.append(item.strip().split(","))
    for s in L:
        if a[0]!=' ':
            d[s[0]]=[float(a[0]), float(s[1]), (float(a[0])/(float(a[0])+float(s[1])))*100]
        else: 
            d[s[0]]=[a[0], s[1], ' ']
        a=a[1:] 
    return d

def report():
    healthiest=healthiest_state('state_deathper100,000_health.csv')
    rw=redvswhite('US_certified_organic_livestock_08.csv')
    org=organicvsreg('cattleps.csv')
    pr=percentred('US_certified_organic_livestock_08.csv')
    pw=percentwhite('US_certified_organic_livestock_08.csv')
    r=[]
    for s in healthiest:
        r.append([s])
    for item in r:
        item.append(rw[item[0]][0])
        item.append(rw[item[0]][1])
        item.append(org[item[0]][0])
        item.append(org[item[0]][1])
        item.append(org[item[0]][2])
        item.append(pr[item[0]])
        item.append(pw[item[0]])
    return r

     

if __name__=="__main__":
    app.debug=True
    app.run()
    ##app.run(host="0.0.0.0",port=8000)
