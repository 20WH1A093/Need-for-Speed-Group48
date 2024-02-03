def calculate_c():

    #input
    n, t = input().split()
    lst_d=[]
    lst_s=[]
    t1 = []
    for i in range(0,int(n)):
        d,s = input().split()
        lst_d.append(int(d))
        lst_s.append(int(s))
        t1.append(int(d)/int(s))

    #finding total time w.r.t speedometer readings
    T = sum(t1)

    #average actual speed of the journey
    sum_d = (sum(lst_d))
    S = ((sum_d/int(t)))

    #average speedometer speed of the journey
    s1 =(sum_d/T)

    #error
    c = S - s1
    return c

print(calculate_c())
