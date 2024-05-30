# Ý tuỏng
'''
    Ta có tổng dãy số liên tiếp của: 1, 2, 3, ... n có dạng = (1+n)(n-1+1)/2. Tổng quát hơn nó là: = (r+l)(r-l+1)/2; với: l, l+1, ... r;
    Ta thấy rằng N = (r+l)(r-l+1)/2 <=> N*2 = (r+l)(r-l+1);
    Coi
    r+l = x;
    r-l+1 = y;
    => 2*N = x*y => x, y là ước của 2*n (x, y nguyên).
    -> Liệt kê các ước của 2*N;
    Với mỗi ước thu được là x -> y=N/x; -> Giải hệ tìm được r, l; -> kiểm tra r, l xem có thỏa man không rồi đếm.
'''
t = int(input())
for k in range(t):
    n,s = 2*int(input()),0
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            x,y = int(n/i),i
            k = x + y -1
            if k % 2 == 0:
                r = int(k/2)
                l = x - r
                if r > l and r >= 1: s += 1
    print(s)