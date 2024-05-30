class SV:
    def __init__(self,id,name,lop):
        self.name = name
        self.id = id
        self.lop = lop
        self.diem = 10
    def tinhdiem(self,s):
        for i in s:
            if i == 'v': self.diem -= 2
            elif i == 'm': self.diem -= 1
        if self.diem < 0: self.diem = 0
    def output(self):
        print(self.id , self.name , self.lop, self.diem,end=" ")  
    
t = int(input())
a=[]
for i in range(t):
    a.append(SV(input(),input(),input()))
for i in range(t):
    id,cc = map(str,input().split())
    for i in a:
        if i.id == id:
            i.tinhdiem(cc)
            break
for i in a:
    i.output()
    if i.diem == 0: print("KDDK")
    else: print()
