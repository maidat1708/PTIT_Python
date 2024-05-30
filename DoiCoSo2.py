import math
f = "0123456789ABCDEF"
f = list(f)
t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = input()
    n = int(math.log(n)/math.log(2))
    while len(s)%n!=0: s = '0' + s
    for i in range(0, len(s), n):
        u = 0
        for j in range(i, i+n):
            if s[j]=='1': u+=int(math.pow(2,n-j+i-1))
        print(f[u], end="")
    print()
