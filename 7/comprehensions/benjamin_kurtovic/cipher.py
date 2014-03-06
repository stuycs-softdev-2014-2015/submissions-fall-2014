import math
import random

englishPercents=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,
                 6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,
                 5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];
englishPercents = [n / 100. for n in englishPercents]

def encode(s, n):
    """Rotate the string by n characters, leaving spaces."""
    r = [chr(((ord(x) - ord("a") + n) % 26) + ord("a")) if x != " " else x for x in s]
    return "".join(r)

def dist(a, b):
    """Calculate the distance between two points in any dimension."""
    return math.sqrt(sum(pow(a[i] - b[i], 2) for i in xrange(len(a))))

def calcPercents(s):
    """Returns a list of 26 elements: L[0] will be the frequency of the letter
    a in the list, L[1] the letter b etc."""
    return [float(s.count(chr(ord("a") + i))) / len(s) for i in xrange(26)]

def decode(enc, freqs):
    """Decode an encoded string using English letter frequencies."""
    freqs = [dist(calcPercents(encode(enc, i)), freqs) for i in xrange(26)]
    shift = freqs.index(min(freqs))
    return encode(enc, shift)

def read_shakespeare():
    """Read letter frequencies from a text file."""
    with open("shakespeare.txt", "r") as fp:
        text = fp.read()
    s = [c for c in text.lower() if ord("z") >= ord(c) >= ord("a")]
    return [float(s.count(chr(ord("a") + c))) / len(s) for c in xrange(26)]

def main():
    freqs = read_shakespeare()
    s = "this is a sample sentence for use in testing the ceasar cipher thing"
    print s
    encoded = encode(s, random.randrange(1, 26))
    print encoded
    decoded = decode(encoded, freqs)
    print decoded
    assert s == decoded

if __name__ == "__main__":
    main()
