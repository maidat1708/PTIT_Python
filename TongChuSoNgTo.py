import math


def Ngto(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0: return False
    return n>1
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        s = input()
        sum=0
        for x in s:
            sum += int(x)
        print("YES") if Ngto(sum) else print("NO")