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

	table_pkg={
	'types': [
			'1', '2', '3',
		],

		'data': [
			['huh', 'yup', 'yeah'],
			['yes', 'whoop', 'hooray'],
			['no', 'nah', 'noop'],
			['random', 'words', 'here'],
			['just', 'testing', 'brah'],
		],
	}

	desc = "Welcome to the analysis."

        return render_template("data.html", table_package=table_pkg, 		description=desc)


if __name__ == '__main__':
    app.run(debug=True)
