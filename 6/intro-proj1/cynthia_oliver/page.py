from flask import Flask,render_template,request


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)

def htmlify(s):
    x = ""
    x += "<html><head><title>NBAstats</title>"
    x += s
    
    return x

def getStats(filename):
    x = open(filename)
    y = x.readlines()
    x.close
    i = 0
    while i < len(y):
        y[i] = y[i].strip()
        i += 1
    return y[1:]

def getstatheaders(filename):
    x = open(filename)
    y = x.readlines()
    x.close
    i = 0
    while i < len(y):
        y[i] = y[i].strip()
        i += 1
    return y[0].split(",")

def pythtable(csvfile):
    l = getStats(csvfile)
    m = getstatheaders(csvfile)
    p = "<table border = '3'>"
    k = 0
    p += "<tr>"
    while k < len(m):
        p += "<td>"
        p += m[k]
        p += "</td>"
        k += 1
    p += "</tr>"
    i = 0
    while i < len(l):
        p += "<tr>"
        a = l[i].split(",")
        j = 0
        while j < len(a):
            p += "<td>"
            p += str(a[j])
            p += "</td>"
            j += 1
            
        p += "</tr>"
        i += 1
    p += "</table>"
    return p
x = "NBAstats.csv"

@app.route("/source")
def source():
    return render_template("source.html")

@app.route("/comment")
def comment():
    l = ['cookies', 'donuts', 'ice cream', 'muffins']
    if request.method=="GET":
        return render_template("comment.html", l=l)
    
        
 
@app.route("/project")
def help():
    return htmlify(pythtable(x))

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")
if __name__=="__main__":
    app.debug=True
    app.run()
