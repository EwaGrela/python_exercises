"""
some more exercises
"""
list_to_look = [1,3,4,5,3,5,6,2]
print list_to_look
element = 1
element2 = 8
# nedd to find it it exists in the list, and return the right boolean

def check_if_element_in_list(li, element):
  li = sorted(li)
  for el in li:
    if element == el:
      return True
    else:
      return False
print check_if_element_in_list(list_to_look, element) # True
print check_if_element_in_list(list_to_look, element2) # False

