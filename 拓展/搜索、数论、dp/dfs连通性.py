dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=5,5

def dfs(x,y):
    if g[x][y]=='0':return 0#如果没有return 0的话，就会返回函数内形参cnt的初始值也就是1
    g[x][y]='0'     #防止反复搜索
    cnt=1       #统计连通块的大小
    for i in range(4):  #四个方向
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if g[nx][ny]=='1': #鉴于p1162题，最好还是再判断一下
                cnt+=dfs(nx,ny) #每个方向的符合条件的方块数相加
    return cnt

g=list()
for i in range(5):g.append(list(input().split()))#注意用了split函数所以输入时要添加空格

ans=0

for i in range(n):
    for j in range(m): #遍历
        if g[i][j]=='1':
            ans=max(ans,dfs(i,j))#输出最大的连通块大小，具体按照题目要求来改，主要是dfs函数

print(ans)
