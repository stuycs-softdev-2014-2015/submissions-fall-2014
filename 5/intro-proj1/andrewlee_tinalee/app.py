from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    html = ""
    html += "<html><title>" + "Home Page" + "</title>"
    html += "<h1>Starter Pokemon</h1>"
    html += tablefy('Water Starters.csv',"33CCFF")
    html += tablefy('Fire Starters.csv',"FF9933")
    html += tablefy('Grass Starters.csv',"33CC66")
    html += "<br>"
    html += "<a href = '/avg'>Average of Starter Pokemon</a>"
    html += "</html>"
    return html

@app.route("/avg")
def avg():
    x = open('pokemonAverages.csv')
    readFile = x.readlines()
    firstLine = readFile[0].split(",")
    water = readFile[1].split(",")
    fire = readFile[2].split(",")
    grass = readFile[3].split(",")
    return render_template("avg.html", firstLine = firstLine, water = water, fire = fire, grass = grass)

@app.route("/")
def index():
    uname = request.args.get("uname",None)
    button = request.args.get("b",None)
    if button == None or button=="Cancel":
        return render_template("index.html")
    else:
       return "<a href = 'home'>Click this!</a>"

    
def tablefy(fileName,color):
    x = open(fileName)
    readFile = x.readlines()
    tableHtml = '<table border = "1" bgcolor =' + color + '>'
    firstLine = readFile[0].split(",")
    for column in firstLine:
        column = column.strip()
        tableHtml += "<th>" + column + "</th>"
    for line in readFile[1:]:
        line = line.split(",")
        tableHtml += "<tr>"
        for column in line:
            column = column.strip()
            tableHtml += "<td><center>" + column + "</center></td>"
        tableHtml += "</tr>"
    tableHtml += '</table></head><br>'
    return tableHtml


if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(host = "0.0.0.0", port = 1657)


