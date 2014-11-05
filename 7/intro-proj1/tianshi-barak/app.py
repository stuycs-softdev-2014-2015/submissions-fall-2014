from flask import Flask, render_template, request

data_file = open("data.csv", "r")
data_text = data_file.read();

#THIS IS THE THING WE ARE USING
data_text = [x.split(",") for x in data_text.split("\n")]

champList = []
kdaList = []
killList=[]
deathList=[]
assistList=[]
for x in data_text:
    champList.append(x[0].upper())
    kdaList.append(x[1])
    killList.append(x[2])
    deathList.append(x[3])
    assistList.append(x[4])

data_file.close();

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("survey2.html");

@app.route("/results")
def results():
    button = request.args.get("b",None)
    search1 = request.args.get("search1",None)
    search2 = request.args.get("search2",None)
    if button == "Search":
        if search1.upper() in champList and search2.upper() in champList:
            i = champList.index(search1.upper())
            j = champList.index(search2.upper())
            kda1 = kdaList[i]
            kda2 = kdaList[j]
            kill1 = killList[i]
            kill2 = killList[j]
            death1 = deathList[i]
            death2 = deathList[j]
            assist1 = assistList[i]
            assist2 = assistList[i]
            return render_template("comparison2.html",
                                   search1 = search1.capitalize(), 
                                   search2 = search2.capitalize(),
                                   kda1 = kda1,
                                   kda2 = kda2,
                                   kill1 = kill1,
                                   kill2 = kill2,
                                   death1 = death1,
                                   death2 = death2,
                                   assist1 = assist1,
                                   assist2 = assist2)
        else:
            return render_template("/error2.html")
    
    
@app.route("/data")
#def data():
#  s = """
#  <!DOCTYPE html>
#  <html>
#  <head>
#  <h1 align="center"><b>LEAGUE OF LEGENDS CHAMPION STATISTICS</b></h1>
#  <style>
#  body {
#  background-color: #b0c4de;
#  }
#  tr:hover{color: #F00;}
#  </style>
#  </head>
#  <body>
#  <table border="2" cellspacing="1" cellpadding="5" align="center">
#  """
#  i = 0;
#  for x in data_text:
#      s+= "<tr>"
#      for y in range(0,len(x)):
#          if i<5:
#              s += """<th bgcolor="#FFFF00"><b>"""+x[y].upper()+"</b></td>"
#          elif i%5==0: #for first row
#              s += """<td bgcolor="#00FFCC"><b>""" + x[y] + "</b></td>"
#          else:
#              s += """<td bgcolor="#FF66FF">""" + x[y] + "</td>"
#          i+=1
#      s+= "</tr>"
#  s += "</table></body></html>"
#  return s
def data():
    return render_template("data.html");

if __name__ == "__main__":
    app.debug=True
    app.run()
