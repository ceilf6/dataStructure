MOD=998244353
m=int(input())

A=list(map(int,input().split()))

f=[[]]

def dfs(step,k,n):
    if n==k:
        chose=[]
        for i in range(m):
            if vis[i]:
                chose.append(A[i])
        f.append(chose)
        return

    if step==m:
        return

    vis[step]=0
    dfs(step+1,k,n)
    vis[step]=1
    dfs(step+1,k,n+1)

    vis[step]=0

for i in range(1,m+1):
    vis=[0]*m
    dfs(0,i,0)

summ=0

for i in range(1,len(f)):
    maxx=max(f[i])
    minn=min(f[i])
    summ=(summ+maxx*minn)%MOD
print(summ)
    
