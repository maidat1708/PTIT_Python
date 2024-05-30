t = int(input())
while t>0:
    a=input()
    s=list(a)
    for i in range (0,len(s),1):
        if int(i)%2!=0:
            for j in range (0,int(s[i]),1):
                print(s[i-1],end="")
    print()
    t-=1
