f1 = open(r'C:\Users\Lenovo\Documents\pythonProject\Python - CodePTIT\SOTAY.txt')
class TT:
    def __init__(self,name,sdt,date):
        self.date = date
        self.sdt = sdt
        self.name = name
s = []
n = 0
for x in f1:
    if x.startswith("Ngay"):
        arr = x.split(" ")
        date = str(arr[1])
    elif x[0] == '0':
        sdt = x
        if date == "":
            date = s[n-1].date
        n += 1
        s.append(TT(name[:len(name)-1],sdt[:len(sdt)-1],date[:len(date)-1]))
    else:
        name = x
for i in range(n):
    print(s[i].name + ": " + s[i].sdt +" "+ s[i].date)