with open ("primes.txt", "r") as f:
  primes = f.read()


with open("happy.txt", "r") as g:
  happy = g.read()

primes = str(primes)
happy = str(happy)

primes = primes.split("\n")
happy = happy.split("\n")

print type(primes)
print type(happy)

overlap = [];
for num1 in primes:
  for num2 in happy:
    if num1 == num2:
      overlap.append(num1)
print overlap
   