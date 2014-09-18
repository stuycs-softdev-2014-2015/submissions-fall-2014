
from flask import Flask,render_template


app = Flask(__name__)



'''@app.route("/Results")
def Results():
    
    boro is a string, col is either 3 (food type) or 6 (grade)
   
    return render_template("Results.html",dictionary=d,boro=boro)
    '''
@app.route("/")
def home():
    if request.method =="GET":
        return render_template("Home.html")
    else:
        boro = request.form["group1"]
        col = 6
        foodorgrade = request.form["group2"]
        if foodorgrade == "Food":
            col = 3
        d = {}
        for list in inspectiondata:
            if list[1]==boro:
                if d.has_key(list[col]):
                    d[list[col]]+=1
                else:
                    d[list[col]]=1
        return render_template("Results.html",dictionary=d,boro=boro,foodorgrade=foodorgrade)
def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
    return l
    
inspectiondata = get_file('Results_Without_violations.csv')


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
