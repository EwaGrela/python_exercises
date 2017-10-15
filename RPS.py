"""
this programm is a paper-rock-scissors game
"""
from random import randint
from time import sleep
options = ["R", "P", "S"]
lost_message = "YOU LOST, SUCKER"
winning_message = "YAY, YOU WIN"
def decide_winner(user_choice, computer_choice):
  print "you chose %s: " % user_choice
  print "Computer selecting ..."
  sleep(1)
  print "the machine chose %s: " % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "Its a tie"
  elif user_choice_index ==0 and computer_choice_index ==2:
      print winning_message
  elif user_choice_index ==1 and computer_choice_index ==0:
    print winning_message
  elif user_choice_index ==2 and computer_choice_index ==1:
    print winning_message
  elif user_choice_index > 2:
    print " It must be a value between 0 and 2"
  else:
    print lost_message
    
def play_RPS():
  print "This is RPS game"
  user_choice = raw_input("Choose your tool Select R for Rock, P for Paper, or S for Scissors:")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = options[randint(0, len(options)-1)]
  decide_winner(user_choice, computer_choice)
   
play_RPS();