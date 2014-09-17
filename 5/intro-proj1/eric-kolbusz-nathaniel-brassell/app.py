from flask import Flask,render_template,flash

app = Flask(__name__)
app.secret_key = 'whydoesthisneedtobehere'

@app.route("/home")
@app.route("/") 
def home():
    return '''
    <h1>This is the home page</h1>
    <br>
    <form action="/page1">
        <input type="submit" value="Start">
    </form>
    '''

@app.route("/page1")
def page1(a1=None,a2=None,a3=None,a4=None,a5=None):
    print(a1)
    if (a1 != None):
        print(a1+'\n')
        flash(a1)
        print("hey it worked\n") #too bad it doesnt
        return redirect(url_for("/page2")) #maybe someday when I can use integers in flask loops
    else:
        flash(a1)
        return render_template("question.html"
                               ,qnum=1
                               ,a1=a1
                               ,a2=a2
                               ,a3=a3
                               ,a4=a4
                               ,a5=a5)
    
@app.route("/page2")
@app.route("/page2?a1=<a1>")
def page2(a1=None,a2=None,a3=None,a4=None,a5=None):
    return render_template("question.html"
                           ,qnum=2
                           ,a1=a1
                           ,a2=a2
                           ,a3=a3
                           ,a4=a4
                           ,a5=a5)

@app.route("/page3")
@app.route("/page3?a1=<a1>&a2=<a2>")
def page3(a1=None,a2=None,a3=None,a4=None,a5=None):
    return render_template("question.html"
                           ,qnum=3
                           ,a1=a1
                           ,a2=a2
                           ,a3=a3
                           ,a4=a4
                           ,a5=a5)

                                                 
if __name__=="__main__":
    app.debug=True
    app.run() 
    
