N=int(input())
m=list(map(int,input().split()))

dp=[[float('inf')]*(N+1) for i in range(N+1)]

s=[0]*(N+2)
s[1]=m[0]
for i in range(2,N+1):
    s[i]=s[i-1]+m[i-1]

for i in range(1,N+1):
    dp[i][i]=0

for j in range(2,N+1):
    for i in range(j-1,0,-1):
        #dp[i][j]=float('inf')
        for  k in range(i,j):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+s[j]-s[i-1])

print(dp[1][N])
