from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    pass


if __name__ == "__main__":
    app.debug=True
    app.run(port = 5005)
    
