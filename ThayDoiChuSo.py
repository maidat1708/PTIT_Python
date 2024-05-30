t = int(input())
while t > 0:
    t -= 1
    x1,x2 = [str(x) for x in input().split()]
    s1 = input().strip()
    if s1.count(" "):
        s1,s2 = s1.split()
    else: s2 = input()
    print(int(s1.replace(x2, x1)) + int(s2.replace(x2, x1)),end=' ')
    print(int(s1.replace(x1, x2)) + int(s2.replace(x1, x2)))