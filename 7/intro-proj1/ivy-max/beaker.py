from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("carbon.html")

@app.route("/data/", methods=['POST'])
def data():
    str = ''
    form = request.form
<<<<<<< HEAD
    setup()
    rundata()
    return "UH"

def setup():
    global locus, duplicates
    global data, restriction, data1, data2
    s = ''
    f=open('data.csv')
    raw_data = f.read().split('\n')
    data = [] #IM TIRED OKAY D:
=======
    print form
    setup(form)
    #rundata() #gives an error
    return "Submitted"

def setup(form):
    data = []
    f=open('data.csv')
    raw_data = f.read().split('\n')
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    for x in raw_data:
        data.append(x.split(',')) 
    print "test"
        
<<<<<<< HEAD
    country1 = request.form['country1']
    country2 = request.form['country2']
    duplicates = False
    if country1 == country2:
        duplicates = True
    headers = {'Total fossil fuels':2, 'Solid fuel consumption':3, 'Liquid fuel consumption':4, 'Gas fuel consumption':5, 'Cement production':6, 'Gas flaring':7,'Per capita CO2':8, 'Bunker fuels':9} #Call headers[header] to get position in data
    print "test2"
        
    #s+= countries(country2)
    data1 = countries(country1)[::-1] #defaults to reverse chronological order
    if not duplicates: 
        data2 = countries(country2)[::-1] 
    print "test3"
=======
    country1 = form.get('country1')
    country2 = form.get('country2')
    #print country1
    #print country2
    
    duplicates = False
    if country1 == country2:
        duplicates = True
        headers = {'Total fossil fuels':2, 'Solid fuel consumption':3, 'Liquid fuel consumption':4, 'Gas fuel consumption':5, 'Cement production':6, 'Gas flaring':7,'Per capita CO2':8, 'Bunker fuels':9} #Call headers[header] to get position in data
    #print countries(country2)
    data1 = countries(country1, data)[::-1] #defaults to reverse chronological order
    #print data1
    if not duplicates: 
        data2 = countries(country2, data)[::-1]
        #print data2
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    locus = 2
    print request.form['typeofemission']
    print headers['Gas fuel consumption']
    try:
<<<<<<< HEAD
        print "trying..."
        restriction = request.form['typeofemission']
=======
        restriction = form.get('typeofemission')
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
        locus = headers[restriction]
    except: #Sort by year.
        print "failing..."
        restriction = 'Total fossil fuels'
<<<<<<< HEAD
        locus = 2 #default to Total fossil fuels

    print locus
    return s #oops this doesn't return anything.


def countries(country):
    print "test2.5"
=======
        #locus = 1 #default to Total fossil fuels
    print "bloop"

def countries(country, data):
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    tempdata = []
    for element in data:
        if element[0] == country:
            #print element
            tempdata.append(element)
    print "test2.6"
    return tempdata
 
<<<<<<< HEAD
def restrict(ilist):
    print "restrict"
=======
def restrict(ilist, form):
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    global restriction
    #global locus
    new = []
    yearholder = ''
    try:
<<<<<<< HEAD
        years = request.form['range']
=======
        years = form.get('range')
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
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


    #print ilist
    for line in ilist:
        #print repr(int(line[1]))
        #print int(line[1]) in yearrange
        #print line
        #print locus
        if int(line[1]) in yearrange:
            minilist = [line[0], line[locus], line[1]]
            new.append(minilist)
        #print line
    print "NEW!"
    return new
<<<<<<< HEAD




def sorter():
    print 'sorter'
    global finalcdata
    #print restrict(data1)
    country1d = restrict(data1)
    print 'yay?'
    if not duplicates: country2d = restrict(data2)
=======
    
def sorter():
    global finalcdata
    final = []
    print "what" 
    #print restrict(data1)
    #restrict isn't working properly
    country1d = restrict(data1, form)
    print "restricted"
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    if not duplicates: 
        country2d = restrict(data2, form) 
        finalcdata = country1d + country2d
<<<<<<< HEAD
    else: finalcdata = country1d
        

    print duplicates
=======
    else: 
        finalcdata = country1d
    print "alwkgjw"

>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    try:
        isyears = form.get('isyears')
    except:
        isyears = 'no' #SWITCH BACK TO NO

<<<<<<< HEAD
    final = []
=======
>>>>>>> 20781f1a15d777a2b2d70f636b1ccea5aed7b9d0
    if isyears == 'yes':
        final = sorted(finalcdata, key=lambda x: float(x[2]))[::-1] #both countries, year only!
    if isyears == 'no':
        final = sorted(finalcdata, key=lambda x: float(x[1]))[::-1]
    return final

def rundata():
    print 'rundata'
    finalcdata = sorter()
    unit = ''
    if restriction == 'Per capita CO2':
        unit = ', metric tons of carbon'
        print "IF!"
    else:
        print "ELSE!"
        unit = ', thousand metric tons of carbon'
        
       # countrycolors = {
       #     country1: 'LightSkyBlue',
       #     country2: 'SpringGreen'
       #     
       # }
        print finalcdata
        print '<center>'
        # table = HTML.table(finalcdata,
        #   header_row=['Country', restriction + unit, 'Year'])
        table = HTML.Table(header_row=['Country', restriction + unit, 'Year'])
        for x in finalcdata:
            color = countrycolors[x[0]]
            colored_country = HTML.TableCell(x[0], bgcolor=color)
            colored_result = HTML.TableCell(x[1], bgcolor=color)
            colored_year = HTML.TableCell(x[2], bgcolor=color)
            table.rows.append([colored_country, colored_result, colored_year])
            print table
            print '</center>'

if __name__ == '__main__':
    app.debug == True
    app.run()
