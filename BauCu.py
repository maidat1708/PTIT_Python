import math


n,k = map(int,input().split())
a = [int(x) for x in input().split()]
b = [0 for i in range(0, k+1)]
for i in a:
    b[i] += 1
max1 = 0
max2 = 0
for i in b:
    if max1 < i:
        max2 = max1
        max1 = i
    elif max2 < i and i != max1:
        max2 = i
if max2 == 0: print("NONE")
else :
    for i in range(1,k+1):
        if b[i] == max2:
            print(i)
            break
