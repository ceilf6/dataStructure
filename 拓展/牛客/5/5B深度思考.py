N=int(input())

for i in range(N):
    n,t,k=map(int,input().split())

    rem=n-k

    if rem<t:
        print(0)
        continue

    else:
        maxx=rem//t
        maxx=min(maxx,k+1)#最多也是k次分割
        print(maxx)
