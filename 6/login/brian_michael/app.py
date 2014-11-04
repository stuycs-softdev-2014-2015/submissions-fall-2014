from flask import Flask,request,redirect,render_template,session,flash
import db

app=Flask(__name__)
app.secret_key ='insert_clever_secret_here'

@app.route('/')
def root():
    return redirect('home')

@app.route('/login',methods=['GET','POST'])
def login():
    if "user" in session:
        
        flash("Please logout first to log into another account!")
        return render_template('home.html',name=db.getName(session['user']))
    if request.method=='GET':
        return render_template('login.html')
    else:
        user=request.form['user']
        pw=request.form['pass']
        if db.validateUser(user,pw):
            session['user']=user
            if 'return_to' in session:
                s = session['return_to']
                session.pop('return_to',None)
                return redirect(s)
            else: return redirect('/home')
        else:
            flash('Please enter a valid username and password')
            return render_template('login.html')
            
@app.route('/register',methods=['GET','POST'])
def register():
    if "user" in session:
        
        flash("Please logout first to register another account!")
        return render_template('home.html',name=db.getName(session['user']))
    if request.method=='GET':
        return render_template('register.html')
    else:
        
        name=request.form['name']
        user=request.form['user']
        pw=request.form['pass']
        color=request.form['color']
        if name == "" or user == "" or pw =="" or color == "":
            flash('Please fill in all the fields')
            return redirect('/register')
        elif db.existingName(user)== False:
            flash('Your username is already taken!')
            return redirect('/register')
        else:
            
            if db.registerUser(user,name,color,pw):
                return redirect('/login')
            else:
                return redirect('/about') ##should be replaced with flash

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')

@app.route('/about')
def about():
    if 'user' not in session:
        return render_template('about.html')
    else:
        return render_template('about.html',user=session['user'],name=db.getName(session['user']))

@app.route('/home')
def home():
    if 'user' not in session:
        session['return_to']='/home'
        return redirect('/login')
    else:
        return render_template('home.html',name=db.getName(session['user']))
        
@app.route('/settings',methods=['GET','POST'])
def settings():
    if 'user' not in session:
        session['return_to']='/settings'
        return redirect('/login')
    else:
        if request.method=='GET':
            return render_template('settings.html',name=db.getName(session['user']))
        else:
            
            ##get new info and update
            user = session['user']
            name=request.form['name']
            pw = request.form['oldpw']
            newpw = request.form['newpw']
            color = request.form['color']
            if pw == "" or not db.updateUserInfo(user,pw,newpw,name,color):
                flash("Please enter your correct current password to make any changes!")
                return redirect("/settings")
            else:
                return redirect('/home')

if __name__ == '__main__':
    
    app.debug=True
    app.run()
