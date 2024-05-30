Prime = [True for i in range(10001)]
Prime[0] = Prime[1] = False
s = []
maxx = 0
def sang():
    i = 2
    global s
    while i*i < 10001:
        if Prime[i] == True:
            for j in range( i*i, 10001,i):
                if Prime[j] == True: Prime[j] = False
        i += 1
    i = 2
    for i in range(2, 10000):
        if Prime[i] == True: s.append(i)
def buoc(n):
    for i in range(1, len(s)):
        if s[i] > n:
            a = abs(s[i] - n)
            b = abs(s[i-1] - n)
            return int(min(a,b))

t = int(input())
a = [int(x) for x in input().split()]
sang()
for i in a:
    if Prime[i] == True: continue
    else: 
        maxx = max(maxx,buoc(i))
print(maxx)
