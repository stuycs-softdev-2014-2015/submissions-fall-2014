from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        button = request.form["b"]
        uname = request.form["uname"]
        pword = request.form['pword']
        if button=="cancel" or uname=="" or pword=="":
            return render_template("login.html")
        else:
            if button=="register":
                inStream = open("userlist.txt","r")
                data = inStream.read()
                inStream.close()
                if uname in data:
                    return render_template("login.html")
                elif pword in data:
                    return render_template("login.html")
                else:
                    outStream=open("userlist.txt","a")
                    outStream.write(uname+':'+pword+"\n")
                    outStream.close()
            elif button=="login":
                inStream = open("userlist.txt","r")
                data = inStream.read()
                inStream.close()
                if not(uname+":"+pword in data):
                    return render_template("login.html")
            return redirect(url_for('data'))

@app.route("/")
def home():
     return redirect(url_for('login'))
@app.route("/data")
def data():
    inStream = open("data01.csv",'r')
    data = inStream.read()
    inStream.close()
    rows = data.split("\n")
    for i in range(0,len(rows)):
        rows[i] = rows[i].split(",")
    return render_template("data.html", info = rows)
@app.route("/analysis")
def analysis():
    inStream = open("averages_hw25.csv","r")
    data = inStream.read()
    inStream.close()
    rows = data.split("\n")
    for i in range(0,len(rows)):
        rows[i] = rows[i].split(",")
    return render_template("analysis.html", info=rows)
if __name__=="__main__":
    app.debug=True
    app.run() 

    
