import math

if __name__ == '__main__' :
    t = int(input())
    while t >0 :
        t-=1
        s = input()
        ok = 0
        s = list(s)
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                ok= 1
                break
        print('YES') if ok ==0 else print('NO')


