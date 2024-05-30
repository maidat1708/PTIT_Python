def toHop(n):
    return int(giaiThua(n)/giaiThua(n-2)/2)
def giaiThua(k):
     sum =1
     for i in range(1,k+1): sum*=i
     return sum;
if __name__ =='__main__':
    n = int(input())
    ds=list()
    cnt = 0
    for i in range(n):
        s = input()
        ds.append(s)
        if s.count('C') >= 2: cnt += toHop(s.count('C'))
    for i in range(n):
        dem = 0
        for j in range(n):
            if ds[j][i] == 'C' : dem+=1
        if dem >=2 : cnt += toHop(dem)
    print(cnt)


