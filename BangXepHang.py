import functools

class SV:
    def __init__(self,name,ac,sub):
        self.name = name
        self.ac = ac
        self.sub = sub
def cmp(a , b):
    if a.ac < b.ac: return 1
    elif a.ac == b.ac: 
        if a.sub > b.sub: return 1
        elif a.sub == b.sub:
            if a.name > b.name: return 1
            else: return -1
        else: return -1
    else: return -1
n = int(input())
a = []
for i in range(n):
    name = input()
    ac,sub = [int(x) for x in input().split()]
    a.append(SV(name,ac,sub))
a.sort(key=functools.cmp_to_key(cmp))
for i in a:
    print(i.name, i.ac, i.sub)
