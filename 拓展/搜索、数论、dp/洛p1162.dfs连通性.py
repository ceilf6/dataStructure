import sys
sys.setrecursionlimit(10000)

dx=[0,-1,0,1]
dy=[1,0,-1,0]

n=int(input())

a=list()

for i in range(n):
    a.append(list(input().split()))

def dfs(x,y):
    if a[x][y]=='1':return
    a[x][y]='2'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if a[nx][ny] == '0': #别忘记判断是不是0(未处理的），防止重复处理
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if a[i][j]=='0':
            dfs(i,j)

def dfs2(x,y):
    if a[x][y]=='1':return
    a[x][y]='0'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if a[nx][ny] == '2': #别忘记判断是不是2(未处理的），防止重复处理
                dfs2(nx,ny)
                
# 对于边界上的 '2'，进行 dfs2，确保它们不被填充
for i in range(n):
    if a[0][i] == '2':  # 上边界
        dfs2(0, i)
    if a[n-1][i] == '2':  # 下边界
        dfs2(n-1, i)
for i in range(n):
    if a[i][0] == '2':  # 左边界
        dfs2(i, 0)
    if a[i][n-1] == '2':  # 右边界
        dfs2(i, n-1)

ans='\n'.join(' '.join(map(str,row)) for row in a)

print(ans)
