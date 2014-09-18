from flask import Flask,render_template

app = Flask(__name__)

data = open('pokemon.csv', 'r')
data = data.readlines()

@app.route('/')
def index():
    length = len(data)
    return render_template("index.html", 
                           data=data,
                           num=0,
                           length = str(len(data)))


@app.route('/info')
def info():
    return fill('pokemon.csv')

if __name__ == "__main__":
    app.debug=True
    app.run()
