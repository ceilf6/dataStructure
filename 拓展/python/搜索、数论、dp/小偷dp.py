def maxLoot(hval, n):
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = hval[0]
    dp[1] = max(hval[0], hval[1])
    for i in range(2, n):
        dp[i] = max(hval[i] + dp[i-2], dp[i-1])
    return dp[-1]
