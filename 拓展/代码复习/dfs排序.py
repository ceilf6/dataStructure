n=int(input())

vis=[0]*n
a=[i for i in range(1,n+1)]
print(a)
result=[]
b=[0]*n

def dfs(step):
    if step==n:
        b2=b.copy()#注意得copy，否则result里面都是b最后的形态
        result.append(b2)
        return

    for i in range(n):
        if vis[i]==0:#未使用
            b[step]=a[i]
            vis[i]=1
            dfs(step+1)
            vis[i]=0

dfs(0)

print(result)
