import math
t = int(input())
while t>0:
    t=t-1
    n,x,m = [float(x) for x in input().split()]
    mu = m/n
    x = 1+x/100
    val = math.log(mu,x)
    res = int(val)
    if val - res >0 : res+=1
    print(res)


