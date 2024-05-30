n,m = map(int,input().split())
b = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
a,cs = [],[]
for i in range(n):
    c = [int(x) for x in input().split()]
    a.append(c)
    for j in range(m):
        if c[j] == -1:
            cs.append([i,j])
sum = 0
while len(cs) > 0:
    u = cs[0]
    cs.pop(0)
    for i in b:
        imoi,jmoi = i[0] + u[0],i[1] + u[1]
        if imoi >= 0 and jmoi >= 0 and jmoi <= m and imoi <= n:
            if a[imoi][jmoi] != 0:
                sum += a[imoi][jmoi]
                a[imoi][jmoi] = 0
print(sum)