t= int(input())
while(t>0):
    t-=1
    n=input()
    if int(n) < 10 :
        print(n)
    size = len(n)
    n=list(n)
    for i in range (size-1,0,-1):
        if int(n[i])>=5 : n[i-1]=str(int(n[i-1])+1)
        n[i]='0'
    print("".join(n))
