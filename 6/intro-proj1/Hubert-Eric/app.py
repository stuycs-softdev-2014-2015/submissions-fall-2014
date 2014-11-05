from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home(cols = None, counter = 0):
    grid =  getGrid('planets.csv')
    grid = cleanGrid(grid, getDelete(grid))
    header = grid[0]
    return render_template('home.html',
            grid = grid[1:], headerRow = header)

@app.route('/planet/dataset', methods=['GET', 'POST'])
def planetpage(stats = None):
    if request.method=='POST':
        print("post")

        #receive variables
        lowerbound = request.form['lowerbound']
        upperbound = request.form['upperbound']
        variable = request.form['variable']

        try:
            variable = int(variable)
            lowerbound = float(lowerbound)
            upperbound = float(upperbound)
        except ValueError:
            print("Not a Number")

        if variable > 0:
            partialGrid = getPartialGrid(cleanedGrid[1:],
                                         lowerbound,
                                         upperbound,
                                         variable)
        else:
            partialGrid = cleanedGrid
        
        analysisFile(partialGrid, bounds = [variable, lowerbound, upperbound])
        return render_template('dataset.html',
                               grid=partialGrid,
                               headerRow = cleanedGrid[0])
    else:
        print("get")
        return render_template('dataset.html',
                grid=cleanedGrid[1:], headerRow = cleanedGrid[0])

def analysisFile(pg, bounds):
    file = open('boundsAnalysis.txt', 'w')
    avgMass = str(getAverage(pg, 1))
    avgRadius = str(getAverage(pg, 2))
    avgEcc = str(getAverage(pg, 3))
    avgInc = str(getAverage(pg, 4))
    avgYear = str(getAverage(pg, 5))
    avgList = [avgMass, avgRadius, avgEcc, avgInc, avgYear]
    for x in range(3):
        if x == 0:
            var = bounds[x]
            if var == 1:
                file.write("mass\n")
            elif var == 2:
                file.write("radius\n")
            elif var == 3:
                file.write("eccentricity\n")
            elif var == 4:
                file.write("inclination\n")
            else:
                file.write("year of discovery\n")
        else:
            file.write(str(bounds[x]) + "\n")
    for e in avgList:
        file.write(e + "\n")
  
@app.route('/analysis')
def analysis(file = 'boundsAnalysis.txt'):
    data = open(file, 'r')
    bounds = []
    nums = []
    for x in range(3):
        bounds.append(data.readline())
    for y in range(5):
        nums.append(data.readline())
    return render_template('analysis.html', avgList = nums,
                           bounds = bounds)
 
def dictData(grid):
    data = {}
    for row in grid:
        key = row[0]
        data[key] = []
        for elem in row:
            data[key].append(elem)
    return data

def getDelete(grid):
    ans = []
    exclude = ['updated', 'K', 'albedo', 'omega',
               'tperi', 'molecules', 'ra', 'dec']
    headers = grid[0]
    for i, elem in enumerate(headers):
        if elem.strip() in exclude or '_' in elem:
            ans.append(i)
    return ans

def cleanGrid(grid, toDel):
    newgrid = [[] for x in range(len(grid))]
    for rowi, row in enumerate(grid):
        for coli, col in enumerate(row):
            if coli not in toDel and len(newgrid[rowi]) < 6:
               newgrid[rowi].append(col)
    return newgrid

def getGrid(filename = 'planets.csv'):
    planets = open(filename, 'r').readlines()
    grid = [planets[x].split(',') for x in range(len(planets))]
    return grid

# returns a 2d array with elements of the table between
# the upperbound and lowerbound of the variable
#
# column -> int for column index
def getPartialGrid(grid, lowerbound, upperbound, column = 1):
    partialGrid = []
    for row in grid:
        try:
            num = float(row[column])
            if num > lowerbound and num < upperbound:
                partialGrid.append(row)
        except ValueError:
            print("not a float")
    pGridGlobal = partialGrid
    return partialGrid


def getAverage(grid, column, removeTableHeader = True):
    # Get rid of header row without data

    if removeTableHeader:
        grid = grid[1:]
    totalValue = 0
    counter = 0

    for row in grid:
        try:
            counter += 1
            totalValue += float(row[column])
        except ValueError:
            print("not a float")

    return totalValue/counter

if __name__=='__main__':
    allPlanetData = dictData(getGrid())
    grid = getGrid('planets.csv')
    cleanedGrid = cleanGrid(grid, getDelete(grid))
    app.run(debug=True)


