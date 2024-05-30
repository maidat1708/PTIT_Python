n = input()
while len(n) > 1:
    n1 = n[0:int(len(n)/2):]
    n2 = n[int(len(n)/2)::]
    sum = int(n1) + int(n2)
    n = str(sum)
    print(n)