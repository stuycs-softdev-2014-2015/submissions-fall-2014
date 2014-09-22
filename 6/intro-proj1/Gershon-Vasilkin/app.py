from flask import Flask,render_template,request


app = Flask(__name__)

boros = ["BROOKLYN","BRONX","QUEENS","MANHATTAN","STATEN ISLAND"]

@app.route("/Results",methods=['GET', 'POST'])
def Results():
        button = request.args.get("b",None)
        if button == "return":
            return render_template("Home.html",l=boros)    
    #boro is a string, col is either 3 (food type) or 6 (grade)
   
    #return render_template("Results.html",d=d,boro=boro,foodorgrade=foodorgrade)

@app.route("/facts")
def facts():
        return render_template("Facts.html")
    

@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method =="GET":
        return render_template("Home.html",l=boros)
    else:
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
