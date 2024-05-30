import math
def myfunc(x):
    x = str(x)
    sum = 0
    for i in x: sum += int(i)
    return sum
if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        n= int(input())
        arr = [int(x) for x in input().split()]
        arr.sort()
        arr.sort(key=myfunc)
        for i in arr: print(i,end = ' ')
        print()





