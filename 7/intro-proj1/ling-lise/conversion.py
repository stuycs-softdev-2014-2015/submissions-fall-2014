from flask import Flask, render_template

app = Flask(__name__)

#global variable - holds string content
htmlStr ="<table> <table border = '1'> <tr> <td> "

@app.route("/")
@app.route("/conversion")
def conversion (): #converts the csv file into html code
    ans = ""
    filecsv = open ("data_hw25.csv", "r") # the data set with teh debate statistics 
    y = filecsv.readlines () # every line put into the a list of strings
    filecsv.close ()
    i =0
    lengths = len(y)
    while i < lengths :
        if i != lengths - 1: #if the index is not the last index of the list
            ans += y[i].replace ("\n", "</td> </tr> <tr> <td>") # strings can use function replace to replace substrings
            #/n symbolizes next line/ row for table : that means we need to end cell and row and add new row and cell if the element is not the last one
        else: # last index of the list, add all the end tags to the html
            ans += y[i].replace ("\n", " </td> </tr> </table> </div>  </body> </html> ") # we need to end all tags in last element
            i += 1
            ans = ans.replace (",", "</td> <td>") # for all the commas we need to end the cell for the nums and add one for the squares
            ans = ans.replace (";", " ")  # for some reason, google docs/libre office; one of them added ";" instead of a blank white space...
                                      #so to fix the problem, we added this line to replace the semi-colon with an actual space
    return render_template("some.html",
                           ans)

if __name__=="__main__":
    app.debug=True
    app.run(port=5050)
    
