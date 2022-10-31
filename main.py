import random

options = ("rock", "scissors", "paper")
print("Welcome to rock, scissors papers, the classic game. You may now choose between the following options (please type your imput, you may stop the game by typing 'end' without quotes).")

user_wins = 0
pc_wins = 0
rounds = 1

while True:
	print("*" * 10)
	print("ROUND", rounds)
	print("*" * 10)
	print("Your wins -->", user_wins)
	print("Computer wins -->", pc_wins)

	user = input("Rock, paper or scissors? --> ").lower()

	if user == "end":
		print("The game has been aborted. Quitting means you lost!")
		break

	if not user in options:
		print("The option you chose is not rock, paper nor scissors, please select a valid option.")
		continue

	rounds += 1
	pc = random.choice(options)
	print("User choice:", user.capitalize())
	print("Computer choice:", pc.capitalize())

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
	elif user == "paper":
		if pc == "scissors":
			print ("Scissors win paper")
			print("You lose this round!")
			pc_wins += 1
		else:
			print("Paper wins rock")
			print("You win this round!")
			user_wins += 1

	if user_wins ==  2:
		print("*" * 18)
		print("You won the game!")
		print("*" * 18)
		break
	elif pc_wins ==  2:
		print("*" * 18)
		print("You lost the game!")
		print("*" * 18)
		break
