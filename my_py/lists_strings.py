"""
Given a string, return a string where for every char in the original, there are two chars.
"""
def double_char(str):
  str = list(str)
  return "". join([x*2 for x in str])
print(double_char("mama"))

"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(str):
  res = 0;
  l = len("hi")
  for i in range(len(str)):
    if str[i: i+l] == "hi":
    	res +=1
  return res
print(count_hi("hihihahi"))

"""
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
import re
def count_code1(str):
  sub = "co[a-zA-Z]e"
  p = re.compile(sub)
  l= p.findall(str)
  return len(l)
  
print(count_code1("aaacodebbb"))
print(count_code1("aaacodecozecopebbb"))

# one more time, but without regex
def count_code(str):
  count = 0;
  for i in range(len(str)-3):
  	if str[i:i+2]=="co" and  str[i+2].isalnum() and str[i+3]=="e":
  	  count+=1
  return count
print(count_code1("aaacodebbb"))
print(count_code1("aaacodecozecopecodecofe cozebbb   cose"))
  	
"""
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.
"""
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a)==len(b):
  	if a == b:
  	  return True;
  	else:
  	  return False
  elif len(a)>len(b):
  	for i in range(len(a)):
  	  if b ==a[-len(b)::]:
  	  	return True
  	  else:
  	  	return False
  elif len(b)>len(a):
  	for i in range(len(b)):
  	  if a == b[-len(a)::]:
  	  	return True
  	  else:
  	  	return False
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

"""
Return True if the string "cat" and "dog" 
appear the same number of times in the given string.
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
print("cat_dog")
def cat_dog(str):
  sub1 = "cat"
  sub2 ="dog"
  occ_cat =0;
  occ_dog = 0;
  for i in range(len(str)):
    if str[i:i+len(sub1)] ==sub1:
      occ_cat +=1
    elif str[i:i+len(sub2)] ==sub2:
      occ_dog +=1

  if occ_dog == occ_cat:
    return True
  else:
  	return False

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))

"""
Return the number of even ints in the given array. 
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(nums):
  evc = 0;
  for num in nums:
  	if num%2 ==0:
  	  evc +=1
  return evc
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([3,4,5,8,7,3]))

"""
Given an array length 1 or more of ints, 
return the difference between the largest and smallest values in the array. 
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""

def big_diff(nums):
  return max(nums) - min(nums)
print(big_diff([10, 3, 5, 6]))