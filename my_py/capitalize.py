def capitalize(string):
  string = string.split(" ")
  newStr = []
  for word in string:
    word = word.capitalize()
    print (word)
    newStr.append(word)
    string = " ".join(newStr)
  return string
print(capitalize("hello world"))


arr = [1,2,6,5,4,6]
print (arr[::-1])
arr = sorted(arr);
arr = list(set(arr))
arr = arr[::-1]
print(arr)