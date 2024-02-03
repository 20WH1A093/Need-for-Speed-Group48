def calculate_c():
        n, t = input().split()
        lstd = []
        lsts = []
        for i in range(0, int(n)):
            d, s = input().split()
            lstd.append(int(d))
            lsts.append(int(s))
        #print(lstd)
        #print(lsts)
        sumd = sum(lstd)
        sums = sum(lsts)
        s1 = sumd/int(t)
        c = (s1 - sums)/int(n)
        return c
print(calculate_c())
