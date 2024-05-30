import math

class PS:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        uc = math.gcd(self.tu,self.mau)
        x = self.tu/uc
        y = self.mau/uc
        print (str(int(x)) + "/" + str(int(y)))
x,y = [int(x) for x in input().split()]
ps = PS(x,y)
ps.rutgon()