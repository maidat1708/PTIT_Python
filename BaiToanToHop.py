import math
n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr = set(arr)
arr = list(arr)
arr.sort()
n= len(arr); pos = -1
res = [0 for i in range(k)]
check = [False for i in range(n)]
def toHop(i):
    global pos
    for j in range(n):
        if check[j] == False and j> pos :
            pos = j
            check[j]= True
            res[i] = arr[j]
            if i == k-1 :
                for h in range(k): print(res[h],end =' ')
                print()
            else: toHop(i+1)
            check[j] = False
            pos = -1
toHop(0)