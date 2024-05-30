s = input()
n = len(s)
s = s[::-1]
res = ''
for i in range ( n ):
    res += s[i]
    if (i+1) % 3 == 0: res += ','
res = res[::-1]
print(res[1:]) if res[0] == ',' else print(res)