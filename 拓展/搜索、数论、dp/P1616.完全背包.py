J,N=map(int,input().split())

j=[0]*(N+1)#多设1！
w=[0]*(N+1)

for i in range(1,N+1):#注意各个变量名称和用途的区分
    j[i],w[i]=map(int,input().split())

dp=[[0]*(J+1) for i in range(N+1)]

for i in range(1,N+1):
    for t in range(1,J+1):
        dp[i][t]=dp[i-1][t]
        if t>=j[i]:
            dp[i][t]=max(dp[i][t],dp[i][t-j[i]]+w[i])
            #每次将当前状态和下一个未比较作max

print(dp[N][J])
