from flask import Flask, render_template, request, abort
import utils
import collections

app = Flask(__name__)

@app.route('/data/')
@app.route('/data/<idnum>')
def data(idnum = None):
	# If an ID number was selected, display that data
	# Otherwise, data choice form page

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

	ordered_code_dict = collections.OrderedDict(sorted(code_dct.items()))

	if idnum:

		
		base = 'Diabetes-Output/'
		code = idnum
		fname = base + 'data-fromated-'+code+'.csv'
		try:
			file_stream = open(fname)
		except:
			abort(404)
		data =[];
		
		for line in file_stream:
			data.append(line.split(','))
		
		table_package = {
			'types':['Month', 'Day', 'Year', 'Time', 'Value'],
			'data':data
		}
		description = ""
		head = utils.headerify_string(code_dct[code])
		return render_template("data_table.html", table_package=table_package, description=description, head=head, id_num = idnum)
	else:
		# Simple GET request stuff handled via URL information passing
		return render_template("data_choice.html", selection_list=ordered_code_dict)

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.errorhandler(404)
def not_found(e): # Return rendering, 404
	return render_template('404.html'), 404

if __name__ == '__main__':
  app.run(debug=True)
