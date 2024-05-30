import math


def isPrime(n):
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return n>1
def isPerfectPrime(n):
    if not isPrime(n): return False
    if not isPrime(int(str(n)[::-1])): return False
    sum = 0
    n = str(n)
    for i in n:
        if i!='2' and i !='3' and i !='5' and i !='7': return False
        sum += int(i)
    return isPrime(sum)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        print("Yes") if isPerfectPrime(n) else print("No")