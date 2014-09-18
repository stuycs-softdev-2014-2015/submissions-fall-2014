from flask import Flask,render_template

app = Flask(__name__)

images=["static/img/chick.jpeg",
        "static/img/cow.jpg",
        "static/img/milk.gif",
        "static/img/pig.jpg",
        "static/img/sheep.jpg",
        "static/img/turkey.jpg",
    ]

@app.route("/")
def home():
    import random
    num = random.randrange(0,4)
    return render_template("home.html", 
                           img = images[num])

if __name__=="__main__":
    app.debug=True
    app.run()
    ##app.run(host="0.0.0.0",port=8000)
