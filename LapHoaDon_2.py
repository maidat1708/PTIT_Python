from datetime import datetime
class K:
    def __init__(self,id,name,phong,dongia,ngay,phi):
        self.id = "KH%02d" %id
        self.name = name
        self.phong = phong
        self.ngay = ngay
        self.cost = dongia*ngay + phi
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phong} {self.ngay} {self.cost}'
def songay(vao,ra):
    time = (datetime.strptime(ra, "%d/%m/%Y") - datetime.strptime(vao, "%d/%m/%Y")).days+ 1
    return time
t = int(input())
ds = []
for i in range(t):
    name = input().strip()
    phong = input().strip()
    if phong[0] == '1': dongia = 25
    if phong[0] == '2': dongia = 34
    if phong[0] == '3': dongia = 50
    if phong[0] == '4': dongia = 80
    ngay = songay(input().strip(),input().strip())
    phi = int(input())
    ds.append(K(i+1,name,phong,dongia,ngay,phi))
ds.sort(key = lambda x: -x.cost)
for i in ds:
    print(i)
