from flask import Flask,render_template, request
#<center>And how many words? <input type="text" name="topwords" size="5" value="50"><br>


app = Flask(__name__)




@app.route("/")
def test():
    return "hello world"

@app.route("/start")
def start():
    return render_template("constitutionoptions.html")


@app.route("/results", methods = ["POST", "GET"])
def main():

    if request.method == 'POST':
<<<<<<< HEAD
        elements = request.form["Submit"]
        
        #return elements;
        
       
        
=======
        elements = request.form.getlist("Yes")


        return elements
>>>>>>> FETCH_HEAD



        s = "";

        checked=0
        Dict={'one':[],'two':[]}
        #return "Succcess"
<<<<<<< HEAD
        
=======

>>>>>>> FETCH_HEAD
        one=1
        two=2
        if 'Iran' in elements:
            Dict['one'].append('Iranian constitution')
            a=open('Iran.txt')
            iran=a.read()
            iran=iran.lower()
            iran=iran.split()
            Dict['one'].append(iran)

            checked+=1
        if 'USA' in elements:
            b=open('unitedstates.txt')
            usaw=b.read()
            usaw=usaw.lower()
            usaw=usaw.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("USA's constitution")
                Dict['one'].append(usaw)
            else:
                Dict['two'].append("USA's constitution")
                Dict['two'].append(usaw)
<<<<<<< HEAD
       
        if '1791' in elements:
=======

        if elements.has_key('seventeen'):
>>>>>>> FETCH_HEAD
            c=open('1791France.txt')
            revolution=c.read()
            revolution=revolution.lower()
            revolution=revolution.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("French constitution of 1791")
                Dict['one'].append(revolution)
            else:
                Dict['two'].append("French constitution of 1791")
                Dict['two'].append(revolution)
<<<<<<< HEAD
            
        if 'Russia' in elements:
=======

        if elements.has_key('Russia'):
>>>>>>> FETCH_HEAD
            d=open('russia.txt')
            rus=d.read()
            rus=rus.lower()
            rus=rus.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("Russian Federation' constitution")
                Dict['one'].append(rus)
            else:
                Dict['two'].append("Russian Federation' constitution")
                Dict['two'].append(rus)
<<<<<<< HEAD
        
        if 'USSR' in elements:
=======

        if elements.has_key('ussr'):
>>>>>>> FETCH_HEAD
            e=open('USSR.txt')
            ussr=e.read()
            ussr=ussr.lower()
            ussr=ussr.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("Union of Soviet Socialist Republic's constitution")
                Dict['one'].append(ussr)
            else:
                Dict['two'].append("Union of Soviet Socialist Republic's constitution")
                Dict['two'].append(ussr)
<<<<<<< HEAD
        
        if 'France' in elements:
=======

        if elements.has_key('france'):
>>>>>>> FETCH_HEAD
            f=open('France.txt')
            france=f.read()
            france=france.lower()
            france=france.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("French constitution")
                Dict['one'].append(france)
            else:
                Dict['two'].append("French constitution")
                Dict['two'].append(france)
<<<<<<< HEAD
            
        if 'Manifesto' in elements:
=======

        if elements.has_key('manifesto'):
>>>>>>> FETCH_HEAD
            g=open('manifesto.txt')
            manifesto=g.read()
            manifesto=manifesto.lower()
            manifesto=manifesto.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("Communist Manifesto")
                Dict['one'].append(manifesto)
            else:
                Dict['two'].append("Communist Manifesto")
                Dict['two'].append(manifesto)
<<<<<<< HEAD
            
        if 'Magna' in elements:
=======

        if elements.has_key('magna'):
>>>>>>> FETCH_HEAD
            h=open('Magnacarta.txt')
            magna=h.read()
            magna=magna.lower()
            magna=magna.split()
            checked+=1
            if Dict['one']==[]:
                Dict['one'].append("Magna Carta")
                Dict['one'].append(magna)
            else:
                Dict['two'].append("Magna Carta")
                Dict['two'].append(magna)
        checker=0
        if checked!=2:
            s+= '<br><center><font size="10"> <b> I said two gosh darn it!<br> </b> <font size="7"> <a href="constitutionoptions.html">Go back</a>'
            return s
        #10
        s+= '<br><center> You have chosen to compare the '+Dict['one'][0]+' with the '+Dict['two'][0]
        if True: #elements.has_key('yestopwords'):
            checker+=1
            s+=  '<br><br><b><font size="5">Top ' + '50' +' Words</font><br><br>' #elements['topwords'].value
            s+= Dict['one'][0]+':</b><br>'
            s+= top50(Dict['one'][1],50)
            s+= '<br><br><b>'+Dict['two'][0]+':</b><br>'
            s+= top50(Dict['two'][1],50)
        if True: #elements.has_key('total'):
            checker+=1
            s+= '<br> <br><b><font size="5">Total Words</font></b><br><br>'
            s+= Dict['one'][0]+': '+str(len(Dict['one'][1])) +'<br>'
            s+= Dict['two'][0]+': '+str(len(Dict['two'][1]))
        uniqueone=[]
        uniquetwo=[]
        for x in Dict['one'][1]:
            if x not in uniqueone:
                uniqueone.append(x)
        for x in Dict['two'][1]:
            if x not in uniquetwo:
                uniquetwo.append(x)
        if True: #elements.has_key('unique'):
            checker+=1
            s+= '<br> <br><b><font size="5">Total Unique Words</font></b><br><br>'
            s+= Dict['one'][0]+': '+str(len(uniqueone)) +'<br>'
            s+= Dict['two'][0]+': '+str(len(uniquetwo))
        if True: #elements.has_key('percentage'):
            checker+=1
            s+= '<br> <br><b><font size="5">Percentage of Unique Words</font></b><br><br>'
            s+= Dict['one'][0]+': '+str(float(len(uniqueone))/len(Dict['one'][1])*100) +'%<br>'
            s+= Dict['two'][0]+': '+str(float(len(uniquetwo))/len(Dict['two'][1])*100) +'%'
        if True: #elements.has_key('common'):
            checker+=1
            s+= '<br> <br><b><font size="5">All Common Words</font></b><br><br>'
            new=[]
            for x in uniqueone:
                if x in uniquetwo:
                    new.append(x)
            s+= 'There are '+ str(len(new))+" common words and they are:<br>"
            r=0
            new.sort()

            for word in new:
                s+= word+'  '
                r+=1
                if r==6:
                    s+= '<br>'

                    r=0
        if True: #elements.has_key('letters'):
            checker+=1
            s+= '<br> <br><b><font size="5">Total number of letters</font></b><br><br>'
            s+= Dict['one'][0]+': '
            s+= str(letters(Dict['one']))
            s+= "<br>"+ Dict['two'][0]+": "
            s+= str(letters(Dict['two']))
        if True: #elements.has_key('wordlength'):
            checker+=1
            s+= '<br> <br><b><font size="5">Average word length</font></b><br><br>'
            s+= Dict['one'][0]+': '
            s+= str(letters(Dict['one']))
            s+= "<br>"+ Dict['two'][0]+": "
<<<<<<< HEAD
            s+= str(letters(Dict['two']))   
=======
            s+= letters(Dict['two'])
>>>>>>> FETCH_HEAD
        if checker==0:
            s+= '<br><br><br><font size="5"> <b> But you forgot to check off actions to take!</b>'
            s+= '<br>  <a href="constitutionoptions.html">Go back!</a>'
            return s

        s+= '<br><br> <br> <b> Resources</b><br> All constitutions taken from <a href="http://www.constitution.org/cons/natlcons.htm">here</a>'
        s+= '<br> manifesto taken from <a href="http://www.gutenberg.org/ebooks/61"> here</a>'
        s+= '<br> French constitution of 1791 taken from <a href="http://ic.ucsc.edu/~traugott/hist171/readings/1791-09ConstitutionOf1791"> here</a>'
        s+= '<br> and Magna Carta taken from <a href="http://www.constitution.org/eng/magnacar.htm"> here</a>'
        return s
<<<<<<< HEAD
    #'''
=======

>>>>>>> FETCH_HEAD
def top50(filen,number):

    s = ""
    cm=filen
    d={}
    x=0

    while x<len(cm):
        cm[x]=cm[x].strip(".,?[]!();:-")
        x+=1

    for x in cm:
        if x in d:
            d[x]+=1
        else:
            d[x]=1

    x=sorted(d.values())
    x=x[::-1]
    y=0
    n=0

    dr=0
    while y<int(number):
        for w in d:
            if y!=n:
                n+=1
                dr+=1
                if dr==4:
                    dr=0
                    s+= '<br>'

            if d[w]==x[y]:
                s+= str(y+1)+') '+w+': '+str(x[y])

                y+=1
    return s
def letters(x):
    s = 0
    constitution=x[1]
##    constitution.split()
    d=[]
    for word in constitution:
        for l in word:
            d.append(l)

    s+= len(d)
    return s

if __name__=="__main__":
    app.debug=True
    app.run()
