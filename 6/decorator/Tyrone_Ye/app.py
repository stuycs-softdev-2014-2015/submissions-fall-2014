from flask import Flask
from flask import session, url_for, redirect
#from functools import wraps

app = Flask(__name__)
app.secret_key = 'sdafsadfs'

#def auth(link):
 #   def authin(func):
  #      @wraps(func)
   #     def authpage(*args, **kwargs):
    #        if not 'username' in session:
     #           return login(link)
      #      else:
       #         return func(*args,**kwargs);

@app.route("/")
def home():
    return """<a href="/hi">Say HI</a>"""

#@auth
@app.route("/hi")
def home():
    return "<h1> Hi </h1>"


@app.route("/login", methods=['GET', 'POST'])
def login(redir = "/"):
    if request.method == "GET":
        return """<form method="GET"> 
Username: <input type="text" name="username"><p>
<input type="submit" name="button" value="Submit">"""
    else:
        session['username'] = username
        return redirect(redir)

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
