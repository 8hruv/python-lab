import random
n = int(input())
l = 10**(n-1)
u = 10**n - 1
res = random.randrange(l, u)
print(res)