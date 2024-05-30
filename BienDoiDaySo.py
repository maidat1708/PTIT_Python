while True:
    a,b,c,d = [int(x) for x in input().split()]
    if a == 0 and b == 0 and c == 0 and d == 0: break
    e = a
    cnt = 0
    while a != b or c != d or b != c or c != d:
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - e)
        e = a
        cnt += 1
    print(cnt)