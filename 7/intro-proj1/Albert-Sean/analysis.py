from flask import Flask, render_template, request

app = Flask(__name__)

def school_data():
	#read data
	f = open("static/SAT__College_Board__2010_School_Level_Results.csv")
	s = f.read()
	f.close()

	s = s.split("\n")
	del s[len(s) - 1]
	
	#remove schools without data; schools without data have ",s" as the score
	i = 0
	while (i < len(s)):
		if (",s" in s[i]):
			s[i] = ""
		s[i] = s[i].replace(" ,", ",")
		i += 1
	while ("" in s):
		s.remove("") #don't know why "del s[i]" doesn't work

	i = 0
	while (i < len(s)):
		s[i] = s[i].split(",")
		i += 1

	#remove schools with commas in their names; they create quirks in the table. It's only 6 six schools anyway.
	i = 0
	while (i < len(s)):
		if (len(s[i]) > 6):
			del s[i]
		i += 1
	
	return s

@app.route("/")
def analysis():
	return render_template("analysis.html", s = school_data())

@app.route("/compare")
def compare():
	if (request.args.get("schools", None) == None):
		school_list = []
		numbers = []
		x = 0
		for school in school_data()[1:]:
			school_list.append(school[1])
			numbers.append(x)
			x += 1
		return render_template("compare.html", length = numbers, schools = school_list)
	else:
		schools_selected = request.args.get("schools", None)
		return "fuck you"
	
if __name__ == '__main__':
    app.run(debug = True)
