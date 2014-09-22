from flask import Flask, render_template, request

app = Flask(__name__)

#global variable - holds string content
htmlStr ="<table border = '1' align='center'> <tr> <td> \r"
filecsv = open ("data.csv", "r") # the data set with teh debate statistics 
y = filecsv.readlines () # every line put into the a list of strings
filecsv.close ()

#******************************************************************#
#for analysis page
holder = [] # just placeholding lists for two globals below
holder2 = []
def countcommas (calculatinglist, lists): # countcommas counts commas in a string and gives back everything in the total column excl the first row
    calculatinglist = calculatinglist [1:]
    for z in calculatinglist:
            i= 0
            while i < 6:
                z = z[(z.find(",")) + 1:] #
                i += 1
            lists.append (float(z[:z.find(",") ]))
    return lists

def Schoolnames (calculatinglist, lists): # countcommas counts commas in a string and gives back everything in the total column; includes first row
    i = 0
    while i < len (calculatinglist):
        string = calculatinglist[i]
        string = string[:string.find(",")]
        lists.append (string)
        i += 1
    return lists

listwithnames = Schoolnames(y, holder2)
totallists= countcommas (y, holder)

def avgvalues (listx):
    i = 1 # skip the first row which label the columns of the list
    answer = "<tr> <td> <b> " + "Team Name" + "</b></td> <td><b> " + "Average of scores" + " </b></td> </tr> " # first row of the table
    while i < len (listx): # loops through all the elements of listx which are strings
        ans = 0 # temp variable to denote the sum of top 1- top 5
        yar = listx[i].split (",")
        yar = yar [1:6]
        indice = 0
        counter = 0 # counts how many columns have been passed
        while indice < 5: # counts index of the splitted list from the strings
            if yar[indice] != "" :
                ans += float(yar[indice])
                counter += 1
            indice += 1
        answer += "<tr> <td>" + listwithnames[i] + "</td> <td>" + str(ans/counter) + "</td> </tr> "
        i += 1
    return answer

def modeListA(nums):# only returns first of the modes.. *** this function is used in the other following functions
                    # variation one, returns List of the mode and its index
    ans = nums[0]
    i = 1
    while i < len (nums):
        if nums.count (nums[i]) > nums.count (ans): # if it was >= the last mode would be returned -> goes through whole list for the mode
            ans = nums[i]
        i += 1
    x = nums.index (ans)
    return [ans, x]

def medList(nums): # finds median of list
    nums = sorted(nums)
    if len(nums)%2 == 0:
        return (nums[(len(nums))/2] + nums[((len(nums))/2) - 1])/2.0
    else:
        return nums[(len(nums))/2]

def meanList(nums):
    return sum(nums) * 1.0 / len(nums)

modename =   modeListA(totallists) # global that gives mode with its index in a list of the totals
SchoolName = y[modename[1] + 1] # modename[1] gives the nth row of the real table - 1 *** -> x [that index]
SchoolName = SchoolName[:SchoolName.find(",")] # global variable that takes the school name from the csv dco aka the first column excl the first row



#                        START OF SERVER CODE                      #
#******************************************************************#
############ Fiddling form elements #################
@app.route("/")
@app.route("/home")
@app.route("/index")
def home ():    
    return render_template("althome.html")


@app.route("/welcome",methods=["GET","POST"])
@app.route("/about",methods=["GET","POST"])
def about():
    strs = " "
    estrs = " "
    if request.method == "GET":
        return render_template("about.html")
    else:
        l = request.form.getlist("style")
        name2 = request.form["name2"]
        name = request.form["name"]
        print name,name2

    if "bold" in l:
        strs += "<b>"
        estrs += "</b>"
    if "big" in l:
        strs += "<span style='font-size:2.4em'>"
        estrs += "</span>"      
    if "color" in l:
        strs += "<span style='color:green'>"
        estrs += "</span>"      

    if name == "":
        name = "Anonymous"
    if name2 == "":
        name2 = name


    #if bold != None or big != None or color != None:
    return render_template("about.html", tag = strs, etag = estrs, name = name, name2 = name2)
    
            
    
    
    

@app.route("/analysis")
def analysis():
    ans = " <div align ='center'> <table> <table border = '1' width= '70' height = '80' > <tr> <td> <b> MODE </td>  <td> " + str(modename[0]) + "</td> <td> " + SchoolName
    ans += " </td> </tr> <tr> <td> <b> MEDIAN </td> <td> " + str (medList (totallists)) + "</td> <td> " + "N/A" + "</td> </tr>"
    ans += "<tr> <td> <b> MEAN </td>  <td> " + str (meanList (totallists)) + "</td> <td> " + "N/A" + "</td> </tr>"
    ans +=  " </table> </div> <br>"
    
    ans += "<div align ='center'> <table> <table border = '1'>" + avgvalues (y) + "</table> "
    ans += "<a href= 'data01.py' > Link to the Data </a>  <br><br><br> <img src='http://diseaseoftheweek.files.wordpress.com/2010/08/debate-1.jpg' width='300' height='250'> <br> <br>"
   
    ans = ans.replace (";", " ") 
    return render_template("altanalysis.html",ans=ans)

######### Prints Table ############
@app.route("/conversion")
def conversion(): #converts the csv file into html code
    ans = ""
    i =0
    lengths = len(y)
    while i < lengths :
        if i != lengths - 1: #if the index is not the last index of the list
            ans += y[i].replace ("\n", "</td </tr> <tr> <td>\r") 
        else: 
            ans += y[i].replace ("\n", "</td> </tr> \r</table> </div>  </body> </html> ")
            ans = ans.replace(",","</td><td>")
            ans = ans.replace (";", " ")  # for some reason, google docs/libre office; one of them added ";" instead of a blank white space...
                                      #so to fix the problem, we added this line to replace the semi-colon with an actual space
        i += 1
    return render_template("altable.html", 
                           htmlStr=htmlStr,
                           ans=ans)




###########################

if __name__=="__main__":
    app.debug=True
    app.run(port=5020)
    
