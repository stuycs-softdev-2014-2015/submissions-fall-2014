from flask import Flask,render_template


app = Flask(__name__)

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/about")
def about():
    #s = "<h1>this is an excercise Z made us do</h1>"
    return render_template("about.html")

@app.route("/random")
def randomnumber():
    import random
    num = random.randrange(0,100)
    
    return render_template("random.html",
                           num=num,
                           name="Mr. T",
                           l=[1,2,3,4,5],
                           d={'a':1,'two':2,3:'hello'})


@app.route("/home")
@app.route("/") 
def home():
    s = "<table>"
    data = open("pokemon2.csv", "r")
    t = data.readline().split(',')
    for b in t:
        s = s + "<th>" + b + "</th>"
    data.readline()
    for line in data:
        s = s + "<tr>"
        t = line.split(',')
        for b in t:
            s = s + "<td>" + b + </td>
        s = s + "</tr>"
    data.close()
    s = s + "</table>"
    return render_template("home.html")
    

if __name__=="__main__":
    app.debug=True
    app.run() 
