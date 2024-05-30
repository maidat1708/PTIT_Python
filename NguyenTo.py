import math

prime = [True for i in range(10000)]
prime[0] = prime[1] = False
def eratosthenes():
    i = 2
    while i*i < 10000:
        if prime[i]==True:
            for j in range (2*i,10000,i): prime[j] = False
        i+=1
if __name__ == '__main__' :
    eratosthenes()
    t = int(input())
    while t >0 :
        t-=1
        n = int(input()); cnt = 0
        for i in range(1,n):
            if math.gcd(i,n) == 1: cnt += 1
        print('YES') if prime[cnt] else print('NO')