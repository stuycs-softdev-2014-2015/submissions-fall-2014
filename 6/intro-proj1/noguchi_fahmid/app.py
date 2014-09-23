from flask import Flask,render_template
import utils

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
            query = request.form["name_query"]
            return render_template("mainpage.html",
                                   namequery=query,
                                   data=data,
                                   num=0,
                                   length = len(data))
            #Sadman change this part

if __name__ == "__main__":
    app.debug=True
    app.run()
