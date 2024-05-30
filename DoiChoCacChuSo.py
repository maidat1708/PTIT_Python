t = int(input())
while t > 0 :
    t -= 1
    s = input()
    x = 0
    x1 = 0
    ktra = 0
    for i in range(len(s)-2,-1,-1):
        for j in range(i+1,len(s),1):
            if s[i] > s[j]:
                x = i
                x1 = j
                ktra = 1
                break
        if ktra == 1: break
    if ktra == 0: print("-1")
    else:
        k = x1
        p = s[x1]
        for i in range (x+1,len(s),1):
            if s[x] > s[i] and p < s[i]:
                p = s[i]
                k = i
        s1 =''
        for i in range(len(s)):
            if i == x: s1 += p
            elif i == k: s1 += s[x]
            else: s1 += s[i]
        if s1[0] == '0': print("-1")
        else:
            print(s1)
