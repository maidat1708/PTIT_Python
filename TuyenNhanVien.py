import functools
class SV:
    def __init__(self,cnt,name,lt,th):
        self.name = name
        self.id = "TS0" + str(cnt)
        self.lt = lt
        self.th = th
        self.tb = None
        self.loai = None
    def tinhdiem(self):
        tb = (self.lt + self.th)/2
        self.tb = tb
        if tb < 5: self.loai = "TRUOT"
        elif tb < 8: self.loai = "CAN NHAC"
        elif tb <= 9.5: self.loai = "DAT"
        else: self.loai = "XUAT SAC"
    def output(self):
        print(self.id , self.name ,"{:0.2f}".format(self.tb),self.loai)  
def cmp (a,b):
    if a.tb < b.tb: return 1
    return -1
t = int(input())
a=[]
for i in range(t):
    name = input()
    lt = float(input())
    th = float(input())
    if lt > 10: lt /= 10
    if th > 10: th /= 10
    a.append(SV(i+1,name,lt,th))
for i in a:
    i.tinhdiem()
a.sort(key=functools.cmp_to_key(cmp))
for i in a:
    i.output()
