import math
def isPrime(n):
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0 : return False
    return n>1
if __name__ == '__main__':
    t = int (input())
    while t > 0 :
        t-=1
        s = input()
        sum = 0
        for i in range(0,len(s),2): sum += int(s[i])
        mul = 1; ok =0
        for i in range(1,len(s),2):
            if int(s[i])!=0 :
                ok=1
                mul *= int(s[i])
        print(sum,end=' ')
        print(0) if ok == 0 else print(mul)