"""
more exercises, cause practice makes perfect
"""
from random import randint
from time import sleep

def play_game():
  welcome = "Can you guess a number a computer will generate?"
  goodbye = "Buh bye"
  success_msg = "You guessed it!"
  failure_msg = "You failed"
  error_msg = "Something went wrong"
  random_num = randint(1,9)
  points = 0;
  print welcome
  play = raw_input("Wanna play? Y/N: ").upper()
  if play == "Y":
  	user_input = raw_input("Type a number: ")
	user_input = int(user_input) 
	print "Generating number..." 
	sleep(2)
	print random_num
	if user_input ==random_num:
	  print success_msg
	else:
	  print failure_msg
  elif play =="N":
	  print goodbye
  else:
  	  print error_msg
play_game()







