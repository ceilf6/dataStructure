t=int(input())

def ans(a):
    n=len(a)
    s=0
    for i in range(1,n+1):
        s+=i*a[i-1]
    return s

for _ in range(t):
    q=int(input())
    a=[]
    for i in range(q):
        c=list(map(int,input().split()))
        if c[0]==3:
            a.append(c[1])
            print(ans(a))
        elif c[0]==1:
            a=[a[-1]]+a
            del a[-1]
            print(ans(a))
        elif c[0]==2:
            a=list(reversed(a))
            print(ans(a))

