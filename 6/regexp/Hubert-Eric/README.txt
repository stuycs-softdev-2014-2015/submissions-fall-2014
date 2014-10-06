Name Entity Recognizer
======================

Run NER.py and input the name of the text file to parse. 
Originally the code was a lot longer and used the NLTK library, but it was very heavy and slower than pure regex. Although in some cases it did provide better results.
I was also going to add learning so that unknown first names preceding known last names would be added (and vice verse), but that becomes a problem with parsing longer texts, because a lot of the time I ended up picking up beginnings of sentences,
quotes, etc...