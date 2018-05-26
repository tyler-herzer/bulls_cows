class Settings():
	def __init__(self):
		
		# Game Settings
		self.max_guesses = 8
		
		# Bot Settings
		self.bp_mode = False
		self.bp_static_goal_num = True
		self.bp_goal_num = '0758'
		
		# Initial guess data - Update locations listed below
		self.guess_data = {
			'guess': '0123', # get_bot_guess() main.py
			'bcc': '', # update_guess_data() main.py
			'guess_counter': 1, # update_guess_data() main.py
			'current_index': -1, 
			'new_num': 0,
			'old_num': 0,
			}
