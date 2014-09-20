from flask import Flask,render_template,request


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)
@app.route("/Analysis")
@app.route("/Analysis", methods = ['Post'])
def Analysis():
    return render_template("Analysis.html")
	
@app.route("/Compare")
@app.route("/Compare", methods = ['Post'])
@app.route("/Compare/<state1>/<state2>",methods = ['Post'])
def Compare():
	state1 = (request.args.get("state1"))
	state2 = (request.args.get("state2"))
	print(state1)
	return render_template("Compare.html",
							state1 = state1,
							state2 = state2)
							
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
