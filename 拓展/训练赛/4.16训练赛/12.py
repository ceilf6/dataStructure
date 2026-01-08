
def get_nei(x,y):
    neis=[]
    for dx,dy in[[0,1],[0,-1],[1,0],[-1,0]]:
        nx,ny=x+dx,y+dy
        if 0<=nx<len(ma) and 0<=ny<len(ma[0]):
            neis.append((nx,ny))
    return neis

'''
def dfs(pos):
    x,y=pos
    if ma[x][y]==0:return 0

    if 2<=ma[x][y]<=9:
        return 2

    ma[x][y]=0

    for nei in get_nei(pos):
        if dfs(nei)==2:
            return 2
        
    return 1
'''
from collections import deque
def bfs(pos):
    q=deque([pos])
    flag=0
    while q:
        x,y=q.popleft()
        if vis[x][y]:
            continue
        vis[x][y]=1

        if 2<=ma[x][y]<=9:
            flag=1

        for nei in get_nei(x,y):
            nx,ny=nei
            if not vis[nx][ny] and ma[nx][ny]!=0:
                q.append((nx,ny))
                
    return flag
            
        
    
n,m=map(int,input().split())
ma=[]
for i in range(n):
    ma.append([int(k) for k in input()])

cnti=0
cntt=0
vis=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if ma[i][j] and not vis[i][j]:
            flag=bfs((i,j))
            cnti+=1
            if flag:
                cntt+=1
print(cnti,cntt)
