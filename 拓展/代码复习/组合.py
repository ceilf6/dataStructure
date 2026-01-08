n,m=map(int,input().split())

a=[i for i in range(1,n+1)]
#组合的话就用vis对应a即可
vis=[0]*n
result=[]
def dfs(step):
    if step==n:
        if sum(vis)==m:
            ans=[]
            for i in range(len(vis)):
                if vis[i]==1:
                    ans.append(a[i])
            result.append(ans)
        return


    #不用for了，直接用step：for i in range(step,n):
    vis[step]=1
    dfs(step+1)
    vis[step]=0
    dfs(step+1)

dfs(0)
print(result)
