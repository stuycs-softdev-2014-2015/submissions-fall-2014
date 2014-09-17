from flask import Flask
app = Flask(__name__)

html = ""

@app.route("/home")
@app.route("/")
def home():
    html += "<html><title>" + "Home Page" + "</title>"
    html += "<h1>Starter Pokemon</h1>"
    html += tablefy('Water Starters.csv',"33CCFF")
    html += tablefy('Fire Starters.csv',"FF9933")
    html += tablefy('Grass Starters.csv',"33CC66")
    html += "</html>"
    return html

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


