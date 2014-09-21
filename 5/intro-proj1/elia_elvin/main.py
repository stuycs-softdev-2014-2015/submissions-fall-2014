from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/data')
def data():
	# Table package is a dictionary 
	# table_package['types'] is a list of table column headers (data types) in the order that they will appear
	# table_package['data'] is a two-dimensional list of row lists with data in them
	# table_package['data'][0] is a list of data

	# A short script or function will be needed to place necessary data in the correct data structures as defined above
	# Here's a fabricated one for the purposes of testing while the data-manipulating engine is being tweaked:
    tits = ['month', 'day', 'year', 'time', 'value']
    base = '/home/students/2014/elia.portnoy/Documents/Senoir/submissions/5/intro-proj1/elia_elvin/Diabetes-Output/'
    fname = base+'data-fromated-33.csv'
    in_file = open(fname,'r')
    data = []
    
    for line in in_file:
        s = line.split(',');
        data.append(s)
        print s
    
    
	table_pkg={
	'types': tits,
	'data': data
	}

	desc = "Welcome to the analysis."

        return render_template("data.html", table_package=table_pkg, 		description=desc)


if __name__ == '__main__':
    app.run(debug=True)
