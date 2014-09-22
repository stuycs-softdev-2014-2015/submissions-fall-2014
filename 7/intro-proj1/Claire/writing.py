from flask import Flask, render_template, request

def writing(string):
    Q1 = request.form['Q1']
    Q2 = request.form['Q2']
    Q3 = request.form['Q3']
    Q4 = request.form['Q4']
    Q5 = request.form['Q5']
    t = s.split(" ")
    for n in t:
        if n == "Q1":
	    i = t.index(n)
            t[i] = Q1
        elif n == "Q2":
	    i = t.index(n)
            t[i] = Q2
        elif n == "Q3":
	    i = t.index(n)
            t[i] = Q3
        elif n == "Q4":
	    i = t.index(n)
            t[i] = Q4
        elif n == "Q5":
	    i = t.index(n)
            t[i] = Q5
    poem = " ".join(t)
    return poem
