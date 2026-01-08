#lanqiao1174
N,V=map(int,input().split())

w=[0]*(N+1)
v=[0]*(N+1)

for i in range(1,N+1):
    v[i],w[i]=map(int,input().split())#注意先后，是先输入的体积，再输入的价值

dp=[[0]*(V+1) for _ in range(N+1)]

for i in range(1,N+1):#遍历I个：装与不装
    for j in range(V+1):#当前容量情况
        if v[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-v[i]]+w[i])
            #两种情况：选或不选，取max             #注意：i-1从上一个物品推得；j-v【i】减去容量

print(dp[N][V])
            
