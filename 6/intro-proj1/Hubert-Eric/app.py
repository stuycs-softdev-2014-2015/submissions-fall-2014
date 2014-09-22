from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home(cols = None, counter = 0):
    grid =  getGrid('planets.csv')
    grid = cleanGrid(grid, getDelete(grid))
    header = grid[0]
    return render_template('home.html',
            grid = grid[1:], headerRow = header)

@app.route('/planet/test')
def planetpage(stats = None):
    return str(getPartialGrid(cleanedGrid, 1, 2))

@app.route('/analysis')
def analysis():
    grid = getGrid('planets.csv')
    grid = cleanGrid(grid, getDelete(grid))
    averagemass=str(getAverage(grid, 1))
    return render_template('analysis.html', averagemass = averagemass)


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


