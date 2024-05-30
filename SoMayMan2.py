t = int(input())
while(t>0):
    s = input()
    a = s.count('4');
    b = s.count('7')
    c = a + b
    t=t-1
    print('YES') if c == len(s) else print('NO')


