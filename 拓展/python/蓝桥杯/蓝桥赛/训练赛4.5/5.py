n,m=map(int,input().split())

mapp=[[] for i in range(n)]

for i in range(n):
    mapp[i]=list(map(int,input().split()))

for i in range(m):
    for j in range(n):
        print(mapp[n-j-1][i],end=' ')
    print()
