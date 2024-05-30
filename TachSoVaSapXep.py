import re

t = int(input())
ds = []
while t > 0:
    t -= 1
    s = input()
    arr = [int(x) for x in re.findall('\d+', s)]
    for i in arr:
        ds.append(i)
ds.sort()
for i in ds:
    print(i)
