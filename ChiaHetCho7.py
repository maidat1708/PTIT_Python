t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    ok = 1
    for i in range (1000):
        if n % 7 == 0:
            print(n)
            ok = 1
            break
        s1 = n
        s2 = int(str(n)[::-1])
        n = s1 + s2
    if ok == 0: print(-1)
