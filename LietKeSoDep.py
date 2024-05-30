import math
def isReversible(s):
    if len(s)%2!=0 : return False
    if s != s[::-1]: return False
    for x in s :
        if int(x)%2!=0 : return False
    return True
if __name__ == '__main__':
    t = int (input())
    while t >0:
        t-=1
        s = int(input())
        for i in range (10,s,2):
            if isReversible(str(i)) :print(i,end=' ')
        print()