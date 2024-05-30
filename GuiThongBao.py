n = int(input())
while n > 0:
    n -= 1
    s = input()
    if (len(s) <= 100): print(s)
    else:
        k = 99
        while s[k] != ' ': k -= 1
        s = s[:k]
        print(s)