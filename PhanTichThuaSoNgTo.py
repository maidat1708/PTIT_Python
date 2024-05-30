if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        print("1 * ", end='')
        i = 2
        while i*i <= n:
            cnt = 0
            ok = 0
            while n % i == 0:
                cnt += 1
                n = int(n/i)
                ok = 1
            if ok == 1: print(str(i) + "^" + str(cnt), end='')
            if n > 1 & ok == 1: print(" * ",end='')
            i += 1
        print(str(n) + "^1") if n > 1 else print()
