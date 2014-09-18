from flask import Flask, render_template

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
    s = """
    <h1>Welcome to our webpage.</h1>
    <h2> Tianshi Wang, Barak Zhou, pd7 </h2>
    <a href="../data">Check out our data!</a><br>

    <form action="../search/<search>" method="get">
    Or search for a champion: <input type="text" name="search"><br>
    <input type="submit" value="Search">
    </form>    
    """
    return s

@app.route("/search/<search>")
def search(search, methods=['POST']):
    s = """
<h1 align="center"><b>Search Results</b></h1>
"""
    for x in data_text:
        if x[0] == search:
            s += """
        <table border="2" cellspacing="1" cellpadding="5" align="center">
        """
            s+= "<tr>"
            for y in range(0,len(x)):
                if i<5:
                    s += """<th bgcolor="#FFFF00"><b>"""+x[y].upper()+"</b></td>"
                elif i%5==0: #for first row
                    s += """<td bgcolor="#00FFCC"><b>""" + x[y] + "</b></td>"
                else:
                    s += """<td bgcolor="#FF66FF">""" + x[y] + "</td>"
        s+= "</tr>"
        s += "</table>"
    return s



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
