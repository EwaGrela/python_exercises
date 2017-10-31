def count_substr(string, substr):
  sb_len = len(substr)
  count = 0
  for i in range(0, len(string)):
    if string[i: i+sb_len] == substr:
      count +=1
  return count
  
  



    