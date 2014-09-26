from flask import Flask,render_template,request

app = Flask(__name__)

data = open('pokemon.csv', 'r')
data = data.readlines()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data', methods=["GET", "POST"])
def datapage():
    if request.method=="GET":
        return render_template("mainpage.html", 
                               data=data,
                               num=0,
                               length = len(data))
    else :  #post
        query = request.form["query"]
        searchdata = []
        for line in data:
            if line.find(query,0) >= 0:
                searchdata.append(line)
        if len(searchdata)==0:
            searchdata = data
            query += " Not found."

        return render_template("mainpage.html",
                               namequery="Search for: "+query,
                               data=searchdata,
                               num=0,
                               length = len(searchdata))

if __name__ == "__main__":
    app.debug=True
    app.run()
