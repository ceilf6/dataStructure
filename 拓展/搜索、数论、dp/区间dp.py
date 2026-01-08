def stone_merge(stones):
    n = len(stones)
    # 初始化前缀和数组，用于快速计算区间和
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]

    # 初始化 DP 数组
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0  # 单个石子无需合并

    # 按区间长度递推
    for length in range(2, n + 1):  # 区间长度从 2 开始
        for i in range(n - length + 1):
            j = i + length - 1
            # 枚举分割点
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i]
                )

    return dp[0][n - 1]

print(float('inf'))
# 示例使用
stones = [4, 3, 3, 4]
min_cost = stone_merge(stones)
print(f"最小合并代价为: {min_cost}")
