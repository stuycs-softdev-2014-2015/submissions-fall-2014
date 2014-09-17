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
	page = "/"+answer+".html";
	return redirect(page)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/firewaterspd")
def firewaterspd:
	return render_template("firewaterspd")

@app.route("/grassgroundatk")
def grassgroundatk:
	return render_template("grassgroundatk")

#1:30 AM right now, too tired to copy paste rest of these pages
#Now we need to copy paste these, just put the graphs on those pages and put the (already done) CSS on them
#The background image + CSS + redirecting is all done

  <option value="grassnormalhp">Grass vs. Normal (HP)</option>
  <option value="groundelectricdef">Ground vs. Electric (Defense)</option>
  <option value="dragonicehp">Dragon vs. Ice (HP)</option>
  <option value="darksteelspatk">Dark vs. Steel (Special Attack)</option>
  <option value="ghostpsychicspdef">Ghost vs. Psychic (Special Defense)</option>
  <option value="firenormalspd">Fire vs. Normal (Speed)</option>
  <option value="watergrounddef">Water vs. Ground (Defense)</option>
  <option value="steelelectrichp">Steel vs. Electric (HP)</option>
  <option value="rockgroundspatk">Rock vs. Ground (Special Attack)</option>
  <option value="flyingghostdef">Flying vs. Ghost (Defense)</option>
  <option value="flyingwateratk"

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6734)
