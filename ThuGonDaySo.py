if __name__ == '__main__':
    t = int(input())
    s = input()
    s = s.split()
    st = []
    i = 0
    while t > 0:
        t -= 1
        x = int(s[i])
        i += 1
        if len(st) > 0:
            if x + st[len(st)-1] %2 == 0: st.pop()
            else: st.append(x)
        else: st.append(x)
    print(len(st))