import random
print('Hey player! Guess your number between 0-10 ')
TOTAL_TRY = 3
COMPUTER_NUMBER = ''
def get_random_number():
		global COMPUTER_NUMBER
		COMPUTER_NUMBER = random.randint(0,10)
get_random_number()
		
def get_player_input():
	print(f'You have only {TOTAL_TRY} attempt')
	player_input = input('Guess your Number : ')
	if player_input == str(COMPUTER_NUMBER):
		print('Hurry! YOU WIN')
	if player_input != str(COMPUTER_NUMBER):
	 def calculate_wrong_count():
	 	global TOTAL_TRY
	 	TOTAL_TRY -= 1
	 	if TOTAL_TRY > 0:
	 		get_player_input()
	 	elif TOTAL_TRY == 0:
	 		print('Game Over! Ohh Computer win.')
	 		print(f'Computer guessed number is {COMPUTER_NUMBER}')
	 	else:
	 		print('ok nothing happend')
	 calculate_wrong_count()  	
get_player_input()
