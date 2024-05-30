def tong(n):
    x = 0
    u = n % 10
    n = int(n/10)
    while n > 0:
        x += u
        if abs(u - n % 10) != 2: return -1
        else: u = n % 10
        n = int(n/10)
    x += u
    return x

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        k = tong(n)
        if k == -1: print("NO")
        elif k % 10 == 0: print("YES")
        else: print("NO")


