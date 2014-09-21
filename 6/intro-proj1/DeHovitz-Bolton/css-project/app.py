from flask import Flask,render_template, request
import random

app = Flask(__name__)

name = None
quote = None
adjective = None

@app.route("/")
def start():
    global name
    global quote 
    global adjective

    name = None
    quote = None
    adjective = None
    
    return render_template("index.html")

@app.route("/results", methods = ["POST", "GET"])
def main():
    global name
    global quote 
    global adjective

    if name == None:
       name = request.form["name"]
    if quote == None:
        quote = request.form["quote"]
    if adjective == None:
        adjective = request.form["adjective"]

    print name
    print quote
    print adjective
    s = '''<!doctype html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <title>Wisdom!</title>
        <style>
    body {
        background: #f1f1f1}
    section {
    
        border-radius: 10px;
        padding: 10px;
        margin-left: auto;
        margin-right: auto;
        width: 400px
    }
    .c {
        background: #D3D3D3;
        color: black;
        }
    .a   {
     background: black;
        color: white;
        } 
    .b {
    background: #d7d7d7;
    width: 312px
    }
    
  </style>
    
        <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
</head>


        
        '''

    s+= '<h3 class="brand-title"><center><b>Wise words from a figure of great stature </b></h3>'

    #s+= "<center>and now for your pleasure a quote: <br><br>"
    get_it = open('quotes.txt', 'r')
    variableName = get_it.read()
    lines= variableName.split('\n')
    lines=lines[:len(lines)-1]
    if quote!="":
        lines.append(quote)
        lines.append(quote)
        


    filez = open('namesAndImages.txt', 'r')
    Dict=filez.read()
    Dict=Dict.split('\n')
    Dict=Dict[:len(Dict)-1]
    if name!="":
        Dict.append(name+',https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ4qlCVQrMo5QqT5-y_pEcycr-HEap5aOoWAHsHtEa3_qJAFxKZA')
        Dict.append(name+',https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ4qlCVQrMo5QqT5-y_pEcycr-HEap5aOoWAHsHtEa3_qJAFxKZA')
    
    Image=Dict[random.randint(0, len(Dict)-1)]
    Image=Image.split(',')

    Name=Image[0]
    image=Image[1]
    filezd = open('Titles.txt', 'r')
    titles=filezd.read()
    titles=titles.split('\n')
    titles=titles[:len(titles)-2]
    if adjective!="":
        titles.append(adjective)
        titles.append(adjective)
    s+= '<center><section class ="a"><img src='+'"'+image+'"'+'width="400" height="400"></img></center></section>'
    s+= '<section class ="c"><center>As the '+ titles[random.randint(0, len(titles)-1)]+' <b>'+Name+'</b> once said:<br>'
    s+= '"'+lines[random.randint(0, len(lines)-1)]+'"'
    s+= '''</section><center><br>
    <section class = "b">
   <a class="pure-button pure-button-primary" href="/results">Next Quote</a>  
   
   <a class="pure-button" href="/">Return to Home Page</a></section>
   
'''

#s+= '''<br><br><br> <b> TEST </b> <br> <br>'''
    #for allImage in Dict:
        
        #allImage=allImage.split(',')

        #Name=allImage[0]
        #image=allImage[1]
        #s+='<br><br> ' + Name + "<br><br>"
        #s+= '<center><img class="pure-img" src='+'"'+image+'"'+'width="400" height="400"></img></center><br>'
    
    s+= '<br><br><br> <font size="1.5"> <b>*historical accuracy may<br> not be guaranteed'
    filez.close()
    get_it.close()
    filezd.close()



    return s

    
if __name__=="__main__":
    app.debug=True
    app.run()
