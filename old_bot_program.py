from random import randint

def guess(attempt_counter, current_index, result):
	print("Index before guess: " + str(current_index))
	num_guess = '1234'
	if attempt_counter == 1: # Occurs during first round
		pass
	elif result == '00' and current_index == -1: #No bulls/cows first round
		num_guess = '5678'
	elif result[0] != '0' and current_index != -1:
		high_num = num_guess[current_index + 1]
		reduced_num = (str(int(high_num) - 1))
		num_guess = num_guess.replace(high_num, reduced_num)
		print("TO BE REPLACED: " + num_guess[current_index])
		print("TO BE ADDED: " + high_num)
		num_guess = num_guess.replace(num_guess[current_index], high_num)
		current_index -= 1
		print("NUM GUESS: " + num_guess)
	elif result[0] != '0' and current_index == -1: # Bull detected
		num_data = find_bull_loc_guess(num_guess, current_index, result)
		num_guess = num_data['num_guess']
		current_index -= 1
	print("Index after guess: " + str(current_index))
	return num_guess, current_index, high_num, #####

def find_bull_loc_guess(num_guess, current_index, result):
	num_data = {}
	num_data['new_num'] = get_next_high_num(num_guess, current_index)
	num_data['old_num'] = num_guess[current_index]
	num_data['num_guess'] = num_guess.replace(old_num, new_num)
	return num_data

def get_next_high_num(num_guess, current_index):
	high_num = '0'
	for char in num_guess:
		if ord(char) > ord(high_num):
			high_num = char
	high_num = str(int(char) + 1)
	return high_num

