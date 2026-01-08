def jifen(f,a,b,n):#a,b区间的f函数的积分，n越大越精细
    h=(b-a)/n
    total=sum(f(a+i*h) for i in range(1,n))
    total=(0.5*(f(a)+f(b))+total)*h
    return total

def f(x):
    return 1

print(jifen(f,1,3,1000))
