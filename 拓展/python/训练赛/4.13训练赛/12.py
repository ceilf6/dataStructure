n=int(input())

a=list(input().split())


res=[]
vis=[0]*n
b=[0]*n
def dfs(step):
    if step==n:
        b2=b.copy()
        s=''.join(b2)
        res.append(int(s))
        return

    for i in range(n):
        if vis[i]==0:
            b[step]=a[i]
            vis[i]=1
            dfs(step+1)
            vis[i]=0

dfs(0)

summ=0
def pf(x):
    return x**2

for i in res:
    summ+=i**2


flag=0
result=[]
vis=[0]*int(len(res)/2)
m=len(res)/2
def dfs2(step):
    if step==n:
        if sum(vis)==m:
            ans=[]
            for i in range(len(vis)):
                if vis[i]==1:
                    ans.append(res[i])
            result.append(ans)
        return

    vis[step]=1
    dfs(step+1)
    vis[step]=0
    dfs(step+1)
dfs2(0)
print(result)





    
