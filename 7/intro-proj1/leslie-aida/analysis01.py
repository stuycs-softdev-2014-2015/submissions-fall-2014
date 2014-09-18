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
CONCLUSION = "Overall, we noticed that many zip codes were repeated meaning that they had multiple building types in that region. Although it was in the same zip code, depending on the building type, there was a huge difference in consumption within the same area. We noticed that the consumption of electricity for commercial service classes was the greatest out of the 4 different types. It was almost 7 times as much as large residentials in kWh and almost 5 times as much in GJ. It almost had the largest range of consumption as well, ranging from 0.0 - 1469718951.0 in kWh and 0.0 - 5290988.0 in GJ. One of our greatest obstacles was trying to generate a table within python instead of creating another csv file and opening it like we did with data01. It was also difficult to not only find average of numbers in column, but to also separate the numbers based on category and then find individual averages for each gorup.  Our massive data set also made it difficult to toruble shoot and really figure out what was going on,  we we created an extra, short data set to use while writing code."

# we had an issue where there were line breaks within the cells, so this was confusing for splitting the data by row
def removeLineBr(a):
    pos = 0
    data = a[:]                 # copy of orig string
    amount = data.count('(')        
    while pos <= amount:        # you have to do this once for each C
        a = data.find('(')
        data = data[: (a - 1)] + '-' + data[a:]     # will slice off data before the ( and put a - inbetween
        data = data[: a] + '^' + data[a + 1:]       # replace the ( temporarily so that you can keep moving down the string
        pos += 1
    data = data.replace('^', '(')   # then convert those placeholder ^s with C
    data = data[:126239]           # the above function makes 2 copies and chops off the last letter, so i sliced the string in half and added on the y, i also could have added a[-1]
    return data

# we had seprate groups of data within our massive data, so we had to split up so of the averaging and such by switching "target:

def findzipRange(lines, target, location):          # set up code to run through a column of our data for zip codes, then find the range
    rangelista = []
    for line in lines:                              # every line where the target is there, like range for small or commercial etc
        if line.count(target) > 0:
            rangelista.append( (line[1:])[:5])      # appends that data to a big mother list of all the zip codes
    rangelist = [min(rangelista)] + [max(rangelista)]   # for range we just need max and min
    rangelist = "-".join(rangelist)
    return rangelist

def zipReplace(lines, target, location, zipRange):      # now that we figured out range, we can go back and put it in the table
    for line in lines:
        if line.count(target) > 0:                      
            newline = line.split(',')                   # split the line into a list
            newline[location] = str(zipRange)           # use index bc its like column
            newline = ','.join(newline)
            lines[ lines.index(line) ] = newline
    return lines

def moreRange(lines, target, location):
    rangelista = []
    for line in lines:
        if line.count(target) > 0:                      # this is to add up all of the data in each  data type appeared
            newline = line.split(',')
            rangelista.append( float(newline[location]) )
    rangelist = [ str(min(rangelista))] + [ str(max(rangelista))]   # then this finds range
    rangelist = " - ".join(rangelist)
    return rangelist
      
def ReplaceRange(lines, target, location1, location2, rangeKWH, rangeGJ):
    for line in lines:
        if line.count(target)>0:
            newline = line.split(',')
            newline[location1] = str(rangeKWH)                      # now that we know the ranges, we enter them into the string to replace where the averages were
            newline[location2] = str(rangeGJ)
            newline = ','.join(newline)
            lines[lines.index(line)] = newline
    return lines

def findrange(lines,target):
    rangelista = []
    for line in lines:                                      # to separate the data types, use this , it will give you a list of the lowest andhighest indexes, so now you have a range
        if line.count(target) > 0:
            rangelista.append(lines.index(line))
    rangelist = [min(rangelista)] + [max(rangelista)] 
    return rangelist 

def findaverage(lines, Range, location):
    mini = Range[0]
    maxi = Range[1]
    dataSet = []
    for line in lines:
        if lines.index(line) >= mini and lines.index(line) <= maxi:         # this averages all of the values in a column based ont he fanges found
            newline = line.split(',')
            dataSet.append( float( newline[location]) )
    listsum = sum(dataSet)
    listlength = len(dataSet)
    average = listsum / listlength
    average
    return average

def replaceaverage(lines, Range, location, location2):          # once you find the averages you need too enter them, 2 per column
    mini = Range[0]
    maxi = Range[1]
    average = findaverage(lines, Range, location)
    average2 = findaverage(lines, Range, location2)
    for line in lines:
        if lines.index(line) == mini:
            newline = line.split(',')
            newline[location] = str(average)                # turns first values into the new values
            newline[location2] = str(average2)
            newline = ','.join(newline)
    lines[mini] = newline
    del lines[ (mini + 1) : (maxi + 1)]                     # deletes the rest of that section
    return lines
    

inStream = open("data_hw252.csv", 'r')           # set up inStream to store data from data_hw25.csv, into data
data = inStream.read()
inStream.close()
data = removeLineBr(data)
lines = data.split("\n")                        # split data at line break to separate by row
html = '''<html> \n <body bgcolor= "#ffe4c4"> <title> Hw25 data </title> <img src="http://classroomclipart.com/images/gallery/Animations/lightbulb.gif" alt="lightbulb" align="left" height="100" width="80">  </title> <img src="http://classroomclipart.com/images/gallery/Animations/lightbulb.gif" alt="lightbulb" align="right" height="100" width="80"> <br> <h1> <center> <font color ="#800000">  Electric Consumption by Zip Codes 2010 </font> </h1> <br> <center>''' + str(HEADING) + '<br> <br> <font size="5" align="center"> Averages: </font><table align=''center'' border="1">'      # sets up top of pg

comerZip = findzipRange(lines, 'Commercial', 1)
indusZip = findzipRange(lines, 'Industrial', 1)             # definitons of the zip code ranges for the data types
institZip = findzipRange(lines, 'Institutional', 1)
largeZip = findzipRange(lines, 'Large Residential', 1)
smallZip = findzipRange(lines, 'Small Residential', 1)

rangecomerKWH = moreRange(lines, 'Commercial', 2)
rangeindusKWH = moreRange(lines, 'Industrial', 2)           # definitions of the range of energy comsump in KWH for diff data types
rangeinstitKWH = moreRange(lines, 'Institutional', 2)
rangelargeKWH = moreRange(lines, 'Large Residential', 2)
rangesmallKWH = moreRange(lines, 'Small Residential', 2)

rangecomerGJ = moreRange(lines, 'Commercial', 3)            # definitons of the range of energy consump in GJ for diff data types
rangeindusGJ = moreRange(lines, 'Industrial', 3)
rangeinstitGJ = moreRange(lines, 'Institutional', 3)
rangelargeGJ = moreRange(lines, 'Large Residential', 3)
rangesmallGJ = moreRange(lines, 'Small Residential', 3)
    
comerRange = findrange(lines, 'Commercial')                 #find range of all the comercial data data
lines = replaceaverage(lines, comerRange, 2, 3)             # then replaceaverage will update that range with its commercial averages
indusRange = findrange(lines, 'Industrial')
lines = replaceaverage(lines, indusRange, 2, 3)
institRange = findrange(lines, 'Institutional')
lines = replaceaverage(lines, institRange, 2, 3)
largeRange = findrange(lines, 'Large Residential')
lines = replaceaverage(lines, largeRange, 2,3)
smallRange = findrange(lines, 'Small Residential')
lines = replaceaverage(lines, smallRange, 2,3)

lines = zipReplace(lines, 'Commercial' , 0, comerZip)
lines = zipReplace(lines, 'Industrial', 0, indusZip)                    # makes master list of all of the zip codes
lines = zipReplace(lines, 'Institutional', 0, institZip)
lines = zipReplace(lines, 'Large Residential', 0, largeZip)
lines = zipReplace(lines, 'Small Residential', 0, smallZip)

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
html += "\n <br> <br>  </table> <br <br> <font size='5' align='center'> Ranges: </font> <br> <br> <table align=""center"" border='1'> "
lines = ReplaceRange(lines, 'Commercial', 2,3, rangecomerKWH, rangecomerGJ)     #  replaces ranges of the diff sections with the diff KWH and Gj values
lines = ReplaceRange(lines, 'Industrial', 2,3, rangeindusKWH, rangeindusGJ)
lines = ReplaceRange(lines, 'Institutional', 2,3, rangeinstitKWH, rangeinstitGJ)
lines = ReplaceRange(lines, 'Large Residential', 2,3, rangelargeKWH, rangelargeGJ)
lines = ReplaceRange(lines, 'Small Residential', 2,3, rangesmallKWH, rangesmallGJ)
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
html += "</table>"
html += "<br> <br> <h1> Conclusion </h1>" + str(CONCLUSION)
html +=  "<br> <br> <h2> Sources </h2>  All data from: <a href='https://nycopendata.socrata.com/Environmental-Sustainability/Electric-Consumption-by-ZIP-Code-2010/74cu-ncm4'> Nycopendata </a> <br> NYC Open Data. N.p., n.d. Web. 25 Apr. 2013."
html += "<br><br><br> <br> For Complete Data, click : <a href='http://lisa.stuy.edu/~leslie.bresnahan/data01.py'> HERE </a> "
html += "</html>"                # close all the tags
print html

