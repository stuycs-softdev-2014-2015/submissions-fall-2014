from flask import Flask, render_template
import csv


more_stuff = ['False Advertising','Noise, Ice Cream Truck (NR4)','MOLD', 'Loud Music/Party', 'Pothole','Graffiti', 'VERMIN','Chemical Vapors/Gases/Odors','Food Spoiled','E3A Dirty Area/Alleyway','Car/Truck Horn','Congestion/Gridlock','Chemical Vapors/Gases/Odors','Condition Attracting Rodents']

stuff=['Gender Pricing','Time Clock Maladjusted','Unauthorized Climbing','Pigeon Odor','Beekeeping - Honeybees','Farm Animal','Decorative Necklace Lighting','Minor Received Tattoo','Harassment','Snake']

borough = ["MANHATTAN","QUEENS","BRONX","STATEN ISLAND","BROOKLYN"]
dborough = {"MANHATTAN":"Manhattan","QUEENS":"Queens","BRONX":"Bronx","STATEN ISLAND":"Staten+Island","BROOKLYN":"Brooklyn"}


data=[line for line in csv.reader(open("2013.csv","rU"))]
aprildata=[line for line in csv.reader(open("april2013.csv","rU"))]

html_list = []
html_list_two = []

maps = Flask(__name__)

@maps.route("/maps")
def mapspage():
    mapsx(data,stuff)
    other_maps(data,['Sewage Leak'])
    other_maps(aprildata,more_stuff)
    return render_template("maps.html",html_list=html_list,html_list_two=html_list_two)


def make_map(data,value):
    result = ""
    for item in data:
        if item[1] == value and item[3] != "" and item[3]!= " ":
            result+= "&markers=color:blue%7C"+item[3][1:-1]
    return 'http://maps.googleapis.com/maps/api/staticmap?center=Ridgewood,Queens,New+York,NY&zoom=10&size=640x640&maptype=roadmap'+result+'&sensor=false'

def mapsx(data,listy):
    for item in listy:
        html_list.append("These are the 311 calls for "+item+" in 2013.")
        html_list.append(""+make_map(data,item))
        
def make_other_maps(data,value):
    result = ""
    maplist=[]
    for item in borough:
        for stuff in data:
            if stuff[1] == value and stuff[2] == item and stuff[3] != "" and stuff[3]!= " ":
                result+= "&markers=color:blue%7C"+stuff[3][1:-1]
        maplist.append('http://maps.googleapis.com/maps/api/staticmap?center='+dborough[item]+',New+York,NY&zoom=11&size=640x640&maptype=roadmap'+result+'&sensor=false')
        result = ""
    return maplist


def other_maps(data,listy):
    for item in listy:
        html_list_two.append("These are the 311 calls for "+item+" in 2013.")
        maplist=make_other_maps(data,item)
        for mapurl in maplist:
             html_list_two.append(""+mapurl)


if __name__=="__main__":
    maps.debug = True
    maps.run()


