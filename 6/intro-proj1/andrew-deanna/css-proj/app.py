import random
import utils
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/advertisers")
def advertisers():
    return render_template("advertisers.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/rates", methods=['GET', 'POST'])
def rates():
    button = request.args.get("b",None)
    issues = request.args.get("issues",None)
    size = request.args.get("size",None)
    print button,issues,size
    if button == None:
        return render_template("rates.html",image="AdSizes")
    else:
        return render_template("rates.html",
                                priced="TRUE",
                                price="1000",
                                image=utils.getImg(size)
                                )



@app.route("/cssdemo")
def cssdemo():
    return render_template("cssdemo.html")


if __name__=="__main__":
    app.debug=True
    app.run()
