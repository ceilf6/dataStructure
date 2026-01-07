t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    b=[0]*n
    cnt=[0]*30 #题目说了 0<= ai < 2**30
    for i in range(n):
        b[i]=bin(a[i])[2:].zfill(30)

    for i in range(30):
        for j in range(n):
            cnt[i]+=(b[j][i]=='1')

    maxx=0
    for i in range(n):
        ans=0
        for j in range(1,31):
            if b[i][-j]=='0':
                ans+=cnt[-j]*(2**(j-1))
            else:
                ans+=(n-cnt[-j])*(2**(j-1))
        maxx=max(ans,maxx)
    print(maxx)
