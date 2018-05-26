import json
from random import randint

from settings import Settings

sets = Settings()

def check_guess(guess, goal_num, guess_counter):
	if sets.bp_mode == True:
		guess = guess['guess']
	if goal_num == guess:
		result = 'correct'
	else:
		result = gen_corrections(goal_num, guess, guess_counter)
	return result
	
def display_bulls_cows(guess, guess_counter, result):
	if sets.bp_mode == True:
		guess = guess['guess']
	bulls = result[0]
	cows = result[1]
	print('Guess ' + str(guess_counter) + '/' + str(sets.max_guesses) + 
	": " + guess + ' || Bulls: ' + str(bulls) + ' || Cows: ' + str(cows))
	
def display_error(): ###################
	print("Error. Try Again.")

def display_rules():
	print("-----------------------------------------")
	print("Goal Number: ####")
	print("Attempt to guess what the goal number is!")
	print("A 'Bull' means that a number is in the correct location!")
	print("A 'Cow' mean that a number is correct but in the wrong" +  
		" location!")
	print("Begin by entering a 4 digit number:")
	
def display_victory_message():
	result = 'win'
	if sets.bp_mode != True:
		f.update_save(result)
	print("Correct! Great job!")
	
def display_win_rate(win_data):
	print("Win Rate: " + str(win_data['win_rate']) + "% " + 
		str(win_data['success_count']) + " Wins " + 
		str(win_data['failure_count']) + " Losses")

def game_over(goal_num):
	result = 'loss'
	if sets.bp_mode != True:
		f.update_save(result)
	print("Correct Answer: " + goal_num)
	print("Better luck next time!")
	
def gen_corrections(goal, guess, guess_counter):
	bulls = 0
	cows = 0
	for char in guess:
		if (char in goal) and (goal.index(char) == guess.index(char)):
			bulls += 1
		elif (char in goal):
			cows += 1
	result = str(bulls) + str(cows)
	return result
	
def gen_goal_num():
	if (sets.bp_mode == True) and (sets.bp_static_goal_num == True):
		goal_num = sets.bp_goal_num
	else:	
		goal_num = ''
		for i in range(4):
			while True:
				num = str(randint(0, 9))
				if num not in goal_num:
					goal_num += num
					break
	return goal_num
	
def get_user_guess():
	while True:
		user_guess = input()
		if guess_is_valid(user_guess):
			break
	return user_guess

def get_win_data(data):
	win_data = data
	wins = data['success_count']
	losses = data['failure_count']
	win_rate = ((wins + losses)/wins) * 100
	win_data['win_rate'] = win_rate
	return win_data

def guess_is_valid(guess):
	if guess == 'win_rate':
		data = load_save()
		win_data = get_win_data(data)
		display_win_rate(win_data)
		save_win_rate(win_data)
		return False
	elif len(guess) != 4:
		print("Entry must be 4 numbers long. Try again!")
		return False
	else:
		for char in guess:
			if guess.count(char) > 1:
				print("Entry can only contain unique numbers." +
				" Try again!")
				return False
			if (ord(char) < 48) or (ord(char) > 57):
				print("Entry can only contain numbers. Try again!")
				return False 
	return True
	
def load_save():
	with open('save.txt', 'r') as f_obj:
		data = json.load(f_obj)
		return data
		
def load_win_data():
	with open('win_rates.txt', 'r') as f_obj:
		data = json.load(f_obj)
		return data

def save_win_rate(win_data):
	data = load_win_data()
	if data[-1] != win_data:
		data.append(win_data)
		with open('win_rates.txt', 'w') as f_obj:
			json.dump(data, f_obj)

def update_save(result):
	with open('save.txt', 'r') as f_obj:
		data = json.load(f_obj)
		if result == 'win':
			data['win_count'] += 1
		elif result == 'loss':
			data['loss_count'] += 1
	with open('save.txt', 'w') as f_obj:
		json.dump(data, f_obj)
