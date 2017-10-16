"""
simple game of coin tossing
"""
from random import randint
from time import sleep
results = ["heads", "tails"];
options = {"H": "heads", "T":"tails"}
bad_news = "You poor soul...so sorry..."
good_news = "You won! Yay!"
tie = "It's a tie"
def play_game():
	print "Welcome to head or tails!"
	user_choice = raw_input("Heads or tails? Choose H for heads and T for tails: ").upper()
	user_choice = options[user_choice]
	print "You chose %r" % user_choice
	print "Wait for the computer to decide..."
	computer_choice_index = randint(0, len(results)-1)
	sleep(2)
	computer_choice = results[computer_choice_index]
	print "The computer chose %r" % computer_choice
	print "Time for a coin toss..."
	coin_toss_index = randint(0, len(results)-1)
	sleep(2)
	coin_toss = results[coin_toss_index]
	print "The winning one is %r" % coin_toss
	determine_winner(user_choice, computer_choice, coin_toss)


def determine_winner(user_choice, computer_choice, coin_toss):
	print user_choice
	print computer_choice
	print coin_toss
	if user_choice == coin_toss and user_choice != computer_choice:
		print good_news
	elif user_choice == computer_choice:
		print tie
	elif computer_choice == coin_toss and user_choice != computer_choice:
		print bad_news
	else :
		print "Something is not quite right, try again!"
	
	
play_game();