import math
t = int(input())
while t > 0:
    t -= 1
    s = input()
    a = int(s)
    s = s[::-1]
    b = int(s)
    print("YES") if math.gcd(a,b) == 1 else print("NO")
