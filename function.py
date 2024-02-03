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
