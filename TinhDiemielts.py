def diem(a):
    if a <= 2: return 0.0
    elif a <= 4: return 2.5
    elif a <= 6: return 3.0
    elif a <= 9: return 3.5
    elif a <= 12: return 4.0
    elif a <= 15: return 4.5
    elif a <= 19: return 5.0
    elif a <= 22: return 5.5
    elif a <= 26: return 6.0
    elif a <= 29: return 6.5
    elif a <= 32: return 7.0
    elif a <= 34: return 7.5
    elif a <= 36: return 8.0
    elif a <= 38: return 8.5
    else:
        return 9.0
def ktra(tong):
    nguyen = int(tong)
    du = float(tong - nguyen)
    if du == 0.5 or du == 0: return 0
    if du == 0.25 or du == 0.75: return 0.25
    if du < 0.25: return -du
    if du < 0.5 and du > 0.25: return 0.5-du
    if du > 0.5 and du < 0.75: return 0.5-du
    if du > 0.75: return 1-du

t = int(input())
while t > 0:
    t -= 1
    a,b,c,d = [float(x) for x in input().split()]
    a = int(a); b = int(b)
    listening = diem(a)
    reading = diem(b)
    tong = listening + reading + c + d
    tong /= 4
    print(tong + ktra(tong))
