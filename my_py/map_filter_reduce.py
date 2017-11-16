print("map filter reduce")
lis = [1,2,3,4]
lis2 = list(map(lambda x:x*2, lis))
print(lis2)

lis3 = [ x*3 for x in lis]
print(lis3)
lis4 = list(map(lambda x: x*5, lis))
print(lis4)
lis5 = list(filter(lambda x: x>=10, lis4))
print(lis5)
lis6 = list(filter(lambda x: x %2 ==0, lis4))
print(lis6)