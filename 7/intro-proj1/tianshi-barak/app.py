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
    """
    return s

#@app.route("/kda")
#def kda():
    #return render_template("kda.html")

#@app.route("/kills")
#def kills():

@app.route("/data")
def data():
    s = """
<table style="width:100%">
 <tr>
<th>Champion</th>
<th>KDA Ratio</th>
<th>Kills</th>
<th>Deaths</th>
<th>Assist</th>
</tr>
<tr>
"""
    for x in data_text:
        s+= "<tr>"
        for y in range(0,len(x)):
            s += "<td>" + x[y] + "</td>"
        s+= "</tr>"
    s += "</table>"
    return s

if __name__ == "__main__":
    app.debug=True
    app.run()
