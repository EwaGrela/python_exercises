def make_out_word(out, word):
  return out[0:2:1]+ word + out[2::]

print(make_out_word("<<>>", "lala"))
print(make_out_word("....", "dodo"))
print("_"*30)

def first_half(str):
  return str[0:int(len(str)/2):1]
print(first_half("dodo"))
print("_"*30)

def without_end(str):
  return str[1:int(len(str)-1):1]
print(without_end("Trojanowska"))

print("_"*30)

def combo_string(a, b):
  if len(a)>len(b):
  	return b+a+b
  elif len(b)>len(a):
  	return a+b+a

print(combo_string("hi", "hello")) #hihellohi
print(combo_string("hello", "hi")) #hihellohi
print(combo_string("dada", "lol"))
print(combo_string("lol", "dada"))

print("_"*30)

def non_start(a, b):
  return a[1::]+b[1::]
print(non_start("hello", "there"))

print("_"*30)

def left2(str): #left2('Hello') → 'lloHe'
  return str[2::]+str[0:2:1]
print(left2("Hello"))

print("_"*30)

def extra_end(str): #extra_end('Hi') → 'HiHiHi' extra_end('Hello') → 'lololo'
  return str[-2::]*3
print(extra_end("Hello"))
print(extra_end("Hi"))

print("_"*30)
"""
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""
def first_last6(nums):
  if nums[0] ==6 or nums[len(nums)-1]==6:
    return True
  else:
    return False

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))

print("_"*30)

def same_first_last(nums):
  if len(nums)>0 and nums[0] ==nums[len(nums)-1]:
  	return True
  else:
  	return False

print(same_first_last([1, 2, 3])) # False
print(same_first_last([1, 2, 3, 1])) # True
print(same_first_last([1, 2, 1])) # True
print(same_first_last([]))

print("_"*30)

def common_end(a, b):
  if (a[0]==b[0] or a[len(a)-1]== b[len(b)-1]) and (len(a) and len(b)>0):
  	return True
  else:
  	return False
print(common_end([1,2,3], [1,2,3]))

print("_"*30)

def rotate_left3(nums):
  return nums[1::]+nums[0:1:]
print(rotate_left3([3,2,1]))
print(rotate_left3([5, 11, 9]))

print("_"*30)

def max_end3(nums):
  if nums[0]> nums[len(nums)-1]:
  	nums = [nums[0] for num in nums]
  elif nums[0] == nums[len(nums)-1]:
  	nums = [nums[0] for num in nums]
  elif nums[0] < nums[len(nums)-1]:
  	nums = [nums[len(nums)-1] for num in nums]
  return nums
print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))

print("_"*30)

def sum2(nums):
  if len(nums)>=2:
  	return nums[0] + nums[1]
  elif len(nums) ==1:
  	return num[0]
  else:
  	return 0
sum2([1, 2, 3]) 
sum2([1, 1]) 
sum2([1, 1, 1, 1]) 

print("_"*30)

def middle_way(a, b):
 return a[1:2:1]+b[1:2:1]
print(middle_way([1, 2, 3], [4, 5, 6])) # [2,5]

print("_"*30)

def make_ends(nums):
  return nums[0:1:1]+ nums[int(len(nums)-1)::]
print(make_ends([7, 4, 6, 2]))

print("_"*30)

def has23(nums):
  if 2 in nums or 3 in nums:
  	return True
  else:
  	return False

