from flask import Flask, render_template, request
from collections import OrderedDict
import coder

app = Flask (__name__)
nav = OrderedDict()
nav['index'] = '/'
nav['about'] = '/about'
nav['data'] = '/table'
nav['input'] = '/input'

@app.route ("/")
def home () :
	return render_template ("index.html", nav = nav)

@app.route ("/table")
# def table ():
#     s = "<table>"
#     data = open ("Lincoln_Square_BID_Business_List.csv", "r")
#     t = data.readline().split(',')
#     for b in t:
#         s = s + "<th>" + b + "</th>"
#     data.readline()
#     for line in data:
#         s = s + "<tr>"
#         t = line.split(',')
#         for b in t:
#             s = s + "<td>" + b + "</td>"
#         s = s + "</tr>"
#     data.close()
#     s = s + "</table>" 
#     return render_template("data.html", nav = nav)%s
def table():
	data = open ("Lincoln_Square_BID_Business_List.csv", "r")
	headers = data.readline().split(',')
	data.readline()
	rows = []
	for line in data:
		rows.append(line.split(','))
	data.close()
	return render_template("table.html", nav = nav, headers = headers, rows = rows)


@app.route("/input")
def input ():
	input = request.args.get ("input", None)
	button = request.args.get ("button", None)
	if button == None:
		return render_template ("input.html", nav = nav)
	elif button == "Codify!":
		return render_template("results.html", nav = nav)%coder.codify(input)
	elif button == "Decodify!":
		return render_template("results.html", nav = nav)%coder.decodify(input)

@app.route("/about")
def about():
	return render_template("about.html", nav = nav)

if __name__ == "__main__":
	app.debug = True
	app.run()
