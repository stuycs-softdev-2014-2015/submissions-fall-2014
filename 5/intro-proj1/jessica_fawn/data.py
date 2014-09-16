from flask import Flask

app = Flask (__name__)

@app.route ("/")
def home ():
    s = "test \n"
    data = open ("TSEV.csv", "r")
    data.readline()
    #for line in data:
        #s = s + line
    data.close()
    return s

if __name__ == "__main__":
    app.debug = True
    app.run()
