import re

File = open('thePrince.txt', 'r')
book = File.readlines()
file.close

def find_names(x):
    re.search('[A-Z]{1}[a-z]+/s[A-Z]{1}[a-z]+',x)


if __name__ == "__main__":
    find_names(book)
