from flask import Flask, render_template,request

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

@app.route("/analysis", methods=["GET","POST"])
def analysis():
    headers = getLabeledTableHeaders("static/JRSmith.csv")
    p1 = getLabeledLastRow("static/JRSmith.csv", "JR Smith")
    p2 = getLabeledLastRow("static/NateRobinson.csv", "Nate Robinson")
    diff = analysis("static/JRSmith.csv", "static/NateRobinson.csv")
    page_title = "Per Game Analysis"
    content_header = "JR Smith vs Nate Robinson"
    if request.method=="GET":
        return render_template("analysis.html", headers=headers, p1=p1, p2=p2,
                           diff=diff, page_title=page_title, content_header=content_header)
    elif request.method=="POST":
        comment= request.form["comment_field"]
        print comment
        button=request.form["submit"]
        if button=="Go!":
            return render_template("comment.html", comment=comment)
        else:
            return render_template("analysis.html", headers=headers, p1=p1, p2=p2,
                    diff=diff, page_title=page_title, content_header=content_header)
            
def getTableHeaders(fileName):
    f=open(fileName,'r')
    data=f.readline()
    f.close()
    headers = data.split(",");
    return headers;

def getLabeledTableHeaders(fileName):
    headers = ["Player Name"]
    f=open(fileName,'r')
    for d in f.readline().split(","):
        headers.append(d)
    f.close()
    return headers;

def getLabeledLastRow(fileName, name):
    data = [str(name)]
    f=open(fileName,'r')
    for d in f.readlines()[-1].split(","):
        data.append(d)
    f.close()
    return data

    
def analysis(file1, file2):
    diff = ["Difference"]
    f1=open(file1, 'r')
    data1 = f1.readlines()[-1].split(',')
    f1.close()
    f2=open(file2, 'r')
    data2 = f2.readlines()[-1].split(',')
    f2.close()
    for i in range(len(data1)):
        if data1[i] != "" and type(data1[i]) is str:
            try:
                diff.append(str(float(data1[i]) - float(data2[i])))
            except ValueError:
                diff.append('')
        else:
            diff.append('')
    return diff
    

def getLastRow(fileName):
    f=open(fileName, 'r')
    data=f.readlines()[-1]
    f.close()
    return data.split(",")

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
