from flask import Flask, render_template, request

app = Flask(__name__)

##page: 0=home, 1=countries, 2=players
def homebase(t1len, t2len, page, s):
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
    rank = 0
    players = {}
    curplayer = ''
    while b and i<t2len:
        b=b.strip('\n')
        if i%7==1:
            rank=b
            table2+='<tr align="center"><td>'+b+'</td>'
        if i%7==2:
            if b[-1]==' ':
                b = b[:-1]
            curplayer=b
            L = []
            L.append(rank) ##pl[0]
            players[curplayer]=L
            table2+='<td>'+b+'</td>'
        if i%7==3:
            b=a.readline().strip('\n')
            total=int(b)*1.0
            players[curplayer].append(total) ##pl[1]
        if i%7==4:
            grandslam=int(b)*1.0
            players[curplayer].append(grandslam) ##pl[2]
        if i%7==5:
            masters=int(b)*1.0
            players[curplayer].append(masters) ##pl[3]
        if i%7==6:
            other=int(b)*1.0
            players[curplayer].append(other) ##pl[4]
        if i%7==0:
            tourneys=int(b)*1.0
            players[curplayer].append(tourneys) ##pl[5]
            biggest=max(grandslam,masters,other)
            if grandslam==biggest:
                majority='Grand Slam'
            elif masters==biggest:
                majority='Masters 1000'
            else:
                majority='Other'
            players[curplayer].append(majority) ##pl[6]
            table2+='<td>'+str(total/tourneys)+'</td><td>'+str((grandslam*100)/total)+'</td><td>'+str((masters*100)/total)+'</td><td>'+str((other*100)/total)+'</td><td>'+majority+'</td></tr>'
            
        i+=1
        b=a.readline()
        while b=='\n' or b==' \n' or 'Page' in b:
            b=a.readline()
    a.close()
    if page==2:
        if s=='': ##no search
            return render_template('players.html',table=table2)
        else:
            resultL=[]
            for name in players.keys():
                if s in name:
                    print name
                    resultL.append(name)
            result=''
            resultL.sort(key=lambda name: (players[name])[1], reverse=True)        
            for name in resultL:
                pl = players[name]
                print pl
                result+= '<tr align="center"><td>'+pl[0]+' </td>'
                result+='<td>'+name+'</td>'
                result+='<td>'+`pl[1]/pl[5]`+'</td>'
                result+='<td>'+`pl[2]*100/pl[1]`+'</td>'
                result+='<td>'+`pl[3]*100/pl[1]`+'</td>'
                result+='<td>'+`pl[4]*100/pl[1]`+'</td>'
                result+='<td>'+majority+'</td></tr>'
            return render_template('players.html',table=result)
    return render_template('index.html',table1=table1,table2=table2)

@app.route('/')
def home():
    return homebase(15,71,0,'')

@app.route('/countries')
def countries():
    return homebase(9001,0,1,'')

@app.route('/players',methods=["GET","POST"])
def players():
    if request.method=='GET':
        return homebase(0,900001,2,'')
    else:
        search = request.form['search']
        return homebase(0,900001,2,search)

    
if __name__=='__main__':
    app.debug=True
    app.run()
