import functions as funcs # Contains all game functions
import bot_program_0 as bp # Contains all bot functions
from settings import Settings # Contains all settings

# Initialize Settings class
sets = Settings()

# Display rules once
funcs.display_rules()

# Main Program
while True:
	# Generate a secret number which must be guessed
	goal_num = funcs.gen_goal_num()
	
	# Keep track of how many guesses have been made
	guess_counter = 1
	
	# Bull Cow Counter (bcc) keeps track of how many of each are known
	# Used to report values to user and by bot to make decisions
	bcc = {'bulls': 0, 'cows': 0}
	
	# Individual Game Program
	while True:
		
		# Player runs out of guesses
		if guess_counter > sets.max_guesses:
			funcs.game_over(goal_num)
			break
			
		# Bot Program Mode ACTIVE (Bot generates guesses) 
		if sets.bp_mode == True:
			# Initialize bot's guess_data for guess #1
			if guess_counter == 1:
				guess_data = sets.guess_data
			# Generate bot's guess and save it along with metadata
			guess_data = bp.get_bot_guess(guess_data)
		# Bot Program Mode INACTIVE (User generates guesses)
		else:
			user_guess = funcs.get_user_guess()
		
		# Check if the guess is correct or return # of cows and bulls	
		if sets.bp_mode == True:
			result = funcs.check_guess(guess_data, goal_num,
				guess_counter)
		else:
			result = funcs.check_guess(user_guess, goal_num,
				guess_counter)
		
		# Result was CORRECT
		if result == 'correct':
			funcs.display_victory_message()
			break
		# Result was INCORRECT	
		else:
			# Display # of bulls and cows
			if sets.bp_mode == True:
				funcs.display_bulls_cows(guess_data, guess_counter,
					result)
				# Update guess_data for bot to generate new guess
				bp.update_guess_data(guess_data, result)
			else:
				funcs.display_bulls_cows(user_guess, guess_counter, result)

		# Guess incorrect therefore increment guess counter	
		guess_counter += 1
		
	# Game has ended and user is asked to play again	
	answer = input("Would you like to play again? (yes/no) \n").lower()
	# User does not wish to play again
	if answer == 'no':
		break
