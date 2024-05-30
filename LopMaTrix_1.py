def multipy(a,b):
    c = []
    m = len(a)
    n= len(b)
    for i in range(m):
        arr =[ 0 for x in range(m)]
        c.append(arr)
    for i in range(m):
        for j in range(m):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    for i in range(m):
        for j in range(m): print(c[i][j],end=' ')
        print()

t = int(input())
while t>0:
    t-=1
    m,n = map(int,input().split())
    matrix = []
    for i in range(m):
        arr = [int(x) for x in input().split()]
        matrix.append(arr)
    transposed_matrix = []
    for i in range(n):
        arr =[]
        for j in range(m): arr.append(matrix[j][i])
        transposed_matrix.append(arr)
    multipy(matrix,transposed_matrix)
