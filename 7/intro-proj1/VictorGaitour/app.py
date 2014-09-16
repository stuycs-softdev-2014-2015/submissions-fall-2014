from flask import Flask
# app is an instance of the Flask class
app = Flask(__name__)
if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()
    
