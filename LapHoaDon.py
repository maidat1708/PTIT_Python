import math
import functools
class HD:
    def __init__(self,i,name,soM):
        self.id = "KH{:02d}".format(i)
        self.name = name
        self.soM = soM
        if soM <= 50: 
            self.dongia = 100
            self.phuphi = 2
        elif soM <= 100:
            self.dongia = 150
            self.phuphi = 3
        else:  
            self.dongia = 200
            self.phuphi = 5
    def cost(self):
        if self.soM <= 50:
            return round(self.dongia*self.soM) + int(self.dongia*self.soM*self.phuphi/100)
        elif self.soM <= 100:
            return round((5000 + int(self.dongia*(self.soM-50)))*1.03)
        else:
            return round((100*50 + 150*50 + 200*(self.soM - 100))*1.05)
    def toString(self):
        return self.id + " " + self.name + " " + str(self.cost())
def cmp(a,b):
    return b.cost() - a.cost()

t = int(input())
a = []
for i in range(t):
    a.append(HD(i+1,input(),abs(int(input())-int(input()))))
a.sort(key= functools.cmp_to_key(cmp))
for i in a:
    print(i.toString())
