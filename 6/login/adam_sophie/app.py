from flask import flash, Flask, g, render_template, session, redirect, url_for, escape, request
#from flask.ext.pymongo import PyMongo

import mongo

app = Flask(__name__)
app.secret_key = 'a'

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    udict = {'uname':False}
    if 'username' in session:
        username = escape(session['username'])
        udict = mongo.getUser(username)
    return render_template('home.html', udict = udict)

@app.route('/user', methods=['POST'])
def user():
    #print("user!");
    if request.method=="POST":
        print request.form['uname']
        newuser = {}
        newuser['uname'] = request.form['uname']
        newuser['fname'] = request.form['fname']
        newuser['lname'] = request.form['lname']
        newuser['pw'] = request.form['pw']
        newuser['rpw'] = request.form['rpw']
        valid_msg = mongo.new_user(newuser)
        if valid_msg == '':
            session['username'] = request.form['uname']
            return redirect('/home')
        else:
            flash(valid_msg)
            return redirect('/register')

@app.route('/login')
def login():    
    return render_template('login.html', udict={'uname':False})


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html', udict={'uname':False})


@app.route('/register')
def register():   
    return render_template('register.html', udict={'uname':False})


@app.route('/verify', methods=['POST'])
def verify():
    if request.method=="POST":
        uname = request.form['uname']
        pw = request.form['pw']
        valid_msg = mongo.check_pword(uname,pw)
        if valid_msg == '':
            session['username'] = uname
            return redirect('/home')
        else:
            flash(valid_msg)
            return redirect('/login')

@app.route('/personal', methods=['GET','POST'])
def personal():    
    username = escape(session['username'])
    if request.method=="POST":
        submit = request.form['submit']
        if submit == 'name':
            mongo.addfield(username,"fname",request.form["fname"])
            mongo.addfield(username,"lname",request.form["lname"])          
        mongo.addfield(username,submit,request.form[submit])
    return render_template('personal.html', udict=mongo.getUser(username))

@app.route('/name')
def name():
    username = escape(session['username'])
    return render_template('personal.html', udict=mongo.getUser(username),change = "change" )
    
@app.route('/age')
def age():
    username = escape(session['username'])
    return render_template('personal.html', udict = mongo.getUser(username),changeage = "change" )

@app.route('/gpa')
def gpa():
    username = escape(session['username'])
    return render_template('personal.html', udict = mongo.getUser(username),changegpa = "change" )

@app.route('/colleges', methods=['GET','POST'])
def colleges():
    username = escape(session['username'])
    if request.method=="POST":
        colleges = request.form.getlist("college")
        newcolleges = []
        for college in colleges:
            newcolleges.append(college.replace("_"," "))
        mongo.addColleges(username, newcolleges)
        
    return render_template('colleges.html', udict = mongo.getUser(username))


@app.route('/addcolleges', methods=['POST','GET'])
def addcolleges():
    if request.method=="POST":
        d = {}
        #college name,location,min gpa,size,type,description
        username = escape(session['username'])
        print("start")
        if request.form.get("size") != None:
            d['size'] = request.form["size"]
        if request.form.get("type") != None:
            print(request.form["type"])
            print("hey1")
            d['type'] = request.form["type"]
        if request.form.get("location") != '':
            print("hey")
            d['location'] = request.form["location"]
        if request.form.get("gpa") != '':
            d['min gpa'] = request.form["gpa"]
        
        collegematch = mongo.collegeLookup(username, d)
        collegeunder = []
        for college in collegematch:
            collegeunder.append(college['name'].replace(" ","_")) 
        
        Clist = []
        x = 0;
        while (x < len(collegematch)):
            nlist = []
            nlist.append(collegematch[x])
            nlist.append(collegeunder[x])
            x=x+1
            Clist.append(nlist)
        return render_template('collegematches.html',Clist = Clist,udict = mongo.getUser(username))

@app.route('/allcolleges')
def allcolleges():
    username = escape(session['username'])
    return render_template('allcolleges.html', colleges = mongo.getColleges(),udict = mongo.getUser(username))


if __name__ == '__main__':
    app.debug = True
    app.run()
