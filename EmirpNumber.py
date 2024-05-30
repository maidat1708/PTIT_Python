Prime = [True for i in range(1000000)]
Prime[0] = Prime[1] = False
def sangnt():
    i = 2
    while i*i < 1000000:
        if Prime[i] == True:
            for j in range (i*i,1000000,i): Prime[j]=False
        i+=1
if __name__ == '__main__':
    t = int(input())
    sangnt()
    while t > 0:
        t -= 1
        p = int(input())
        for i in range (12,p):
            x = int(str(i)[::-1])
            if i < x and x < p and Prime[i] and Prime[x]: print(i, x, end=' ')
        print()