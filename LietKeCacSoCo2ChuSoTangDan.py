n = input()
if len(n) % 2 !=0: n = n[:len(n)-1]

a = set()
for i in range (0,len(n),2):
    s = n[i] + n[i+1]
    a.add(int(s))
a = list(a)
a.sort()
for i in a:
    print(i,end=' ')