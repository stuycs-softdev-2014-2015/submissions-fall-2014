from flask import Flask,render_template,request,redirect
# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result", methods=['POST'])
def result():
	answer = request.form['option']
	page = "/"+answer;
	return redirect(page)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/firewaterspd")
def firewaterspd():
	return render_template("firewaterspd.html")

@app.route("/grassgroundatk")
def grassgroundatk():
	return render_template("grassgroundatk.html")

@app.route("/grassnormalhp")
def grassnormalhp():
  return render_template("grassnormalhp.html")

@app.route("/groundelectricdef")
def groundelectricdef():
  return render_template("groundelectricdef.html")

@app.route("/dragonicehp")
def dragonicehp():
  return render_template("dragonicehp.html")

@app.route("/darksteelspatk")
def darksteelspatk():
  return render_template("darksteelspatk.html")

@app.route("/ghostpsychicspdef")
def ghostpsychicspdef():
  return render_template("ghostpsychicspdef.html")

@app.route("/firenormalspd")
def firenormalspd():
  return render_template("firenormalspd.html")

@app.route("/watergrounddef")
def watergrounddef():
  return render_template("watergrounddef.html")

@app.route("/steelelectrichp")
def steelelectrichp():
  return render_template("steelelectrichp.html")

@app.route("/rockgroundspatk")
def rockgroundspatk():
  return render_template("rockgroundspatk.html")

@app.route("/flyingghostdef")
def flyingghostdef():
  return render_template("flyingghostdef.html")

@app.route("/flyingwateratk")
def flyingwateratk():
  return render_template("flyingwateratk.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6734)
