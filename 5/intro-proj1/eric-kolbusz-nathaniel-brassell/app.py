from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/home")
@app.route("/") 
def home():
    return '''
    <h1>This is the home page</h1>
    <br>
    <form action="/survey">
        <input type="submit" value="Start">
    </form>
    '''

@app.route("/survey")
def survey():
    a1 = request.args.get("a1","None")
    a2 = request.args.get("a2","None")
    a3 = request.args.get("a3","None")
    a4 = request.args.get("a4","None")
    a5 = request.args.get("a5","None")
    if (a1 == "None"):
        return render_template("question.html",question="Ostriches ________ fly",
                               choice1="Always",choice2="Sometimes",choice3="Never",choice4="Probably",
                               qnum=1,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a2 == "None"):
        return render_template("question.html",question="This slang term can be found as early as 1806 Scotland",
                               choice1="Gonna",choice2="Hi",choice3="Sup",choice4="Swag",
                               qnum=2,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a3 == "None"):
        return render_template("question.html",question="Dive, Eive, Five, ________, Hive",
                               choice1="Guys",choice2="Give",choice3="Six",choice4="Drive",
                               qnum=3,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a4 == "None"):
        return render_template("question.html",question="Today ________ are ________, that is truer than true. There is no one alive who is ________er than ________. - Dr. Seuss",
                               choice1="You",choice2="True",choice3="False",choice4="They",
                               qnum=4,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a5 == "None"):
        return render_template("question.html",question="Which of these Pixar movies won 2 Oscars in 2010?",
                               choice1="Toy Story 3",choice2="Cars",choice3="Up",choice4="Cars 2",
                               qnum=5,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    else:
        #done
        nums = [1,2,3,4,5]
        questions = ["Ostriches ________ fly",
                     "This slang term can be found as early as 1806 Scotland",
                     "Dive, Eive, Five, ________, Hive",
                     '''Today ________ are ________, that is truer than true.
                        There is no one alive who is ________er than ________. - Dr. Seuss''',
                     "Which of these Pixar movies won 2 Oscars in 2010?"]
        answers = [a1,a2,a3,a4,a5]
        correct = ["Never","Gonna","Give","You","Up"]
        check = [None,None,None,None,None]
        numcorrect = 0
        easteregg = None
        for i in range(5):
            if answers[i] == correct[i]:
                check[i] = 1
                numcorrect = numcorrect + 1

        s= ''
        for item in check:
            s= s+str(item)+' '
        print(s+'\n')
        
        if (numcorrect == 5):
            easteregg = "whoo"
            
                          
        return render_template("results.html",
                               nums=nums,
                               questions=questions,
                               answers=answers,
                               check=check,
                               easteregg=easteregg)

if __name__=="__main__":
    app.debug=True
    app.run() 
    
