import math
a,k,n = [int(a) for a in input().split()]
i = int(a/k) + 1
sum = a
if i*k > n : print(-1)
while i*k<=n:
    print(i*k-a,end=' ')
    i=i+1
