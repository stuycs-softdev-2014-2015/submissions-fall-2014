from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.chrisndbrian
accounts = db.one
profiles = db.two
post_id = 1

app = Flask(__name__)
@app.route("/")
@app.route("/login", methods = ['GET','POST'])
def login():
	return render_template("login.html");

@app.route("/register", methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print username
		print password
		if username=="" or password=="":
			return redirect('/failedregister')
		else:
			newacc = {"username" : username, "password": password}
			accounts.insert(newacc)
			return redirect('/login')
	else:
		return render_template("Register.html")

@app.route("/failedlogin")
def failedlogin():
	return render_template("failedlogin.html")

@app.route("/failedregister")
def failedregister():
	return render_template("failedregister.html")


@app.route("/index", methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		print request.form
		username = request.form['username']
		password = request.form['password']
		p = accounts.find_one({"username": username})
		if username=="" or password == "":
			return redirect('/failedlogin')
		elif p!=None:
			if p["password"] == password:
				global post_id
				post_id = p['_id']
				print "MISSION SUCCESS"
				print post_id
				return render_template("index.html")
				#render_template();"""
			else:
				return redirect('/failedlogin')
		else:
			return redirect('/failedlogin')

@app.route("/profile",methods=['GET','POST'])
def profile():
	if request.method == 'POST':
		OptionRadios = request.form['OptionRadios']
		print OptionRadios
		p = accounts.find_one({"_id":post_id})
		#if p==None:
			#print True
			#newprof = {"_id":post_id}#, #"hobby":request.form['hobby']}#, "movie":request.form["movie"], "quote":request.form["quote"],"OptionRadios":request.form["OptionRadios"],"OptionRadios2":request.form["OptionRadios2"]"""}
			#profiles.insert(newprof)
		print "TRUE PART 2------------------------"
		username = p['username']
		print "TRUE PART 3------------------------"
		a = request.form['OptionRadios']
		print request.form
		return render_template("profile.html",username=username,movie=request.form.get('movie',None))#,OptionRadios=request.form['OptionRadios'])#,OptionRadios2=request.form["OptionRadios2"],hobby=request.form["hobby"],quote=request.form["quote"])



@app.route("/About")
def About():
	return render_template("About.html")

if (__name__) == "__main__":
	app.debug = True
	app.run()
