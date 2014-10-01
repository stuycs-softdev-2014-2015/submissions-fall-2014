from flask import Flask, render_template,session,redirect

def check(func):
    def wrapper(*args):
        if 'username' in session:
            return func()
        else:
            return redirect('/login')
    return wrapper
    
