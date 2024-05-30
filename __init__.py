n,m,k = map(int,input().split())
a = [[] for i in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    x,y = map(int,input().split())
    a[x].append(y)
    a[y].append(x)
st = []
st.append(k)
visit[k] = 1
while len(st) >0:
    u = st.pop()
    for i in a[u]:
        if visit[i] == 0:
            visit[i] = 1
            st.append(i)
for i in range(1,n+1):
    if visit[i] == 0:
        print(i)