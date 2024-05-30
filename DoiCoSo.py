import math
P =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H',
	'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t = int(input())
while t > 0:
    t -= 1
    n, k = [int(x) for x in input().split()]
    s=''
    while n > 0:
        u = n%k
        n = int(n/k)
        s += P[u]
    s = s[::-1]
    print(s)
