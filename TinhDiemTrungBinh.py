n = int(input())
ds = [float(x) for x in input().split()]
sum=0.0
maxx = 0.0
minn = 10.0
for i in ds:
    maxx = max(maxx,i)
    minn = min(minn,i)
cnt = 0
for i in ds:
    if i == maxx or i == minn: continue
    cnt+=1
    sum += i
print(round(sum/cnt,2))