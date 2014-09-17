from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("data.html",
            page_title="JR Smith's and Nate Robinson's Season per game records",
            p1_section_header="JR Smith's per game stats",
            p1_headers=getTableHeaders("static/JRSmith.csv"),
            p1_data=getTableItems("static/JRSmith.csv"),
            p1_csv_file_name="JRSmith.csv",
            p2_section_header="Nate Robinson's per game stats",
            p2_headers=getTableHeaders("static/NateRobinson.csv"),
            p2_data=getTableItems("static/NateRobinson.csv"),
            p2_csv_file_name="NateRobinson.csv")


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
