def check(s):
    s = list(s)
    n = len(s)
    if n < 3: return False
    i = 0
    while s[i+1] > s[i]:
        i += 1
        if i+1 == n: break
    if i == n-1: return True
    while s[i+1] < s[i]:
        i += 1
        if i+1 == n: break
    if i == n-1: return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        print("YES") if check(s) else print("NO")