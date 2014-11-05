# Edit the password requirements to suit needs.
PASSWORD_REQUIREMENTS = {
	'chars': 6,
	'uppers': 1,
	'numbers': 1
}

def valid_password(password):
	chars_hit = len(password) >= PASSWORD_REQUIREMENTS['chars']

	num_uppers = sum([char.isupper() for char in password])
	uppers_hit = num_uppers >= PASSWORD_REQUIREMENTS['uppers']

	num_nums = sum([char.isdigit() for char in password])
	nums_hit = num_nums >= PASSWORD_REQUIREMENTS['numbers']

	print chars_hit, uppers_hit, nums_hit
	return chars_hit and uppers_hit and nums_hit