t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    ds = []
    maxx=0
    for i in range(1001):
        ds.append(0)
    for i in range(n):
        x = int(input())
        ds[x] += 1
        maxx = max(ds[x],maxx)
    for i in range(1001):
        if ds[i] == maxx:
            print(i)
            break