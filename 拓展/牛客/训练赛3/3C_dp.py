n,k=map(int,input().split())

a=list(map(int,input().split()))

dp=[[[0]*k for i in range(n)] for j in range(n)]

#print(dp)
#临界状态
#dp=[

for i in range(1,n):
    for j in range(n-2,i-1,-1):
        for m in range(1,k):
            #print(i,j,m)
            dp[i][j][m]=max(dp[i][j+1][m-1]-a[j],dp[i-1][j][m-1]-a[i-1])

print(dp[0][n-1][k-1])
