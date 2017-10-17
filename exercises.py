# filtering using lambda
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_input = int(raw_input("write in a number: "))
print filter(lambda x: x<user_input, nums)

# finding overlapping part of lists
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def find_overlap(l1,l2):
  overlap = []
  for int1 in l1:
    for int2 in l2:
      if int1 == int2:
      	overlap.append(int1)
  return overlap
print find_overlap(list1, list2) # [1,2,3,5,8,13]

#checking if string is a palindrome
string_to_check = raw_input("Write in a word and check if its palindrome: ")
def check_if_palindrome(string):
  reversed = string[::-1]
  if string == reversed:
  	return True
  else:
  	return False
print check_if_palindrome(string_to_check)

#returning only even numbers from a list - list comprehension
list3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list4 = [x for x in list3 if x %2 ==0]
print list4
# return overlapping in list using list comprehension
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in a  if x in b]
print c
