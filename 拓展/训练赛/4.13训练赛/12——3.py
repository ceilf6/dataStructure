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

total=sum([x**2 for x in res])
target=total//2
m=len(res)//2
result=[]
found=0
def dfs2(step,count,curr,path):
    global found
    if found:
        return
    if count>m or curr>target:
        return
    if count==m:
        if curr==target:
            for i in path:
                print(i)
            found=1
        return
    if step>=len(res):
        return
    dfs2(step+1,count+1,curr+res[step]**2,path+[res[step]])
    dfs2(step+1,count,curr,path)
dfs2(0,0,0,[])
