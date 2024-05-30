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
        if not NgTo(len(s)): print("NO")
        else:
            x2 = s.count('2')
            x3 = s.count('3')
            x5 = s.count('5')
            x7 = s.count('7')
            x = x2 + x3 + x5 + x7
            print("YES") if x > int(len(s)/2) else print("NO")