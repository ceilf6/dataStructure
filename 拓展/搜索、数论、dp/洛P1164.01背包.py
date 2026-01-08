n,m=map(int,input().split())

a=list(map(int,input().split()))

dp=[[0]*(m+1) for  i in range(n+1)]

for i in range(n+1):dp[i][0]=1

for i  in range(1,n+1):
    for j in range(1,m+1):
        if j>=a[i-1]:dp[i][j]=dp[i-1][j-a[i-1]]+dp[i-1][j]
 #注意状态转移的分段             #选择      或者        不选
        #if j==a[i-1]:dp[i][j]=dp[i-1][j-a[i-1]]+1 因为本身dp【】【0】就是1，所以可以合并到上面
        if j<a[i-1]:dp[i][j]=dp[i-1][j]
        
print(dp[n][m])
