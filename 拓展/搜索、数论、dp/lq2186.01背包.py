dp=[[[0]*2023 for _ in range(11)] for _ in range(2023)]

for i in range(2023):dp[i][0][0]=1

for i in range(1,2023):
    for j in range(1,11):
        for k in range(2023):
            if i>k:
                dp[i][j][k]=dp[i-1][j][k]
            else:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k-i]



print(dp[2022][10][2022])
