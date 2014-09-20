from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/count/<title>")
def count(title):
    try:
        f = open("./files/" + title + ".txt", "r")
    except IOError:
        return render_template("error.html")
    raw_string = f.read()
    word_dict = wordCount(raw_string)
    word = mostCommonWord(word_dict)
    return render_template("count.html", title=title, word=word, word_dict=word_dict)

@app.route("/submit", methods = ["POST", "GET"])
def submit():
    #DO STUFF HERE
    submitted = False
    if request.method == "POST":
        f = request.files['file']
        f.save("./files/"+secure_filename(f.filename));
        submitted = True
    return render_template("submit.html", submitted=submitted)

def wordCount(raw_string):
    words = {}
    for word in string.split(raw_string):
        if not (word in words):
            words[word] = 0
        words[word] += 1
    return words
        
def mostCommonWord(dict_words):
    max_count = 0
    common_word = ""
    for word,count in dict_words.iteritems():
        if max_count < count:
            max_count = count
            common_word = word
    return common_word

if __name__ == "__main__":
    app.run(debug=True)
