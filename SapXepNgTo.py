import math


def nt(n):
    if n < 2: return False
    if n < 4: return True
    for i in range (2,int(math.sqrt(n)+1)):
        if n % i == 0: return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
b = list()
check = [0 for i in range(len(a))]
for i in range(0,len(a)):
    if not nt(a[i]): check[i] = 1
    else: b.append(a[i])
b.sort(reverse=True)
for i in range(len(a)):
    if check[i] == 1: print(a[i],end=' ')
    else:
        print(b[len(b)-1],end=' ')
        b.pop()
