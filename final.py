#function defining
def calculate_c(n,t,lst_s,lst_d,c):
    ti = 0
    for i in range(n):
        if c + lst_s[i] <= 0:
            return false
        else:
            ti += lst_d[i]/(lst_s[i] + c)
    return t > ti

#input n, t, s[i], d[i]
lst_s = []
lst_d = []
l = list(map(int,input().split()))
n = l[0]
t = l[1]
for i in range(n):
    a = list(map(int,input().split()))
    lst_d.append(a[0])
    lst_s.append(a[1])

#Binary search
low = -1e3
high = 1e6 + 1e3
while high - low > 1e-6:
    mid = (high + low)/2
    #function call
    if calculate_c(n,t,lst_s,lst_d,mid):
        high = mid
    else:
        low =mid
print ("{0:.6f}".format(mid))
