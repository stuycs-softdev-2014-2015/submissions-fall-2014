from flask import Flask, render_template

app = Flask(__name__)


x = open("act2.txt",'r')
file1 = x.read()
lines2 = file1.split('\n')
lines=",".join(lines2)
lines=lines.split(',')
x.close()

while "" in lines:
    lines.remove("")


while 'book' in lines:
    lines.remove('book')
while 'command' in lines:
    lines.remove('command')
while 'dreamself' in lines:
    lines.remove('dreamself')
while 'easter egg' in lines:
    lines.remove('easter egg')
while 'fedorafreak' in lines:
    lines.remove('fedorafreak')
while 'original bunny' in lines:
    lines.remove('original bunny')
while 'package' in lines:
    lines.remove('package')
while 'writings' in lines:
    lines.remove('writings')

names=[]
pages=[]

for x in lines:
    try:
        int(x)
        if x not in pages:
            pages.append(x)
    except:
        if x not in names:
            names.append(x)

names.sort()


dnames={}
for x in names:
    dnames[x] = []


lines3=[]

for x in lines2:
    lines3.append(x.split(","))

for x in lines3:
    for y in dnames:
        if y in x:
            dnames[y].append((x[0]))

image = {}
image["Diamonds Droog"] = "http://24.media.tumblr.com/tumblr_ljo6z5uf5T1qipzzwo1_500.jpg"
image["Kernelsprite"] = "http://images.wikia.com/mspaintadventures/images/1/1c/Kernelsprite.gif"
image["Rose"] = "http://static.tumblr.com/e3fot7q/Ymfm39itc/871827.jpg"
image["Hearts Boxcars"] = "http://th05.deviantart.net/fs70/PRE/i/2010/300/7/f/hearts_boxcars_by_neecross-d31lmmq.jpg"
image["4/Clover"] = "http://www.mspaintadventures.com/storyfiles/hs2/01324.gif"
image["Dad"] = "http://24.media.tumblr.com/tumblr_mbjptcymvG1qili7co9_r1_400.png"
image["Bro"] = "http://b.vimeocdn.com/ts/282/147/282147442_640.jpg"
image["John"] = "http://th03.deviantart.net/fs70/PRE/i/2012/095/e/f/john_egbert___homestuck_by_fumi_san-d4v28a4.png"
image["Maplehoof"] = "http://img138.imageshack.us/img138/3527/maplehoof.png"
image["Sawtooth"] = "http://www.fybertech.com/4get/13512999621960.jpg"
image["Jaspersprite"] = "http://fc08.deviantart.net/fs70/f/2011/185/0/f/jaspersprite_by_jesscookie-d3kxjla.png"
image["Nanna"] = "http://images4.wikia.nocookie.net/__cb20100816225720/mspaintadventures/images/e/ef/Nanna3.png"
image["Lil Cal"] = "http://24.media.tumblr.com/tumblr_m9upz8WVy71qmbcy1o1_r1_500.png"
image["Dave"] = "http://25.media.tumblr.com/tumblr_m4w3siAVfe1rnuh17o1_1280.jpg"
image["Colonel Sassacre"] = "http://www.mspaintadventures.com/storyfiles/hs2/00032_2.gif"
image["Kernel/Crowsprite"] = "http://images2.wikia.nocookie.net/__cb20100824161426/mspaintadventures/images/c/c3/Seppucrow.png"
image["Mom"] = "http://static.tvtropes.org/pmwiki/pub/images/Mom_homestuck_4683.png"
image["2/Doze"] = "http://24.media.tumblr.com/06fef16c40f6b15079e11dff0f1e446c/tumblr_ml9o6mlvjw1s8e0v8o1_r2_500.png"
image["1/Itchy"] = "http://24.media.tumblr.com/1b0d6e1c256b37adc90ffc25e6a768f7/tumblr_mhbe0hKya31s27qx0o1_1280.jpg"
image["Peregrine Mendicant"] = "http://24.media.tumblr.com/tumblr_malfr1ZeOF1qiu1ojo1_500.jpg"
image["Clubs Deuce"] = "http://media.tumblr.com/tumblr_md1aqxw9We1r01j8b.gif"
image["Squarewave"] = "http://media.tumblr.com/tumblr_mde6xviQI21r1exsw.png"
image["Liv Tyler"] = "http://images3.wikia.nocookie.net/__cb20100912194041/mspaintadventures/images/a/a0/Uberbunny.png"
image["3/Trace"] = "http://24.media.tumblr.com/3d6535a8a6bc3dfd6ef01c59d7c0adce/tumblr_mer05erdDy1qhqqxpo1_r2_500.jpg"
image["Serenity"] = "http://media.tumblr.com/tumblr_m83upfzGxd1qgef54.gif"
image["Davesprite"] = "http://static.tumblr.com/abab83ff6425c49687fdac326e7a5f81/ssqej2y/Ev9mfw3iy/tumblr_static_yeah.gif"
image["15/Cans"] = "http://static.tvtropes.org/pmwiki/pub/images/213px-15cans_4921.png"
image["Sweet Bro and Hella Jeff"] = "http://images1.wikia.nocookie.net/__cb20091116012943/mspaintadventures/images/4/43/Where_making_this_happen.PNG"
image["Jade"] = "http://static.zerochan.net/Jade.Harley.full.861969.jpg"
image["Jaspers"] = "http://media.tumblr.com/tumblr_lyjgmi0xGj1r645oy.png"
image["Nannasprite"] = "http://25.media.tumblr.com/tumblr_maope9TLNE1qexi1uo1_500.png"
image["Wayward Vagabond"] = "http://fc00.deviantart.net/fs71/f/2012/260/2/a/homestuck_wallpaper__wayward_vagabond_mayor_poster_by_scarelink-d5f1i8t.jpg"
image["Spades Slick"] = "http://images1.wikia.nocookie.net/__cb20110304130153/mspaintadventures/images/0/0e/03614.gif"



def createVarChar(name):
    if name == "Clubs":
        name = "Clubs Deuce"
    if name == "Colonel":
        name = "Colonel Sassacre"
    if name == "Diamonds":
        name = "Diamonds Droog"
    if name == "Hearts":
        name = "Hearts Boxcars"
    if name == "Cal":
        name = "Lil Cal"
    if name == "Liv":
        name = "Liv Tyler"
    if name == "Peregrine":
        name = "Peregrine Medicant"
    if name == "Spades":
        name = "Spades Slick"
    if name == "Sweet":
        name = "Sweet Bro and Hella Jeff"
    if name == "Vagabond":
        name = "Wayward Vagabond"
    if name == "Itchy":
        name = "1/Itchy"
    if name == "Cans":
        name = "15/Cans"
    if name == "Doze":
        name = "2/Doze"
    if name == "Trace":
        name = "3/Trace"
    if name == "Clover":
        name = '4/Clover'

    HTML = '''
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>character.html</title>
    </head>
    <body bgcolor="#0e4603" text="#ffffff">
    <br>
    '''
    HTML += "<div align='center'><big><big><big> "+name+"</big></big></big></div> <br>"
    HTML += "<img src='"+image[name]+"'><br><br><br> Pages in which he appears: <br>"
    for x in dnames[name]:
        HTML += "<a href='http://mspaintadventures.com/?s=6&p=00"+x+"'><font color='cyan'>"+x+"</a><br>"
    HTML += ''' </body>
    </html>'''
    return HTML

def createVarPage(num):
    return ""

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/<Choice>')
def renderChoice(Choice = None):
    if Choice == 'Character':
        return render_template("chooseChar.html")
    return render_template("choosePage.html")

@app.route("/Character/<CharacterName>")
def renderCharPage(CharacterName=None):
    return createVarChar(CharacterName)
@app.route("/Page/<PageNumber>")
def renderPage(PageNumber = None):
    return render_template("page.html",
                           var = createVarPage(PageNumber))
                           

    
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 1639)
