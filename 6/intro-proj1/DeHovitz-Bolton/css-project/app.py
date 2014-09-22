from flask import Flask,render_template, request
import random

app = Flask(__name__)

name = None
quote = None
adjective = None

def imgReader(name):
  filez = open('./Static/namesAndImages.txt', 'r')
  Dict=filez.read()
  Dict=Dict.split('\n')
  Dict=Dict[:len(Dict)-1]
  if name!=""and name!=None:
      Dict.append(name+',http://www.tabwallpaper.com/wp-content/uploads/friedrich-wanderer-above-the-sea-of-fog-1024x1024.jpg')
      Dict.append(name+',http://www.tabwallpaper.com/wp-content/uploads/friedrich-wanderer-above-the-sea-of-fog-1024x1024.jpg')
  filez.close()
  return Dict


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
    if request.method == 'POST':
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
    .title{
            color: #343434;
            font-weight: normal;
            font-family: 'Ultra', sans-sarif
            font-size:34px;
            line-height: 38px;
            text-transform: uppercase;
            text-shadow: 0 2px white, 0 3px #777
         }
    .button-test{
        color: white;
        border-radius: 4px;
        background: rgb(250, 85, 85);
        }
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
    width: 312px;
    }
    .d {
    background: rgb(240, 70, 70);
    width 150px
    }

  </style>

        <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
</head>



        '''

    s+= '''
    <div class="title">
    <h3 class="brand-title"><center><b><font face="Baskerville" size="6"> Wise words from a figure of great stature </font></b></h3>'
    </div>
    '''
    #s+= "<center>and now for your pleasure a quote: <br><br>"
    get_it = open('./Static/quotes.txt', 'r')
    variableName = get_it.read()
    lines= variableName.split('\n')
    lines=lines[:len(lines)-1]
    if quote!="" and quote!=None:
        lines.append(quote)
        lines.append(quote)



    imgRepo = imgReader(name)
    Image=imgRepo[random.randint(0, len(imgRepo)-1)]
    Image=Image.split(',')

    Name=Image[0]
    image=Image[1]
    filezd = open('./Static/Titles.txt', 'r')
    titles=filezd.read()
    titles=titles.split('\n')
    titles=titles[:len(titles)-2]
    if adjective!=""and adjective!=None:
        titles.append(adjective)
        titles.append(adjective)
    s+= '<div class ="pure-g">'
    s+= '<div class ="pure-u-15-24">'
    s+= '<center><section class ="a"><img src='+'"'+image+'"'+'width="400" height="400"></img></center></section>'
    s+= '<section class ="c"><center> As the '+ titles[random.randint(0, len(titles)-1)]+' <b>'+Name+'</b> once said:<br>'
    s+= '"'+lines[random.randint(0, len(lines)-1)]+'"'
    s+= '''</section><br></div>
        <div class ="pure-u-4-24">
        <center>
        <section class = "b">
          <a class="pure-button pure-button-primary" href="/results"><font face ="Baskerville">Next Quote</a>
        <div>
        <style scoped>
          .button-return{
              color: white;
              border-radius: 4px;
              background: rgb(225, 120, 20);
              }
        </style> <br>
        <a class="button-return pure-button" href="/"><font face ="Baskerville">Return to Home Page</a></div>
        </section></font></center>
        <br> <br> <br><br><br> <br> <br><br>
        <section class = "d"><center>
        <a class="button-test pure-button" href="/tester"><font face ="Baskerville"> Image Quality Test </font></center></a>
        </section>
        </div><!--end unit-->
        </div><!--end grid-->
'''

#s+= '''<br><br><br> <b> TEST </b> <br> <br>'''
    #for allImage in Dict:

        #allImage=allImage.split(',')

        #Name=allImage[0]
        #image=allImage[1]
        #s+='<br><br> ' + Name + "<br><br>"
        #s+= '<center><img class="pure-img" src='+'"'+image+'"'+'width="400" height="400"></img></center><br>'

    s+= '<br><br><br><center> <font size="1.5"> <b>*historical accuracy may<br> not be guaranteed</font></center>'
    get_it.close()
    filezd.close()



    return s

@app.route("/results", methods = ["POST", "GET"])
@app.route("/tester")
def test():
    global name

    imgs = imgReader(name)
    array = []
    x = 0;
    for i in imgs:
        pic = i.split(',')
        array.append(pic[1])
    print array
    return render_template("tester.html", images = array, name = name)


if __name__=="__main__":
    app.debug=True
    app.run()
