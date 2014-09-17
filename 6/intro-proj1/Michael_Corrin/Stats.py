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
        +str(num3/v)+ "</td> <td>"+str(num4/v)+"</td></tr> </table>"
    return m
def sumSAT2(table):
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
            if num >= 1800:
                m+="<td>"+ n[1]+"</td><td>" + n[2] +"</td><td>"+ str(num)+"</td></tr><tr>"
            num = 0
            y += 1
    return m
@Stats.route("/SAT")
def SAT():
    return render_template("sat.html")

if __name__=="__main__":
    Stats.debug=True
    Stats.run()
