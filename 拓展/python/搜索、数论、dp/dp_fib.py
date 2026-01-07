n=int(input())

dp=[1]*n

for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[-1])
