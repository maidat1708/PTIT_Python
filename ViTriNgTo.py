import math
def isPrime(n):
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0 : return False
    return n>1
def ViTriNgTo(s):
    for i in range(len(s)):
        if isPrime(i) and isPrime(int(s[i]))==False: return False
        if isPrime(i)==False and isPrime(int(s[i])): return False
    return True
if __name__ == '__main__':
    t = int (input())
    while t > 0 :
        t-=1
        s = input()
        print('YES') if ViTriNgTo(s) else print('NO')

