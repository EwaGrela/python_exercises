def print_formatted(input):
  width = len(bin(input)[2::])
  for i in range(1, input+1):
    print(str(i).rjust(width, " "), str(oct(i))[2::].rjust(width, " "), str(hex(i))[2::].upper().rjust(width, " "), str(bin(i))[2::].rjust(width, " "))


print_formatted(17);