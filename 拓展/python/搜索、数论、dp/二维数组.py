n,m,a,b=map(int,input().split())

mapp=[[] for i in range(n)]

for i in range(n):
    listt=list(map(int,input().split()))
    mapp[i]=listt

print(mapp[1][2])
