import re

# one method that uses all other checking methods
def confirmation(username,password,email,name):  
    answer = "good"
    username_msg = username_confirmation(username)
    password_msg = password_confirmation(password)
    email_msg = email_confirmation(email)
    name_msg = name_confirmation(name)
    if username_msg != "valid":
        answer = username_msg
    if password_msg != "valid":
        answer = password_msg
    if email_msg != "valid":
        answer = email_msg
    if name_msg != "valid":
        answer = name_msg
    return answer

def username_confirmation(username):
    if re.match("((\w)|(\d)|[\.-_]){6,15}",username):
        return "valid"
    else:
        return "Sorry, this is not a valid username. Please only use letters, periods, underscores, and hyphens in your username. Usernames must be between 6 and 15 characters."


def password_confirmation(password):
    if re.match("([a-z]|\d+){6,15}",password):
        return "valid"
    else:
        return "Sorry, this is not a valid password. Please use only lowercase letters and numbers in your password. Passwords must be between 6 and 15 characters." 

def email_confirmation(email):
    if re.match("[a-z]+@[a-z]+\.[a-z]+",email):
        return "valid"
    else:
        return "Sorry, this is not a valid email. Please make sure you enter a real email."

def name_confirmation(name):
    if re.match("(\w|\s){6,15}",name):
        return "valid"
    else:
        return "Sorry, this is not a valid username. Please use only letters and spaces in your username. Usernames must be between 6 and 15 characters."














