from flask import Flask, render_template
# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/zestats")
def zestats():
    return render_template("analysis.html")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/data")
def data():
    return render_template("data.html")





if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()
    
