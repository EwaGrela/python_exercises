def swap_case(s):
  s = list(s)
  newS = [];  
  for i in s:
    if i.isupper():
      i = i.lower()
      newS.append(i)
    elif i.islower():
      i = i.upper()
      newS.append(i)
    else:
      newsS.append(i)
  s = "".join(newS)
  return s


print(swap_case("MaMa"));