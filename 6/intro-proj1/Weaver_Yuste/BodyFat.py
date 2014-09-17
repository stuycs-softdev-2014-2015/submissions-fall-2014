from flask import Flask

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

print age
print weight

    
