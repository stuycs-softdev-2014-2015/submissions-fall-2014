from flask import Flask, render_template

app = Flask(__name__)

#global variable - holds string content
htmlStr ="<table border = '1'> <tr> <td> \r"

@app.route("/")
def home ():
    return render_template("test.html")

@app.route("/conversion")
def conversion (): #converts the csv file into html code
    ans = ""
    filecsv = open ("data.csv", "r") # the data set with teh debate statistics 
    y = filecsv.readlines () # every line put into the a list of strings
    filecsv.close ()
    i =0
    lengths = len(y)
    while i < lengths :
        if i != lengths - 1: #if the index is not the last index of the list
            ans += y[i].replace ("\n", "</td </tr> <tr> <td>\r") 
        else: 
            ans += y[i].replace ("\n", "</td> </tr> \r</table> </div>  </body> </html> ")
            ans = ans.replace (",", "</td> <td>") 
            ans = ans.replace (";", " ")  # for some reason, google docs/libre office; one of them added ";" instead of a blank white space...
                                      #so to fix the problem, we added this line to replace the semi-colon with an actual space
        i += 1
        

    

    return render_template("table.html",
                           htmlStr=htmlStr,
                           ans=ans)

if __name__=="__main__":
    app.debug=True
    app.run(port=5050)
    
