from flask import Flask, render_template, request
import unittest
import random
import string
from validator import EmailValidator

###############################
######## Intro-Proj 2 #########
### A. Fischer, G. Noguchi  ###
###############################

######### Flask Pages #########
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    submit    = request.args.get("submit",None)
    #Cancel just clears out the form using "reset"
    uname     = request.args.get("username",None)
    phone     = request.args.get("phone",None)
    password  = request.args.get("password",None)

    print "POST Data:"
    print submit,uname,phone,password

    #We need to add jinja2 substitutions if uname, password, or phone is wrong to show warnings.

    return render_template("index.html")


######### Validators ##########

TLDList = open("TLDs.txt").readlines()

def validate_email(email):
    sides = email.split("@")
    if len(sides) > 2:        # If there are multiple "@"
        return False          # It's not a good email

    uname = sides[0]
    provider = sides[1]

    if "." in provider:       # If it's not a website
        return False          # It's not a good email

    provSite = provider.split(".")
    TLD = provider[1]

    if TLD not in TLDList.lower():    # Not a real TLD?
        return False          # Not a real email

    else:
        return True


def validate_password(pword):
    if pword.find(" ")>=0: #No spaces
        return False
    if len(pword)<6 || len(pword)>20: #Length check
        return False
    if pword == pword.lower(): #Needs one upper case character
        return False
    if pword == pword.upper(): #Needs one lower case character
        return False
    if pword == pword.translate(None, ")(*&^%$#@!~[]{}\|:;'?><.,/"):
        return False
    return True

def validate_phone(phone):
    # First, lets get all phone numbers in the same format. @Andrew--Shouldn't we return false if the number contains these characters?
    #phone = phone.translate(None, string.letters+"()#+!$%^&*_\|[]{}/.-")
    phone = phone.translate(None, "-+()");
    if phone == phone.translate(None, string.letters+"*&^%$#@!~[]{}\|:;'?><.,/=_"):
        return False
    return True


if __name__=="__main__":
    #suite = unittest.TestLoader().loadTestsFromTestCase(EmailValidator)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    app.debug=True
    app.run()
