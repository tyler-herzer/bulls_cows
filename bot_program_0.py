from random import randint # Used to generate random #'s

def get_bot_guess(guess_data):
	"""
	Takes previous guess and meta data (bcc, etc) to generate a new 
	guess
	"""
	# First guess is always 0123
	if guess_data['guess_counter'] == 1:
		guess_data['guess'] = '0123'
		
		
	return guess_data

def update_guess_data(guess_data, result):
	guess_data['bcc'] = result
	guess_data['guess_counter'] += 1
