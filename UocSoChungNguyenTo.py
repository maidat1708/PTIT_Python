import math

prime = [True for i in range(100000)]
prime[0] = prime[1] = False
def eratosthenes():
    i = 2
    while i*i < 1000000:
        if prime[i]==True:
            for j in range (2*i,100000,i): prime[j] = False
        i+=1
if __name__ == '__main__' :
    eratosthenes()
    t = int(input())
    while t >0 :
        t-=1
        a,b = [int(a) for a in input().split()]
        ucln = math.gcd(a,b)
        s = 0
        while int(ucln) >0 :
            s += int (ucln%10)
            ucln/=10
        print('YES') if prime[s] else print('NO')
