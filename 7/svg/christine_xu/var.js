1. 

var map=function(L,F){...}

map takes a list and a function and returns a new list where each element is 
the result of applying F on each element.

So, map([1,2,3,4,5],function(x){return x*x;}) would return [1,4,9,16,25]

2. 

var filter=function(L,F) {...}

filter takes a list and a function and returns a new list where only those elements that return true for F(e) will be in the new list.

So, filter([1,2,3,4,5,6],function(x) { return x%2==0;}) would return
[2,4,6]