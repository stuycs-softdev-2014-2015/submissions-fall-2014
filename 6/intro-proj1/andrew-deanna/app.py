import random
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dice")
def dice():
    dice1num = random.randrange(1,7)
    dice2num = random.randrange(1,7)
    sumdice = dice1num + dice2num
    return render_template("dice.html",
                           dice1num=dice1num,
                           dice2num=dice2num,
                           sumdice=sumdice
                          )

def shakeBall():
    answers = { "Yes!", "No!", "Ask again later.", "If you will it!", "Maybe so!", "No, 'cause you're a bum" }
    numb = random.randrange(0,8)
    return answers[numb]

@app.route("/ball")
def ball():
    result = shakeBall()
    return render_template("8ball.html",
                           result=result
                           )


if __name__=="__main__":
    app.debug=True
    app.run()
