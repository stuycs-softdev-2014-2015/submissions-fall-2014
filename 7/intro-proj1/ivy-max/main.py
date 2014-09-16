#!/usr/bin/python
print 'Content-type: text/html\n'
import HTML, cgi, cgitb, re
#from denis import *
cgitb.enable()

form = cgi.FieldStorage()
f=open('data.csv')
raw_data = f.read().split('\n')
data = []
for x in raw_data:
	data.append(x.split(','))


country1 = form['country1'].value
country2 = form['country2'].value

duplicates = False
if country1 == country2:
	duplicates = True
headers = {'Total fossil fuels':2, 'Solid fuel consumption':3, 'Liquid fuel consumption':4, 'Gas fuel consumption':5, 
'Cement production':6, 'Gas flaring':7,'Per capita CO2':8, 'Bunker fuels':9} #Call headers[header] to get position in data

def countries(country):
	tempdata = []
	for element in data:
		if element[0] == country:
			#print element
			tempdata.append(element)
	return tempdata
#print countries(country2)
data1 = countries(country1)[::-1] #defaults to reverse chronological order
if not duplicates: data2 = countries(country2)[::-1]

locus = 2
try:
	restriction = form['typeofemission'].value
	locus = headers[restriction]
except: #Sort by year.
	restriction = 'Total fossil fuels'
	#locus = 1 #default to Total fossil fuels

def restrict(ilist):
	global restriction
	global locus
	new = []
	yearholder = ''
	try:
		years = form['range'].value
		years = re.sub(r'[^0-9\-]', '', years).split('-')
		if len(years) != 2:
			raise Exception("I don't want to deal with people typing this in wrong, just shortcut to the except.")
		if int(years[1]) < int(years[0]): #2000, 1995.  1995 < 2000.  Fine, I'll fix -this- for them.
			yearholder = years[1] #yearholder > 1995
			years[1] = years[0] #2000, 2000
			years[0] = yearholder #1995, 2000
			

	except:
		years = ['0', '2050'] #Essentially, all years
	yearrange = range(int(years[0]), int(years[1])+1)

	for line in ilist:
		#print repr(int(line[1]))
		#print int(line[1]) in yearrange
		#print line
		if int(line[1]) in yearrange:
			minilist = [line[0], line[locus], line[1]]
			new.append(minilist)
	return new
#print restrict(data1)
country1d = restrict(data1)
if not duplicates: country2d = restrict(data2)
if not duplicates: 
	finalcdata = country1d + country2d
else: finalcdata = country1d

try:
	isyears = form['isyears'].value
except:

	isyears = 'no' #SWITCH BACK TO NO
def sorter():
	global finalcdata
	final = []
	if isyears == 'yes':
		final = sorted(finalcdata, key=lambda x: float(x[2]))[::-1] #both countries, year only!
	if isyears == 'no':
		final = sorted(finalcdata, key=lambda x: float(x[1]))[::-1]
	return final

finalcdata = sorter()

unit = ''
if restriction == 'Per capita CO2':
	unit = ', metric tons of carbon'
else:
	unit = ', thousand metric tons of carbon'



countrycolors = {
        country1: 'LightSkyBlue',
        country2: 'SpringGreen'

    }

print '<center>'
# table = HTML.table(finalcdata,
# 	header_row=['Country', restriction + unit, 'Year'])
table = HTML.Table(header_row=['Country', restriction + unit, 'Year'])
for x in finalcdata:
	color = countrycolors[x[0]]
	colored_country = HTML.TableCell(x[0], bgcolor=color)
	colored_result = HTML.TableCell(x[1], bgcolor=color)
	colored_year = HTML.TableCell(x[2], bgcolor=color)
	table.rows.append([colored_country, colored_result, colored_year])
print table
print '</center>'