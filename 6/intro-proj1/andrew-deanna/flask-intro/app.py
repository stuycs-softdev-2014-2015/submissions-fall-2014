import random
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/oneDice")
def oneDice():
    dice1num = random.randrange(1,7)
    sumdice = dice1num
    return render_template("oneDice.html",
                           dice1num=dice1num,
                           sumdice=sumdice
                          )

@app.route("/twoDice")
def twodice():
    dice1num = random.randrange(1,7)
    dice2num = random.randrange(1,7)
    sumdice = dice1num + dice2num
    return render_template("twoDice.html",
                           dice1num=dice1num,
                           dice2num=dice2num,
                           sumdice=sumdice
                          )

@app.route("/threeDice")
def threeDice():
    dice1num = random.randrange(1,7)
    dice2num = random.randrange(1,7)
    dice3num = random.randrange(1,7)
    sumdice = dice1num + dice2num + dice3num
    return render_template("threeDice.html",
                           dice1num=dice1num,
                           dice2num=dice2num,
                           dice3num=dice3num,
                           sumdice=sumdice
                          )


@app.route("/ball")
def ball():
    answers = [ "Yes!", "No!", "Ask again later.", "If you will it!", "Maybe so!", "No, 'cause you're a bum" ]
    numb = random.randrange(0,6)
    result = answers[numb]
    return render_template("8ball.html",
                           result=result
                           )

@app.route("/coin")
def coin():
    side=""
    a = random.randrange(0,2)
    if a == 1:
        side = "heads"
    else:
        side = "tails"
    return render_template("coin.html",
                           side=side
                           )



def shakeBall():
    answers = [ "Yes!", "No!", "Ask again later.", "If you will it!", "Maybe so!", "No, 'cause you're a bum" ]
    numb = random.randrange(0,8)
    return answers[numb] 


if __name__=="__main__":
    app.debug=True
    app.run()
