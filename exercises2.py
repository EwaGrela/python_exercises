"""
some very simple exercises from python 
"""

# making a new list from an old one with only first and last items
list1 = [5, 10, 15, 20, 25]

def first_last(li):
  new_list =[];
  new_list.append(li[0])
  new_list.append(li[len(li)-1])
  return new_list

print first_last(list1);

# testing on another list:
list2 = [x for x in range(1,15) if x % 2 ==0]
print list2
print first_last(list2)


#checking if number is prime:
number = raw_input("Write in a number: ")

def make_integer(input):
  return int(input)

number = make_integer(number)

def find_divisors(num):
  divisors = [];
  for i in range(1,num+1):
    if num % i == 0:
      divisors.append(i)
  return divisors

def check_prime(num):
  divisors = find_divisors(num)
  if num ==1 or num ==2:
    return True
  elif len(divisors) == 2 and divisors[0]==1 and divisors[len(divisors)-1]==num:
    return True
  else:
    return False

print check_prime(number)

# summ list

def sum_list(li):
  total = 0;
  inter = []
  for i in li:
    total = total + i;
    inter.append(total);
  return inter
print sum_list([1,2,3,4])

# remove duplicates NOT using set
def remove_dup(li):
  singles =[]
  for i in li:
    if i not in singles:
      singles.append(i)
  return singles

print remove_dup([1,2,2,3,3,3,4,4,4,4])

sentence = raw_input("put in a sentence to reverse it")
def new_word_order(sent):
  sent = sent.split(" ")[::-1]
  sent = " ".join(sent)
  print sent
new_word_order(sentence)



