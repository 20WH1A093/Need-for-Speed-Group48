def calculate_c(n,c,lst_s,lst_d,t):
    ti = 0
    for i in range(n):
        if(c + lst_s[i] <= 0):
            return 0
        else:
            ti += lst_d[i]/(lst_s[i] + c)
    if(ti > t):
        return 0
    else:
        return 1
lst_s = []
lst_d = []
l = list(map(int,input().split()))
n = l[0]
t = l[1]
for i in range(n):
    a = list(map(int,input().split()))
    lst_d.append(a[0])
    lst_s.append(a[1])
low = -1e3
high = 1e6 + 1e3
while(high - low > 1e-6):
    mid = (high + low)/2
    if(calculate_c(n,mid,lst_s,lst_d,t)):
        high = mid
    else:
        low =mid
print ("{0:.6f}".format((high+low)/2))

