import string

def alphabet_position(letter):
	#Determine the letter's position in the alphabet_position
	#Normalize the letter
	letter = letter.lower()
	position = string.ascii_lowercase.index(letter)
	return position


def rotate_character(char, rot):
	#Determine character to replace the original
	#This function will call alphabet_position
	lower = False
	upper = False
	if char in string.ascii_lowercase:
		lower = True
	elif char in string.ascii_uppercase:
		upper = True
	orig_letter = alphabet_position(char)
	new_position = (orig_letter + rot) % 26
	new_letter = string.ascii_lowercase[new_position]
	if lower == True:
		new_letter = new_letter.lower()
	elif upper == True:
		new_letter = new_letter.upper()
	return new_letter

def encrypt(text, rot):
	#Function to encrypt a message using substitution
	#This function will call rotate_character
	new_string = ""
	new_char = ""
	for each_char in text:
		if each_char not in string.ascii_lowercase and each_char not in string.ascii_uppercase:
			new_string += each_char
		else:
			new_char = rotate_character(each_char, rot)
			new_string += new_char
	return new_string
