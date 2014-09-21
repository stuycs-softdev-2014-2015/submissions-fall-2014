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
    a1 = request.args.get("a1",None)
    a2 = request.args.get("a2",None)
    a3 = request.args.get("a3",None)
    a4 = request.args.get("a4",None)
    a5 = request.args.get("a5",None)
    if (a1 == None):
        return render_template("question.html",qnum=1,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a2 == None):
        return render_template("question.html",qnum=2,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a3 == None):
        return render_template("question.html",qnum=3,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a4 == None):
        return render_template("question.html",qnum=4,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    if (a5 == None):
        return render_template("question.html",qnum=5,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
                                                 
if __name__=="__main__":
    app.debug=True
    app.run() 
    
