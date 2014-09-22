from flask import Flask, render_template, request
import utils
app = Flask(__name__)


@app.route("/")
def start():

    return render_template("home.html")



@app.route("/results", methods=["POST", "GET"])
def main():
    
    if request.method=="POST":
	print "hi"
        building_type=request.form["building_type"]
	print building_type
        zip_start=request.form["zip_start"]
        print zip_start
        zip_end=request.form["zip_end"]
        print zip_end
        
        return render_template("results.html", lines=utils.results(), building_type= building_type, zip_start = zip_start, zip_end = zip_end)


if __name__ == "__main__":
    app.debug = True
    app.run()
