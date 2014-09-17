from flask import Flask, render_template

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/<sortby>")
def sort(sortby=None):
	return render_template("order.html",sortby=sortby)

@app.route("/")
@app.route("/<sortby>/<order>")
def main(sortby=None, order=None):
	#!/usr/bin/python
	print 'Content-Type: text/html'
	print

	htmlout = render_template("main1.html")
	#OPEN FILE
	dow = open ('DJIA.csv','r')
	header = dow.readline()
	dow = dow.readlines()

	import cgi,cgitb
	cgitb.enable()
	form=cgi.FieldStorage()
	
	#PRICE LIST
	price = []
	for item in dow:
	    price.append(float(item.strip('\r\n').split(',')[1]))

	#MOVING AVERAGE CALCULATION
	ma10 = []
	for x in range(0,10):
	    ma10.append(0)
	for x in range(10,len(price)):
	    ma10.append(sum(price[x-10:x])/len(price[x-10:x]))

	ma15 = []
	for x in range(0,15):
	    ma15.append(0)
	for x in range(15,len(price)):
	    ma15.append(sum(price[x-15:x])/len(price[x-15:x]))

	count=[]
	x=0
	for item in price:
	    if ma10[x] >= ma15[x]:
	        count.append(x)
	    x+=1

	#CHANGE, %CHANGE CALCULATION
	change = []
	changeP = []
	change.append(0)
	changeP.append(0)
	for x in range(1,len(price)):
	    change.append(price[x] - price[x - 1])
	    changeP.append((price[x] - price[x - 1])/(price[x-1])*100)

	#RELATIVE STRENGTH INDEX CALCULATION
	rsi10 = []
	rsi = 0
	rs = 0
	for x in range(0,10):
	    rsi10.append(50)
	for x in range(10,len(price)):
	    g = 0
	    nu = 0
	    l = 0
	    nd = 0
	    for chg in change[x-10:x]:
	        if chg >= 0:
	            nu += 1
	            g += chg
	        else:
	            nd+= 1
	            l += -1 * chg
	    rs = (g / (nu+0.0000000000000000001)) / (l / (nd+0.0000000000000001)+0.0000000000000000001)
	    rsi10.append(100-(100/(1+rs)))
	    
	htmlout += render_template("main2.html")
	
	start = -1
	end=-100
	num = 0

	newlist = dow[start:end:-1]
	newlist2 = []
	x=0
	for item in newlist:
	    newlist2.append(item.replace('\r\n','') +',' + str(change[-x-1])+',' + str(changeP[-x-1])+',' + str(ma10[-x-1])+',' + str(ma15[-x-1])+',' + str(rsi10[-x-1]))
	    x+=1
    
	if sortby:
	    if sortby == 'price':
	        newlist2= sorted(newlist2,key=lambda item: float(item.split(',')[1]))
	        newlist2.reverse()
	        htmlout += '<p>Sort by <u>price</u> '
	    elif sortby == 'pct':
			newlist2=sorted(newlist2,key=lambda item: float(item.split(',')[3]))
			newlist2.reverse()
			htmlout += '<p>Sort by <u>% change</u> '
	    else:
	        htmlout += '<p>Sort by <u>date</u> '

	if order:
	    if order == 'inc':
	        newlist2.reverse()
	        htmlout += 'in <u>ascending</u> order</p>'
	    else:
	        htmlout += 'in <u>descending</u> order</p>'
        
	#HTML DATA TABLE

	if "page" not in form:
		page = 0
	else:
	    page = int(form['page'].value)

	if "per" not in form:
	    per=50
	else:
	    per=int(form['per'].value)
    
	diff = start - end
	extra = 0
	pages = diff / per + 1
	if page == pages - 1:
	    extra = abs(diff - (pages * per))
	htmlout += '<u>' + str(diff) + '</u> values returned. (default - 9)<br>'
	htmlout += '<u>' + str(per) + '</u> entries per page. (default - 50)<br><br>'
	htmlout += 'Pages: &nbsp;'
	for x in range(pages):
	    htmlout += '<a href="project.py?page=' + str(x)
	    if "year" in form:
	            htmlout += '&year='+form['year'].value
	    if "per" in form:
	            htmlout += '&per='+form['per'].value
	    htmlout += '">' + str(x) + '</a>&nbsp;'

	htmlout += '<br><table border=1><tr><th>' + header.split(',')[0] + '</th><th>' + header.strip('\r\n').split(',')[1] + '</th><th>Change</th><th>% Change</th><th>MA-10</th><th>MA-15</th><th>RSI-10</th></tr>'
    
	x=0
	for item in newlist2:
	    out = ''
	    out += '<tr><td>'
	    out += newlist2[x].split(',')[0]
	    out += '</td><td>'
	    out += str(round(float(newlist2[x].split(',')[1]),2))
	    out += '</td><td>'
	    if float(newlist2[x].split(',')[2])>0:
	        out += '<div style="color:green">'
	    elif float(newlist2[x].split(',')[2])<0:
	        out += '<div style="color:red">'
	    out += str(round(float(newlist2[x].split(',')[2]),2))
	    out += '</td><td>'
	    out += str(round(float(newlist2[x].split(',')[3]),2))
	    out += '</td></div><td>'
	    out += str(round(float(newlist2[x].split(',')[4]),2))
	    out += '</td><td>'
	    out += str(round(float(newlist2[x].split(',')[5]),2))
	    out += '</td><td>'
	    out += str(round(float(newlist2[x].split(',')[6]),2))
	    out +='</td></tr>'
	    x+=1
	    htmlout += out

	htmlout += '''
	</table>
	</div>
	'''
	
	#------ANALYSIS--------
	
	htmlout += '''
	<hr>
	<a id='analysis'>
	<div style="font-family:'Century Gothic,Helvetica',Arial;">
	<h3> Analysis</h3>
	<ul><li>A shorter-term MA > longer-term MA is a BULLISH (positive) sign.</li>
		<li>An RSI > 50 is a BULLISH (positive) sign.</li>
	</ul>
	<p>Data from just the last 1000 days alone is also used as the results are more favorable in conditions of higher volatility.</p>
	<p>The main difficulty lies in comparing moving averages and finding a corresponding price change to them.</p>
	'''
	
	htmlout += '<table border = 1><tr><th>Condition</th><th>Bullish/Bearish</th><th>Days When Condition Met</th><th>Days Up</th><th>% Up</th><th>Avg Up</th><th>Days Down</th><th>% Down</th><th>Avg Down</th></tr>'
	htmlout += '<tr><td>All Days</td><td>Regular</td><td>'
	htmlout += str(len(price))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in range(len(price)):
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(price)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in range(len(price)):
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(price)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	htmlout += '<tr><td>Short term MA > Longer term MA</td><td>Bullish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	count=[]
	x=0
	for item in price:
		if ma10[x] < ma15[x]:
			count.append(x)
		x+=1
	
	htmlout += '<tr><td>Short term MA < Longer term MA</td><td>Bearish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	count=[]
	x=0
	for item in price:
		if rsi10[x] < 70 and rsi10[x] > 60:
			count.append(x)
		x+=1
		
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += '<tr><td>60 < RSI10 < 70</td><td>Bullish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	count=[]
	x=0
	for item in price:
		if rsi10[x] < 40 and rsi10[x] > 30:
			count.append(x)
		x+=1
		
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += '<tr><td>30 < RSI10 < 40</td><td>Bearish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	
		
	htmlout += '</table>'
	############
	
	count=[]
	x=0
	for item in price[-1000:-1:1]:
		if ma10[x] >= ma15[x]:
			count.append(x)
		x+=1
		
	htmlout += '<h3>Using the last 1000 days: </h3>'
	
	htmlout += '<table border = 1><tr><th>Condition</th><th>Bullish/Bearish</th><th>Days When Condition Met</th><th>Days Up</th><th>% Up</th><th>Avg Up</th><th>Days Down</th><th>% Down</th><th>Avg Down</th></tr>'
	htmlout += '<tr><td>All Days</td><td>Regular</td><td>'
	htmlout += str(1000)
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in range(len(price[-1000:-1:1])):
		if change[-1*item] > 0:
			y += 1
			z += changeP[-1*item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(price[-1000:-1:1])) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in range(len(price[-1000:-1:1])):
		if change[-1*item] < 0:
			y +=1
			z += changeP[-1*item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(price[-1000:-1:1])) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	htmlout += '<tr><td>Short term MA > Longer term MA</td><td>Bullish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	count=[]
	x=0
	for item in price[-1000:-1:1]:
		if ma10[x] < ma15[x]:
			count.append(x)
		x+=1
	
	htmlout += '<tr><td>Short term MA < Longer term MA</td><td>Bearish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	count=[]
	x=0
	for item in price[-1000:-1:1]:
		if rsi10[x] < 70 and rsi10[x] > 60:
			count.append(x)
		x+=1
		
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += '<tr><td>60 < RSI10 < 70</td><td>Bullish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	count=[]
	x=0
	for item in price[-1000:-1:1]:
		if rsi10[x] < 40 and rsi10[x] > 30:
			count.append(x)
		x+=1
		
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += '<tr><td>30 < RSI10 < 40</td><td>Bearish</td><td>'
	htmlout += str(len(count))
	htmlout += '</td><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] > 0:
			y += 1
			z += changeP[item]
	
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=green>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font><td>'
	
	y = 0
	z = 0.0
	for item in count:
		if change[item] < 0:
			y +=1
			z += changeP[item]
	z = z / y
	
	htmlout += str(y)
	htmlout += '</td><td><font color=red>'
	htmlout += str(round((y*1.0/len(count)) * 100,2))
	htmlout += '</td><td>'
	htmlout += str(round(z,2))
	htmlout += '</td></font></tr>'
	
	
		
	htmlout += '</table>'
	
	
	htmlout += '''
	<p>The results in the first table generally prove that <b>bullish signs are more likely than normal (52.25%) to have up days (rows 2,4)</b>.  However, the magnitude of price change is not affected.  This is also seen in the bearish signals as well, having lower % of up days.  While I originally believed the higher volatility in the second chart would be more favorable towards the results, the result was actually the opposite of what was proved in table 1.</p>
	</div>
	'''
	
	htmlout += '''
	</body>
	</html>
	'''
	
		
	return htmlout
'''
@app.route("/random")
def randompage():
    import random
    num = random.randrange(0,100)
    l = [111,222,333,444]
    d = {'a':100,'hello':'HeLLo',3:'world'}
    
    return render_template("random.html",
                           num=num,
                           name="Thluffy",
                           l=l,
                           d=d)
'''

if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()