from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/data')
def data():
	code_dct = {
	'33':'Regular insulin dose',
	'34':'NPH insulin dose',
	'35':'UltraLente insulin dose',
	'48':'Unspecified blood glucose measurement',
	'57':'Unspecified blood glucose measurement',
	'58':'Pre-breakfast blood glucose measurement',
	'59':'Post-breakfast blood glucose measurement',
	'60':'Pre-lunch blood glucose measurement',
	'61':'Post-lunch blood glucose measurement',
	'62':'Pre-supper blood glucose measurement',
	'63':'Post-supper blood glucose measurement',
	'64':'Pre-snack blood glucose measurement',
	'65':'Hypoglycemic symptoms',
	'66':'Typical meal ingestion',
	'67':'More-than-usual meal ingestion',
	'68':'Less-than-usual meal ingestion',
	'69':'Typical exercise activity',
	'70':'More-than-usual exercise activity',
	'71':'Less-than-usual exercise activity',
	'72':'Unspecified special event'
	}
	
	base = 'Diabetes-Output/'
	code = '33'
	fname = base + 'data-fromated-'+code+'.csv'
	file_stream = open(fname)
	data =[];
	
	for line in file_stream:
		data.append(line.split(','))
	
	table_package = {
		'types':['month', 'day', 'year', 'time', 'value'],
		'data':data
	}
	description = "Welcome to the analysis."
	head = code_dct[code]
	return render_template("data.html", table_package=table_package, description=description, head=head)

if __name__ == '__main__':
  app.run(debug=True)
