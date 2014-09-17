#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

## TEAM BresnaChen
## MEMBERS: Leslie Bresnahan, Shirley Chen
## MKS22-01

## HW25
##
## DATASET: Electric Consumption by Zip Codes 2010
## DATA SOURCE: NYC open data
## We chose this because it was a clear table that was easy to understand and it had interesting facts as well.
## Our table showed the electric consumption by each zip code in the year 2010 and it was easy to interpret and notice
## trends in this table. The table showed each zip code, the building type(service class), the consumption of each in
## (kWh) and (GJ) as well as the utility/data source of the electricity. One trend we noticed was how the building types
## and service class of the electricity was grouped together and shared similar, consecutive zip codes with each other.
    
HEADING = "By Leslie Bresnahan and Shirley Chen  MKS22-01  <br> <br>  Our table showed the electric consumption by each zip code in the year 2010. During that year, New York state was found to be the eigth largest energy consumer in the United States. With New York City alone having a population of 8 million, and its many industries and transportation systems, we didnt find this to be surprising. We wanted to compare where the majority of energy was being consumed in, whether it was used in homes or by large corporations.  We chose this because it was a clear table that was easy to understand and it contained useful facts to help us figure out what we were looking for as well. The table showed each zip code, the building type(service class), the consumption of each in (kWh) and (GJ) as well as the utility/data source of the electricity. The table was ordered by its building type, making it easy to interpret data and compare the zip codes and the building services to their consumptions of electricity. An obstacle we encountered was the fact that within our cells there were line breaks, so this caused python to split the data there as well, so we wrote helper functions to change these unwanted line breaks into dashes instead."
# we had an issue where there were line breaks within the cells, so this was confusing for splitting the data by row

def removeLineBr(a):
    pos = 0
    data = a[:]
    amount = data.count('(')
    while pos <= amount:
        a = data.find('(')
        data = data[: (a - 1)] + '-' + data[a:]
        data = data[: a] + '^' + data[a + 1:]
        pos += 1
    data = data.replace('^', '(')
    data = data[:126239]          # the above function makes 2 copies and chops off the last letter, so i sliced the string in half and added on the y, i also could have added a[-1]
    return data
 

inStream = open("data_hw252.csv", 'r')           # set up inStream to store data from data_hw25.csv, into data
data = inStream.read()
inStream.close()
data = removeLineBr(data)
lines = data.split("\n")                        # split data at line break to separate by row
html = '''<html> \n <body bgcolor= "#ffe4c4"> <title> Hw25 data </title> <img src="http://classroomclipart.com/images/gallery/Animations/lightbulb.gif" alt="lightbulb" align="left" height="100" width="80">  </title> <img src="http://classroomclipart.com/images/gallery/Animations/lightbulb.gif" alt="lightbulb" align="right" height="100" width="80"> <br> <h1> <center> <font color ="#800000">  Electric Consumption by Zip Codes 2010 </font> </h1> <br> <center>''' + str(HEADING) + '<br> <br> <table align=""center"" border="1">
 \n '      # sets up top of pg
for line in lines:                              # for each line within the list of lines, you need to set up the rows
    if lines.index(line) == 0:
        lineList = line.split(',')
        html += '<tr style="font-size:18px;font-weight: bold" >'  # new row
    else:
        lineList = line.split(',')
        html += '<tr>'
    for cell in lineList:                       # to make cells within the rows
        html += "<td>" + cell + "</td>"
    html += "</tr> \n"                          # close the row tag
html += "\n </table>"                # close all the tags
html += "<br> <br> <h2> Sources </h2>  All data from: <a href='https://nycopendata.socrata.com/Environmental-Sustainability/Electric-Consumption-by-ZIP-Code-2010/74cu-ncm4'> Nycopendata </a> <br> NYC Open Data. N.p., n.d. Web. 25 Apr. 2013."
html += "<br><br><br> <br> For Further Analysis, click : <a href='http://lisa.stuy.edu/~leslie.bresnahan/analysis01.py'> HERE </a> "
html += "</html> "
print html
