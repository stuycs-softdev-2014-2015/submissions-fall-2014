<h1> Regex Name Finder </h1>
by Brian and Matt 

How to use:
Run in your terminal by issuing this command:
    '''
    python findnames.py <filename without extension>
    '''
    
For example, if your text file was testtext.txt, you would run this:
    '''
    python findnames.py testext
    '''

NOTE: Names with Mr. and Mrs. are kept by our name finder.
NOTE: There may be false positives with proper nouns which are not composed of more than two english words.
   e.g. "The Secret Service" would not be considered a name, but "Cenozoic Era" and "New York" would not. 
