n,m,q=map(int,input().split())

ma=[[1]*m for i in range(n)]

s=[]
for i in range(q):
    s.append(list(map(int,input().split())))

for i in range(q):
    if s[i][0]==0:
        for j in range(m):
            ma[s[i][1]-1][j]=0
    else:
        for j in range(n):
            ma[j][s[i][1]-1]=0

ans=0
for i in range(n):
    ans+=sum(ma[i])
print(ans)
