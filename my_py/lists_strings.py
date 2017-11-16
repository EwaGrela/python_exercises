# -*- coding: utf-8 -*
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
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
  return str*n
print(string_times("hi", 5))
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""
def front_times(str, n):
  if len(str)>=3:
    return str[0:3]*n
  else:
    return str*n
print(front_times("hi", 5))
print(front_times("chocoloco", 5))
"""
Given a string, return a new string made of every other char 
starting with the first, so "Hello" yields "Hlo".
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
  return str[0::2]
print(string_bits("hello"))
print(string_bits("lala"))

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
  goal ="";
  x =0;
  while x<len(str)+1:
    goal = goal + str[0:x]
    x+=1
  return goal
print(string_splosion("abc"))
