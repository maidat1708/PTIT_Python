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
        cnt = 0
        for i in range (p - 6):
            if Prime[i] and Prime[i+6]:
                if Prime[i+4] or Prime[i+2]: cnt+=1
        print(cnt)