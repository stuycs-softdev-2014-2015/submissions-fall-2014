The mission of our program is to find the main man, woman, and setting in a short story. While it will work best with Sherlock Holmes' stories (we got ours from Project Gutenberg), it will probably work just as well with any other English 19th-century writing. (For our purposes, the main man/woman/place is the one that is found with most frequency in the given story)

We use re.findall and regular expressions to find all names that start with 'Miss' or 'Sir' and are followed by one or two capitalized words (names). We place these in a dictionary, the name being the key and it's frequency the value, and then print out the name with the most frequency, for both the sirs and misses.

To find the main place, we used finditer. We named the second group of our regex function place_type, this being the second word in location names like Baker Street or Scotland Yard. We then created a list of possible place types (Yard, Street, Avenue, Court, etc.) and looked for matches in our text that had one capitalized word followed by another that was found in our place type list. We then put these in a dictionary and returned the one with most frequency.

If you want to look at the dictionaries for any of the three categories, look at places_dict, misses_dict, and sirs_dict. 
One problem; situations when the story says 'Miss Adler' and 'Miss Irene Adler'. We could fix this by naming the third group in three-word names last_name, and making sure there aren't repetitions of these in our dictionry. 
