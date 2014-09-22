# Miscellanous useful functions

def headerify_string(s):
	word_list = s.split()
	new_word_list = [word.capitalize() for word in word_list]
	final = ' '.join(new_word_list)
	return final