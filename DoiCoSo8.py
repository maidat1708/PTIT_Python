import math

s = input()
s = s[::-1]
s1=''
i = 0
while i < len(s):
    sum = 0
    for j in range (0, 3, 1):
        sum += int(math.pow(2, j))*int(s[i])
        i += 1
        if i == len(s): break
    s1 += str(sum)
    if i == len(s): break
s1 = s1[::-1]
print(s1)

# hoac
# print(oct(int(input(), 2))[2:]) 