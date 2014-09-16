from flask import Flask, render_template

app = Flask(__name__)

##page: 0=home, 1=countries, 2=players
def homebase(t1len, t2len, page):
    table1=''    
    f=open('data1.txt','r')
    for x in range(17):
        g=f.readline()
    D={}
    i=1
    while g and i<t1len:
        while g=='\n' or g==' \n' or 'Page' in g:
            g=f.readline()
        country=g[:3]
        if country not in D.keys():
            D[country]=int(f.readline())
        else:
            D[country]=D[country]+int(f.readline())
        for x in range(7):
            while g=='\n' or g==' \n' or 'Page' in g:
                g=f.readline()
            g=f.readline()
        i+=1
    n=1
    for y in range(len(D)):
        for x in D.keys():
            if D[x]==max(D.values()):
                table1+='<tr align="center"><td>'+str(n)+'</td><td>'+str(x)+'</td><td>'+str(D[x])+'</td></tr>'
                n+=1
                del D[x]
    f.close()
    if page==1:
         return render_template('countries.html',table=table1)
    table2=''
    a=open('data1.txt','r')
    for x in range(15):
        b=a.readline()
    i=1
    while b and i<t2len:
        b=b.strip('\n')
        if i%7==1:
            table2+='<tr align="center"><td>'+b+'</td>'
        if i%7==2:
            table2+='<td>'+b+'</td>'
        if i%7==3:
            b=a.readline().strip('\n')
            total=int(b)*1.0
        if i%7==4:
            grandslam=int(b)*1.0
        if i%7==5:
            masters=int(b)*1.0
        if i%7==6:
            other=int(b)*1.0
        if i%7==0:
            tourneys=int(b)*1.0
            biggest=max(grandslam,masters,other)
            if grandslam==biggest:
                majority='Grand Slam'
            elif masters==biggest:
                majority='Masters 1000'
            else:
                majority='Other'
            table2+='<td>'+str(total/tourneys)+'</td><td>'+str((grandslam*100)/total)+'</td><td>'+str((masters*100)/total)+'</td><td>'+str((other*100)/total)+'</td><td>'+majority+'</td></tr>'
            
        i+=1
        b=a.readline()
        while b=='\n' or b==' \n' or 'Page' in b:
            b=a.readline()
    a.close()
    if page==2:
        return render_template('players.html',table=table2)
    return render_template('index.html',table1=table1,table2=table2)

@app.route('/')
def home():
    return homebase(15,71,0)

@app.route('/countries')
def countries():
    return homebase(9001,0,1)

@app.route('/players')
def players():
    return homebase(0,9001,2)

if __name__=='__main__':
    app.debug=True
    app.run()
