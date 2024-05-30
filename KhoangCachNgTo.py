Prime = [True for i in range(1000000)]
Prime[0]=Prime[1]=False
dp = []
def sangnt():
    i = 2
    while i*i < 1000000:
        if Prime[i] == True:
            for j in range(i*i,1000000,i): Prime[j]=False
        i += 1
    for i in range(2,1000000):
        if Prime[i]==True: dp.append(i)
if __name__ == '__main__':
    sangnt()
    n,x=[int(i) for i in input().split()]
    print(x,end=' ')
    for i in range(n):
        x = x + dp[i]
        print(x,end=' ')