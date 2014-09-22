from flask import Flask,render_template,request


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

def retrieve(State):
	f = open('Static/Data.txt', 'r')
	s = f.readlines()
	f.close
	print(s[0])
	i = 0
	while (i < len(s)):
		s[i] = s[i].split(',')
		print(s[i])
		i+=1
	i = 0
	while(i < len(s)):
		if (s[i][0].strip() == State):
			return s[i][1:]
		i+=1

def greatest(State1,s1, State2,s2):
	s = []
	i = 0
	while (i < len(s1)):
		if (s1[i] > s2[i]):
			s.append(State1)
		else:
			s.append(State2)
		i+=1
	return s
	
app = Flask(__name__)
@app.route("/Analysis")
@app.route("/Analysis", methods = ['Post'])
def Analysis():
    return render_template("Analysis.html")
	
@app.route("/Compare")
@app.route("/Compare", methods = ['Post','GET'])
@app.route("/Compare/<state1>/<state2>",methods = ['Post', 'GET'])
def Compare():
	state1 = request.form["state1"]
	state2 = request.form["state2"]
	s1 = retrieve(state1)
	s2 = retrieve(state2)
	s = greatest(state1, s1, state2, s2)
	return render_template("Compare.html",
							state1 = state1,
							state2 = state2,
							s1 = s1, 
							s2 = s2,
							s = s)
							
@app.route("/Data")
@app.route("/Data", methods = ['Post'])
def data():
    return render_template("Data.html")

@app.route("/home")
@app.route("/home", methods = ['Post'])
@app.route("/Index")
@app.route("/")
def home():
    return render_template("Index.html")

if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
