from flask import Flask, render_template
import cgi,cgitb
cgitb.enable()
fD=cgi.FieldStorage()

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('data')
#def data():
	

if __name__=='__main__':
	app.debug=True
	app.run()
