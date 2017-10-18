import random
from time import sleep
def machine_guessing():
  error = "You exceeded the range"
  guess = "Yup, it is"
  miss = "Nope"
  computing_result = "We are now computing your result, Mr Robot"
  success = "You are good at guessing, Mr Robot"
  failure = "Sorry, Mr Robot..."
  print "Hello, you will now play guessing name against a machine"
  rounds = int(raw_input("How many round do you want there to be: "))
  tries = rounds
  # yeah, clone this one, cause round will decrement and you will need their initial value
  limes = raw_input("Please specify the biggest number: ")
  limes = int(limes)
  print limes
  machine_score = 0
  while rounds > 0:
    human_num = int(raw_input("Choose the number: "))
    if human_num > limes:
      print error
    else:
      print "Machine will now try to guess your number"
      machine_num = random.randint(1,limes)
      sleep(1)
      print "Hi human, is it %r ?"  % machine_num
      if machine_num == human_num:
        print guess
        machine_score +=1
        rounds -=1
      else:
        print miss
        rounds -=1
    if rounds ==0:
      print computing_result
      sleep(1)
      if machine_score> tries/2:
        print success
      else:
        print failure    
machine_guessing()
    
  
