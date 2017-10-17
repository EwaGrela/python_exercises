"""
a program asking for a number from a range then returning its divisors

"""
user_input = int(raw_input(" Enter a number from 1 to 1000: "))

def find_divisor(number):
  if number <1 or number >1000:
  	print "The number must be from 1 to 100"
  else:
  	divisors = [];
  	for int in range(1,number+1):
  	  if number % int ==0:
  	    divisors.append(int)
  	return divisors

print find_divisor(user_input)