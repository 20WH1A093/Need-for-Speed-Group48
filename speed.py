n, t = input().split()
lst_d = []
lst_s = []
for i in range(0, int(n)):
    d, s = input().split()
    lst_d.append(int(d))
    lst_s.append(int(s))
def calculate_c(c):
    ti = 0
    for i in range(0, int(n)):
        if(c+lst_s[i]<=0):
            return 0
        else:
            ti+=lst_d[i]/(c+lst_s[i])
        if(ti>int(t)):
            return 0
        else:
            return 1
low = -1e3
high = 1e6+1e3
while(high-low<1e-6):
    mid = (high+low)/2
    if calculate_c(mid):
        high = mid
    else:
        low = mid
print("{0:.6f}".format(calculate_c(mid)))
