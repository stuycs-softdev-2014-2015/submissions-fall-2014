from flask import Flask, render_template, request

data_file = open("data.csv", "r")

data_text = data_file.read();

#THIS IS THE THING WE ARE USING
data_text = [x.split(",") for x in data_text.split("\n")]

#print data_text

data_file.close();

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    button = request.args.get("b",None)
    search1 = request.args.get("search1",None)
    search2 = request.args.get("search2",None)
    print button, search1, search2
    if button == None or button == "Search":
        return render_template("survey.html");

@app.route("/results")
def results():
    ##returns the results of comparison

@app.route("/data")
def data():
    s = """
    <!DOCTYPE html>
    <html>
    <head>
    <h1 align="center"><b>LEAGUE OF LEGENDS CHAMPION STATISTICS</b></h1>
    <style>
    body {
    background-color: #b0c4de;
    }
    tr:hover{color: #F00;}
    </style>
    </head>
    <body>
    <table border="2" cellspacing="1" cellpadding="5" align="center">
    """
    i = 0;
    for x in data_text:
        s+= "<tr>"
        for y in range(0,len(x)):
            if i<5:
                s += """<th bgcolor="#FFFF00"><b>"""+x[y].upper()+"</b></td>"
            elif i%5==0: #for first row
                s += """<td bgcolor="#00FFCC"><b>""" + x[y] + "</b></td>"
            else:
                s += """<td bgcolor="#FF66FF">""" + x[y] + "</td>"
            i+=1
        s+= "</tr>"
    s += "</table></body></html>"
    return s
            

if __name__ == "__main__":
    app.debug=True
    app.run()
