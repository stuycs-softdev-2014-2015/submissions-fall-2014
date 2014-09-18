from flask import Flask,render_template

Stats = Flask(__name__)

def sumSAT(table):
    outStream=open(table,'r')
    x = outStream.readlines()
    outStream.close()
    y = 1
    num = 0
    num2 = 0
    num3 = 0
    num4 = 0
    v = 0
    m= ""
    while y < len(x):
        n = x[y].split(",")
        if n[3] == "s":
            y+= 1
        else:
            num += int(n[3]) + int(n[4]) + int(n[5])
            num2 += int(n[3])
            num3 += int(n[4])
            num4 += int(n[5])
            v += 1
            y+= 1
    m += "<tr> <td>" +str(num/v)+" </td> <td>" +str(num2/v)+ "</td> <td>"\
        +str(num3/v)+ "</td> <td>"+str(num4/v)+"</td></tr></table>"
    return m
def sumSAT2(table,Number):
    outStream=open(table,'r')
    x = outStream.readlines()
    outStream.close()
    y = 1
    num = 0
    num2 = 0
    num3 = 0
    num4 = 0
    v = 0
    m= ""
    while y < len(x):
        n = x[y].split(",")
        if n[3] == "s":
            y+= 1
        elif Number==0:
            num += int(n[3]) + int(n[4]) + int(n[5])
           
            if num >= 1800:
                m+="<td>"+ n[1]+"</td><td>" + n[2] +"</td><td>"+ str(num)+"</td></tr><tr>"
            num = 0
            y += 1
        else:
            m+="<td>"+ n[1]+"</td><td>" + n[2] +"</td><td>"+n[3]+"</td><td>"+n[4]+"</td><td>"+n[5]+"</td></tr><tr>"
            y+=1
    return m
@Stats.route("/SAT")
def SAT():
    table1=sumSAT2('2010SAT.csv',1)+"</tr></table>"
    return render_template("satall.html",table1=table1)
@Stats.route("/Analysis")
def Analysis():
    table3=""
    table2=""
    table3 += sumSAT('2010SAT.csv')
           
    table2+=sumSAT2('2010SAT.csv',0)
    

    return render_template("sat.html",table=table3,table2=table2)
@Stats.route("/")
def Go():
    return render_template("start.html")

if __name__=="__main__":
    Stats.debug=True
    Stats.run()
