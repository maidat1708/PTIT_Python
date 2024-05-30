P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
str=list(P)
while True:
    s=input()
    arr = s.split()
    k=int(arr[0])
    if k==0: break
    a = arr[1]
    res=''
    for i in a:
        pos = P.index(i)
        res+=str[(pos+k)%28]
    print(res[::-1]) # res[::-1] tao ra mot list dao ngc lai vs res 