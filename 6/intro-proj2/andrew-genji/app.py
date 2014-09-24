#from flask import flask, render_template
import unittest
import random
#import String
import EmailValidator

###############################
######## Intro-Proj 2 #########
### A. Fischer, G. Noguchi  ###
###############################

TLDList = open("TLDs.txt").readlines().lower()

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

    if TLD not in TLDList:    # Not a real TLD?
        return False          # Not a real email

    else:
        return True


def validate_password(pword):
    return True

def validate_phone(phone):
# First, lets get all phone numbers in the same format.
    phone = phone.translate(None, string.letters+"/.-")
    
    return True


if name=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(EmailValidator)
    unittest.TextTestRunner(verbosity=2).run(suite)
