t = int(input())
while t > 0:
    t -= 1
    n,m,l = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    x = y = z= 0
    check = 0
    while x < n and y < m and z < l:
        if a[x] == b[y] == c[z]:
            print(a[x], end=" ")
            check = 1
            x += 1
            y += 1
            z += 1
        elif a[x] <= b[y] and a[x] <= c[z]:
            x += 1
        elif b[y] <= a[x] and b[y] <= c[z]:
            y+=1
        elif c[z] <= b[y] and c[z] <= a[x]:
            z+=1
    if check == 0: print("NO")
    print()