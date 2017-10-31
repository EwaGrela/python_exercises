n = int(input())
m = int(input())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
diff = sorted(list(a.difference(b).union(b.difference(a))))
for i in diff:
  print(i)



