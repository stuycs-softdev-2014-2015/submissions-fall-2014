
from flask import Flask, render_template, request
import utils
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        building_type=request.form["building_type"]
        button=request.form["search"]
        print 
        if button=="Search":
            return render_template("results.html", lines=utils.results())


if __name__ == "__main__":
    app.debug = True
    app.run()
