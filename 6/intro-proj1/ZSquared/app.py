from flask import Flask, render_template
import random
app = Flask(__name__)
i1=random.random()
i2=random.random()
@app.route('/')
def home(var1=None,var2=None,var3=None):
        var1=random.random()
        var2=random.random()
        var3='href=other'
	return render_template('home.html',var1=var1, var2=var2, var3=var3)

@app.route('/other')
def other():
        return "<h1>This is a new page!<h1>"

if __name__=="__main__":
	
        app.debug=True
	app.run()
