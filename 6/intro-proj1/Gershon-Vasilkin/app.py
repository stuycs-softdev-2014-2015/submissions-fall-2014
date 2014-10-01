from flask import Flask,render_template,request


app = Flask(__name__)

boros = ["BROOKLYN","BRONX","QUEENS","MANHATTAN","STATEN ISLAND"]


@app.route("/facts",methods=['GET', 'POST'])
def facts():
        return render_template("Facts.html")
    

@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("Home.html",l=boros)

        

        

@app.route("/results",methods=['GET', 'POST'])
def Results():
    boro = request.form['group1']
    if boro == "STATEN":
        boro = "STATEN ISLAND"
    fg = request.form['group2']
    if fg == "Grade":
        col = 6
        d = get_data(boro,col)
        return render_template("Grade.html",d=d,boro=boro)
    else :
        col = 3
        d = get_data(boro,col)
        return render_template("Food.html",d=d,boro=boro)
    button = request.form["b"]
    if button == "return":
        return render_template("Home.html",l=boros)    
   
    

            
def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
    return l

def get_data(boro,col): 
    inspectiondata = get_file('Results_Without_violations.csv')
    d = {}
    for list in inspectiondata:
         if list[1]==boro:
             if d.has_key(list[col]):
                 d[list[col]]+=1
             else:
                 d[list[col]]=1
    return d

'''
def print_grades():
    for list in inspectiondata: 
        if list[1]=='QUEENS':
            grade=int(list[8])
            print grade
'''


#print_grades(); 

if __name__=="__main__":
    app.debug=True
    app.run();
