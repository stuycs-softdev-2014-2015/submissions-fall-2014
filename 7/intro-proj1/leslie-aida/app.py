from flask import Flask, render_template;
app = Flask(__name__)

@app.route("/")
def home():
    inStream = open("data_hw252.csv", 'r')                    
    data = inStream.read()
    inStream.close()

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
         data = data[:126239]
         return data
         comment = '''
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
        
    # data crunching to be continued
'''
    data = removeLineBr(data)
    lines = data.split("\n")

    
    return render_template("home.html", data = data, lines = lines);


if __name__ == "__main__":
    app.debug = True
    app.run()
