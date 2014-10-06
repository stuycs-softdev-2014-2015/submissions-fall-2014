from flask import Flask,render_template,request


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

def greatest(s1, s2):
	s = ['Result']
	i = 1
	while (i < len(s1)):
		if (s1[i] > s2[i]):
			s.append(s1[0])
		else:
			s.append(s2[0])
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
        s1 = request.form["state1"]
        s2 = request.form["state2"]
        sa=[]
        sb=[]
        if(s1==None):
                s1='NY'
        if(s2==None):
                s2='CA'
        if(s1==s2):
                s2='NY'
                if(s1==s2):
                        s2='NJ'
        f=open('static/Data.txt','r')
        s = f.readlines()
        f.close
        i = 0
        while i < len(s):
                s[i]=s[i].split(',')
                i+=1
        for a in s:
                if(a[0]==s1):
                        for x in a[1:2]+a[4:]:
                                sa.append(x)
                elif(a[0]==s2):
                        for x in a[1:2]+a[4:]:
                                sb.append(x)
        s3=greatest(sa,sb)
        return render_template("Compare.html",
                               state1 = sa,
                               state2 = sb,
                               greatest=s3)
        
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
