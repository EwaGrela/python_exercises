"""
more exercises, cause practice makes perfect
"""
from random import randint
from time import sleep
# a game, you ask the computer to generate a random number in specified range and the you guess what it is
def play_game():
  welcome = "Can you guess a number a computer will generate?"
  goodbye = "Buh bye"
  success_msg = "You guessed it!"
  failure_msg = "You failed"
  error_msg = "Something went wrong"
  won_msg = "You won"
  lost_msg = "You lost"
  print welcome
  play = raw_input("Wanna play? Y/N: ").upper()
  if play == "Y":
	tries = raw_input("How many times do you want to play? ")
        tries = int(tries)
        possibilities = tries
#need to clone that one, cause i need numbers of tries twice, once it is mutable, once not
        num_range = raw_input("What is the highest number you want the computer to generate: ")
        num_range = int(num_range)
	winnings =0
	while tries>0:
  	  user_input = raw_input("Type a number, make sure it is : ")
	  user_input = int(user_input) 
          if user_input > num_range or user_input <1:
            print "Try again, number was bigger not in a specifies range"
          else:
	    print "Generating number..." 
	    random_num = randint(1, num_range)
	    sleep(2)
            tries -= 1
	    print random_num
	    if user_input ==random_num:
	      print success_msg
              winnings +=1
	    else:
	      print failure_msg
            if tries ==0:
              if winnings>possibilities/2:
                print won_msg
              else:
                print lost_msg           
  elif play =="N":
	  print goodbye
  else:
  	  print error_msg
play_game()







