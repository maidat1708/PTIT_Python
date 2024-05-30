n,m = [int(x) for x in input().split()]
arr = list()
for i in range(n):
    a = [int(x) for x in input().split()]
    arr.append(a)
if n > m:
    cnt = n - m
    for i in range(n):
        if i % 2 ==0 and cnt > 0:
            cnt -= 1
            continue
        else:
            for j in range(m):
                print(arr[i][j], end=' ')
            print()
elif m > n:
    cnt = m - n
    k = 1
    for i in range(n):
        while cnt > 0:
            cnt -= 1
            arr[i].pop(k)
            k += 1
        cnt = m-n
        k = 1
    for i in range(n):
        for j in range(len(arr[i])):
            print(arr[i][j],end=' ')
        print()
else:
    for i in range(n):
        for j in range(len(arr[i])):
            print(arr[i][j],end=' ')
        print()