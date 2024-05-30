import math


def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0: return False
    return n > 1

n = int(input())
a = [int(x) for x in input().split()]
arr = list()
sum1 = 0
sum2 = 0
for i in a:
    if arr.count(i) == 0:
        sum2+=i
        arr.append(i)
ktra = 0
for i in range(len(arr)):
    sum1 += arr[i]
    sum2 -= arr[i]
    if isPrime(sum1) and isPrime(sum2):
        ktra = 1
        print(i)
        break
if ktra == 0: print("NOT FOUND")