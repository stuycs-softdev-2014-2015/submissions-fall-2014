from flask import Flask,render_template

app = Flask(__name__)


file_object = open('data.txt','r')
age = []
weight = []
i = 0
for line in file_object:
    x = line.replace('\t','').replace('\n','').split(',')
    age.append(x[0])
    weight.append(x[1])
    i += 1

file_object.close()

@app.route("/")
@app.route("/home") 
def home():
    return render_template("home.html", age = age, weight = weight)


if __name__ == "__main__":
    app.debug=True
    app.run()
