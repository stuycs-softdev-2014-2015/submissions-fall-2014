from flask import Flask, render_template, request
import csv, glob

names = glob.glob("*.csv")
files = []
lines = []
d = {}
#Source: http://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python

for name in names:
    f = open(name, 'rb') 
    try:
        reader = csv.reader(f)
        lines.append(reader.next())
        tempList = []
        for row in reader:
            tempList.append(row)
        files.append(tempList)
        d[name] = len(d)
    finally:
        f.close()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", lines=lines, names=names)

@app.route("/<filename>")
def data(filename = None):
    index = 0;
    index2 = d[filename]
    for i in range(len(lines[index2])):
        if lines[index2][i] == request.args['sort']:
            index = i

    L = []
    L.append(lines[index2])
    L = L + sorted(files[index2], key=lambda x: x[index], reverse=(index>=5))
    
    print L
    return render_template("file.html", l=L, filename=filename)

if __name__=="__main__":
    app.debug=True
    app.run()
