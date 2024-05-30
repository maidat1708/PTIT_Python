t = int(input())
while t>0 :
    t -= 1
    a=input()
    dem=1
    for i in range (0,len(a)-1,1):
        if a[i]==a[i+1]:
            dem+=1
        else:
            print(dem,end="")
            print(a[i],end="")
            dem=1
    print(dem,end="")
    print(a[len(a)-1])