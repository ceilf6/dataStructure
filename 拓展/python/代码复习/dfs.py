
b=[0]*n
vis=[0]*n
res=[]
def dfs(step):#paixu
    if step==n:#m
        b2=b.copy()
        res.append(b2)#[:m]
        return

    for i in range(n):
        if vis[i]==0:
            vis[i]=1
            b[step]=a[i]
            dfs(step+1)
            vis[i]=0


vis=[0]*n
res=[]
def dfs(step):#zuhe
    if step==n:
        ans=[]
        for i in range(n):
            if vis[i]:
                ans.append(a[i])
        res.append(ans)
        return

    vis[step]=1
    dfs(step+1)
    vis[step]=0
    dfs(step+1)


def get_nei(pos):
    x,y=pos
    neis=[]
    for dx,dy in[[0,1],[0,-1],[1,0],[-1,0]]:
        nx,ny=x+dx,y+dy
        if 0<=nx<=len(ma[0]) and 0<=ny<=len(ma):
            neis.append((nx,ny))
    return neis

def dfs(pos):#liantong
    x,y=pos
    if ma[x][y]=='0':
        return

    ma[x][y]=0
    cnt=1
    for nei in get_nei(pos):
        cnt+=dfs(nei)

    return cnt








    
