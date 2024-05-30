import re

s = ""
regex = '[\w\s,:]+'
while True:
    try : s += input()
    except EOFError : break
print(s)
# s = re.findall(regex, s)
# for i in s:
#     x = i.lower().split()
#     x[0] = x[0].title()
#     print(' '.join(x))