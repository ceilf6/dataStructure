def f(l,n):
    ans=0
    r=[0]*n
    c=[0]*n
    def dfs(x,y):
        nonlocal ans
        if x==n:
            ans+=1
            return
        nx,ny=(x,y+1) if y+1<n else (x+1,0)
        if y==n-1:
            v=l-r[x]
            if v<0 or c[y]+v>l:return
            r[x]+=v;c[y]+=v
            dfs(nx,ny)
            r[x]-=v;c[y]-=v
        elif x==n-1:
            v=l-c[y]
            if v<0 or r[x]+v>l:return
            r[x]+=v;c[y]+=v
            dfs(nx,ny)
            r[x]-=v;c[y]-=v
        else:
            m=min(l-r[x],l-c[y])
            for v in range(m+1):
                r[x]+=v;c[y]+=v
                dfs(nx,ny)
                r[x]-=v;c[y]-=v
    dfs(0,0)
    return ans
 
a=[[0]*3 for _ in range(8)]
for i in range(2,10):
    for j in range(2,5):
        a[i-2][j-2]=f(i,j)
print(a)
