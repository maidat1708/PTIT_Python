P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
P = list(P)
def tim(c):
    for i in range (0,26):
        if P[i] == c: return i
def chuyen(s):
    n = len(s)
    sum=0
    a=''
    for i in s: sum+=tim(i)
    for i in range(0,n): a += P[(tim(s[i])+sum)%26]
    return a
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        l = int(len(s)/2)
        s1 = s[:l]
        s2 = s[l:]
        s1=chuyen(s1);s2=chuyen(s2)
        s3=''
        for i in range (l):
            s3 += P[(tim(s1[i]) + tim(s2[i]))%26]
        print(s3)