r,c=map(int,input().split())

xx=[0,1,0,-1]#四个方向
yy=[1,0,-1,0]

mapp=[]

for i in range(r):
    mapp.append(list(map(int,input().split())))
 
dp=[[-1]*c for _ in range(r)]#初始化为-1，方便判断进行记忆化

def dfs(x,y):
    global mapp
    if dp[x][y]!=-1:#如果已经计算过，直接返回
        return dp[x][y]

    dp[x][y]=1 #初始化为当前长度，方便下面判断
    for k in range(4):
        nx,ny=x+xx[k],y+yy[k]
        if 0<=nx<r and 0<=ny<c and mapp[nx][ny]<mapp[x][y]:
                                #是要判断能条件，即能否下滑：是mapp，而不是dp
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
                            #若低于：判断当前这位置最大值和当前前一段的路径加一哪个更大
    return dp[x][y]

maxl=0
for i in range(r):
    for j in range(c):
        maxl=max(maxl,dfs(i,j))

print(maxl)

'''
#dp状态：到i，j位置的最长长度

#dp转移：判断 上下左右 是否是小的：若小dp[i][j]=max(dp[i-1][j]+mapp[i-1][j]-mapp[i][j],


#需要保证保证状态转移时前面的状态都已经计算过了！ ：将点按照高度升序排序，再按照排序结果进行计算？
                                            #栈或队列？

for i in range(0,r):
    for j in range(0,c):
        for k in range(4):
            xx=i+x[k]
            yy=j+y[k]
            if 0<=xx<r and 0<=yy<c:#边界判断    #四个方向的轮流判断
                dp[i][j]=max(dp[i][j],dp[xx][yy]+mapp[xx][yy]-mapp[i][j])
                                    #直接不判断是否高低了，因为有max,如果高的话是负数了肯定不符合

                                    #错了！这道题的路径长度的意思是经过多少点!

'''
