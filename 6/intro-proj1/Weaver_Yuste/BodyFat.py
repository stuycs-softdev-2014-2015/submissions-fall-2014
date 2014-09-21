from flask import Flask,render_template

app = Flask(__name__)


file_object = open('data.txt','r')
age = []
weight = []

i = 0
for line in file_object:
    x = line.replace('\t','').replace('\n','').split(',')
    age.append(int(x[0]))
    weight.append(float(x[1]))
    i += 1
file_object.close()

avgs = {}

i = 0
while( i < len(age)):
    if avgs.has_key(age[i]) == False:
        avgs[age[i]] = weight[i]
        num = 1
        j = i + 1
        while( j < len(age)):
            if age[i] == age[j]:
                num = num + 1
                avgs[age[i]] += weight[j]
            j =  j + 1
        avgs[age[i]] = round( (avgs[age[i]]) / num , 3)
        i = i + 1
    else:
        i = i + 1


@app.route("/")
@app.route("/home") 
def home():
    return render_template("home2.html", avgs = avgs)


if __name__ == "__main__":
    app.debug=True
    app.run()
