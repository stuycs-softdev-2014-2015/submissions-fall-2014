from flask import Flask, render_template, request

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

for x in lines2:
    lines3.append(x.split(","))

for x in lines3:
    for y in dnames:
        if y in x:
            dnames[y].append((x[0]))

dpages={}

for x in pages:
    dpages[x]=[]

for x in dnames:
    for y in dpages:
        if y in dnames[x]:
            dpages[y].append(x)

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

@app.route('/')
def main():
    #Name selected
    name1 = request.args.get("char",None)
    name2 = request.args.get("char2", None)
    name3 = request.args.get("char3", None)
    name4 = request.args.get("char4", None)

    #Has user clicked submit
    sub = request.args.get("submit",None)
    if(sub == "Search for Pages"):
        return createVarChar(name1, name2, name3, name4)

    return render_template("main.html")



#my attempt at being more efficient than listing each page number. Probably wont be needed now
def listPages():
    i = 1901
    HTML = ""
    while ( i < 2657 ):
        HTML += '<a href="http://0.0.0.0:1639/Page/' + str(i) + '">Page ' + str(i) + '<br>'
        i+=1
    HTML += "</body></html>"
    return HTML



def createVarChar(name1, name2, name3, name4):
    namelist = [name1]
    if name2 != "None":
        namelist.append(name2)
    if name3 != "None":
        namelist.append(name3)
    if name4 != "None":
        namelist.append(name4)

    for name in namelist:
        if name == "Clubs":
            namelist[namelist.index(name)] = "Clubs Deuce"
        if name == "Colonel":
            namelist[namelist.index(name)] = "Colonel Sassacre"
        if name == "Diamonds":
            namelist[namelist.index(name)] = "Diamonds Droog"
        if name == "Hearts":
            namelist[namelist.index(name)] = "Hearts Boxcars"
        if name == "Cal":
            namelist[namelist.index(name)] = "Lil Cal"
        if name == "Liv":
            namelist[namelist.index(name)] = "Liv Tyler"
        if name == "Peregrine":
            namelist[namelist.index(name)] = "Peregrine Medicant"
        if name == "Spades":
            namelist[namelist.index(name)] = "Spades Slick"
        if name == "Sweet":
            namelist[namelist.index(name)] = "Sweet Bro and Hella Jeff"
        if name == "Vagabond":
            namelist[namelist.index(name)] = "Wayward Vagabond"
        if name == "Itchy":
            namelist[namelist.index(name)] = "1/Itchy"
        if name == "Cans":
            namelist[namelist.index(name)] = "15/Cans"
        if name == "Doze":
            namelist[namelist.index(name)] = "2/Doze"
        if name == "Trace":
            namelist[namelist.index(name)] = "3/Trace"
        if name == "Clover":
            namelist[namelist.index(name)] = "4/Clover"
        if name == "Daves":
            namelist[namelist.index(name)] = "Davesprite"
        if name == "Jaspers":
            namelist[namelist.index(name)] = "Jaspersprite"
        if name == "Crow":
            namelist[namelist.index(name)] = "Kernel/Crowsprite"
        if name == "Kernel":
            namelist[namelist.index(name)] = "Kernelsprite"
        if name == "Maple":
            namelist[namelist.index(name)] = "Maplehoof"
        if name == "Nannas":
            namelist[namelist.index(name)] = "Nannasprite"
        if name == "Saw":
            namelist[namelist.index(name)] = "Sawtooth"
        if name == "Seren":
            namelist[namelist.index(name)] = "Serenity"
        if name == "Square":
            namelist[namelist.index(name)] = "Squarewave"


     


    HTML = '''
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>character.html</title>
    </head>
    <body bgcolor="#0e4603" text="#ffffff">
    <br>
    '''
    savename = namelist.pop(0)
    HTML += "<div align='center'><big><big> "+savename
    print savename
    for name in namelist:
        HTML += ", "+name 
    namelist.insert(0, savename)
    HTML += "</big></big></div> <br>"
    for name in namelist:
        HTML += "<img src='"+image[name]+"'><br><br><br>"
    HTML += "Pages in which your character(s) appear(s): <br>"
    pagelist1 = dnames[namelist[0]]
    pagelist = []
    if len(namelist) == 2:
        pagelist2 = dnames[namelist[1]]
        pagelist = set(pagelist1).intersection(set(pagelist2))
    elif len(namelist) == 3:
        pagelist2 = dnames[namelist[1]]
        pagelist3 = dnames[namelist[2]]
        pagelist = set(pagelist1).intersection(set(pagelist2).intersection(set(pagelist3)))
    elif len(namelist) == 4:
        pagelist2 = dnames[namelist[1]]
        pagelist3 = dnames[namelist[2]]
        pagelist4 = dnames[namelist[3]]
        pagelist = set(pagelist1).intersection(set(pagelist2).intersection(set(pagelist3).intersection(set(pagelist4))))
    else:
        pagelist=pagelist1
    
    if len(pagelist) == 0:
        HTML += "Sorry, they do not appear anywhere together"

    for x in pagelist:
        HTML += "<a href='http://mspaintadventures.com/?s=6&p=00"+x+"'><font color='cyan'>"+x+"</a><br>"
    HTML += ''' </body>
    </html>'''
    return HTML

def createVarPage(num):
    return ""
    
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 1639)
    #app.run()


#css stuff
def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

        app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string


