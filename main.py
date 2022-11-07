import random

def main():
	print("Welcome to rock, scissors papers, the classic game. You may now choose between the following options (please type your imput, you may stop the game by typing 'end' without quotes).")
	run_game()

def choose_options():
	options = ("rock", "scissors", "paper")
	user = input("Rock, paper or scissors? --> ").lower()

	if user == "end":
		print("The game has been aborted. Quitting means you lost!")
		exit()

	if not user in options:
		print("The option you chose is not rock, paper nor scissors, please select a valid option.")
		return None, None

	pc = random.choice(options)
	print("User choice:", user.capitalize())
	print("Computer choice:", pc.capitalize())
	return user, pc

def print_next_round(user_wins, pc_wins, rounds):
	print("*" * 20)
	print("ROUND", rounds)
	print("*" * 20)
	print("Your wins -->", user_wins)
	print("Computer wins -->", pc_wins)

def check_winner(user, user_wins, pc, pc_wins):
	if user == pc:
		print("Tie!")
	elif user == "scissors":
		if pc == "paper":
			print ("Scissors win paper")
			print("You win this round!")
			user_wins += 1
		else:
			print("Rock wins scissors")
			print("You lose this round!")
			pc_wins += 1
	elif user == "rock":
		if pc == "paper":
			print ("Paper wins rock")
			print("You lose this round!")
			pc_wins += 1
		else:
			print("Rock wins scissors")
			print("You win this round!")
			user_wins += 1
	else:
		if pc == "scissors":
			print ("Scissors win paper")
			print("You lose this round!")
			pc_wins += 1
		else:
			print("Paper wins rock")
			print("You win this round!")
			user_wins += 1
	return user_wins, pc_wins

def who_wins(user_wins, pc_wins):
	if user_wins ==  2:
		print("*" * 20)
		print("You won the game!")
		print("*" * 20)
		exit()
	elif pc_wins ==  2:
		print("*" * 20)
		print("You lost the game!")
		print("*" * 20)
		exit()

def run_game():
	user_wins = 0
	pc_wins = 0
	rounds = 1

	while True:
		print_next_round(user_wins, pc_wins, rounds)
		user, pc = choose_options()

		if user == None:
			rounds += 1
			continue

		user_wins, pc_wins = check_winner(user, user_wins, pc, pc_wins)
		who_wins(user_wins, pc_wins)
		rounds += 1

main()
