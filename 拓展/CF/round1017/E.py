t=int(input())

for i in range(t):
    n=int(input())

    a=list(map(int,input().split()))

    #预处理
    ans=[[0]*(n-i) for i in range(n)]


    for j in range(n):
        for z in range(j,n):
            ans[j][z]=a[j]^a[z]


    maxx=0
    for k in range(n):
        now=0
        for z in range(k):
            now+=ans[z][k]
        for z in range(k+1,n):
            now+=ans[k][z]

        maxx=max(now,maxx)



    print(maxx)
