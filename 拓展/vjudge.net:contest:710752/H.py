def dfs(x,y):
    if ma[x][y]=='R':
        return 0

    ma[x][y]='R'
    cnt=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 1<=ny<m:
            cnt+=dfs(nx,ny)
    return cnt

dx,dy=[-1,0,1,0],[0,1,0,-1]

n,m=map(int,input().split())

ma=[]
for i in range(n):
    ma.append(list(input().split()))

maxx=0
for i in range(n):
    for j in range(m):
        if ma[i][j]=='F':
            maxx=max(maxx,dfs(i,j))

print(maxx*)
