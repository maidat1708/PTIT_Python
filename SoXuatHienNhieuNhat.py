import math
if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        n =int(input())
        a = [int(x) for x in input().split()]
        dic = {}
        for i in a:
            dic[i] = 0
        for i in a :
            dic[i] += 1
        cnt = max(dic.values())
        if cnt > n/2 :
            key_list=  list(dic.keys())
            val_list = list(dic.values())
            pos = val_list.index(cnt)
            print(key_list[pos])
        else : print('NO')





