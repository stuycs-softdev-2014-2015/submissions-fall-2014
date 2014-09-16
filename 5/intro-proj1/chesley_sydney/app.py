from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("data.html",
            headers=getTableHeaders("static/JRSmith.csv"),
            data=getTableItems("static/JRSmith.csv"),
            csv_file_name="JRSmith.csv")


def getTableHeaders(fileName):
    f=open(fileName,'r')
    data=f.readline()
    f.close()
    headers = data.split(",");
    return headers;

def getTableItems(fileName):
    f=open(fileName,'r')
    data=f.readlines()
    f.close()
    items = []
    for row in data[1:]:
        tmp = []
        for item in row.split(","):
           tmp.append(item)
        items.append(tmp)
    return items;


if __name__ == "__main__":
    app.debug = True
    app.run()
