n,m = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr1 = list(set(arr1))
arr1.sort()
arr2 = [int(x) for x in input().split()]
arr2 = list(set(arr2))
arr2.sort()
for i in arr1:
    if i in arr2: print(i,end=' ')
print()
for i in arr1:
    if i not in arr2: print(i,end=' ')
print()
for i in arr2:
    if i not in arr1: print(i,end=' ')
print()