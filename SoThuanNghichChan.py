def check(n):
    n = str(n)
    if n != n[::-1] or len(n) % 2 != 0: return False
    for i in n:
        if ord(i) % 2 != 0: return False
    return True
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        for i in range(22, n, 2):
            if check(i): print(i,end=' ')
        print()