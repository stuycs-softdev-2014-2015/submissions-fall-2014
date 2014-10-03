from flask import Flask, session, redirect, url_for, escape, request
import random
from functools import wraps

app = Flask(__name__)

def auth(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if 'username' in session:
            return f(*args,**kwargs)
        else:
            return redirect(url_for('bad'))
    return wrapper


@app.route("/login")
def login():
    session['username'] = "guy"
    return """
you are logged in.\n

go to /logout to logout\n

go back to / if you want
"""

@app.route("/bad")
def bad():
    return """You are not logged in. Go to /login to do so"""

@app.route("/logout")
@auth
def logout():
    session.pop('username',None)
    return """
you are logged out.
"""

@app.route("/random")
@auth
def random():
     return """090090980usfidkajhnf,nkhmmkhjadsfkhjfahdjskjfahdan fds hajchfhdjshjkdhjfajslhjdfalsdkfn cahjshsfdhjlfkhsahlkdfjhafhdsjklfdahslfajksdfhlshadjcnnhcsanhdacsfdsnfdsajlkhfhdjcjskfdnashcdfafdhfahcdjkasjlfncfasnfn a nnnhjnhchnasfhnvnhashfjkchdsannjkfdjkhsahufaeww9439y7843y939ryny3nrayf8y83rcu98y3r99y83rn9r39ayy89r3any39ranrfacy98yra8y9ary9cra8y9nra998yecdwahuininhyudcew8ynewanynedcw9a98y0ewy98a98cn98983ryay83r80c090090980usfidkajhnf,nkhmmkhjadsfkhjfahdjskjfahdan fds hajchfhdjshjkdhjfajslhjdfalsdkfn cahjshsfdhjlfkhsahlkdfjhafhdsjklfdahslfajksdfhlshadjcnnhcsanhdacsfdsnfdsajlkhfhdjcjskfdnashcdfafdhfahcdjkasjlfncfasnfn a nnnhjnhchnasfhnvnhashfjkchdsannjkfdjkhsahufaeww9439y7843y939ryny3nrayf8y83rcu98y3r99y83rn9r39ayy89r3any39ranrfacy98yra8y9ary9cra8y9nra998yecdwahuininhyudcew8ynewanynedcw9a98y0ewy98a98cn98983ryay83r80c090090980usfidkajhnf,nkhmmkhjadsfkhjfahdjskjfahdan fds hajchfhdjshjkdhjfajslhjdfalsdkfn cahjshsfdhjlfkhsahlkdfjhafhdsjklfdahslfajksdfhlshadjcnnhcsanhdacsfdsnfdsajlkhfhdjcjskfdnashcdfafdhfahcdjkasjlfncfasnfn a nnnhjnhchnasfhnvnhashfjkchdsannjkfdjkhsahufaeww9439y7843y939ryny3nrayf8y83rcu98y3r99y83rn9r39ayy89r3any39ranrfacy98yra8y9ary9cra8y9nra998yecdwahuininhyudcew8ynewanynedcw9a98y0ewy98a98cn98983ryay83r80c090090980usfidkajhnf,nkhmmkhjadsfkhjfahdjskjfahdan fds hajchfhdjshjkdhjfajslhjdfalsdkfn cahjshsfdhjlfkhsahlkdfjhafhdsjklfdahslfajksdfhlshadjcnnhcsanhdacsfdsnfdsajlkhfhdjcjskfdnashcdfafdhfahcdjkasjlfncfasnfn a nnnhjnhchnasfhnvnhashfjkchdsannjkfdjkhsahufaeww9439y7843y939ryny3nrayf8y83rcu98y3r99y83rn9r39ayy89r3any39ranrfacy98yra8y9ary9cra8y9nra998yecdwahuininhyudcew8ynewanynedcw9a98y0ewy98a98cn98983ryay83r80c"""

@app.route("/")
@auth
def home():
    return """welcome to my useless website\n\ngo to /logout to log out\n\ngo to /random for something random""" 

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run()


