import math
n, k = [int(x) for x in input().split()]
cnt = 0
a = int(math.pow(10, k-1))
b = int(math.pow(10, k))
for i in range(a,b):
    if math.gcd(n,i) == 1:
        cnt+=1
        print(i, end=' ')
    if cnt % 10 == 0: print()
