from flask import Flask, render_template, request
import random,md5
app = Flask(__name__)
i1=random.random()
i2=random.random()

@app.route('/')
def home(var1=None,var2=None,var3=None):
        var1=random.random()
        var2=random.random()
        var3='href=/login'
	return render_template('home.html',var1=var1, var2=var2, var3=var3)

@app.route('/login', methods=["GET","POST"])
def login(firstname=None, lastname=None):
	if request.method == "POST":
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
	if(firstname != None and lastname !=None):
		return render_template ('data.html', firstname=firstname, lastname=lastname)
        else:
		return render_template('login.html')

if __name__=="__main__":
	
        app.debug=True
        app.run()
