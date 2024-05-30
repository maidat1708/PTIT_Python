import re

t = int(input())
while t > 0:
    t -= 1
    s = input()
    listnum = re.findall(r'\d+',s)
    listnum = [int(x) for x in listnum]
    print(min(listnum))
