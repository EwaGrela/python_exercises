"""
a simple game of dice, you roll and guess how many pints there will be,
if there are more or the same amont - you win 
"""

from random import randint
from time import sleep

def get_user_guess():
    user_guess = int(raw_input("pick a number and write it in"))
    return user_guess
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print "you can get maximum of" + str(max_val) + " points"
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
    	print 'yo, that is too much'
        return
    else:
        print "Rolling..."
        sleep(2)
        print "This is %d " % first_roll
        sleep(1)
        print "This is %d " % second_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "The sum of rolls is: " + total_roll
        sleep(1)
        if user_guess > total_roll:
            print "You win, you crazy son of a bitch"
            return
        else :
            print "You lost, try again"
            return
roll_dice(6)