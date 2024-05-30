import math
def NgTo(n):
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0 : return False
    return n>1
if __name__ == '__main__':
    t = int (input())
    while t > 0 :
        t-=1
        s = input()
        x1 = s[:3]
        x2 = s[len(s)-3:]
        print("YES") if NgTo(int(x1)) and NgTo(int(x2)) else print("NO")