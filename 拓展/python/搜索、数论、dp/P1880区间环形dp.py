N = int(input())
m = list(map(int, input().split()))

# 复制数组，处理环形
m = m * 2  # 复制一遍数组
dp = [[float('inf')] * (2 * N + 1) for _ in range(2 * N + 1)]

# 计算前缀和
s = [0] * (2 * N + 2)
for i in range(1, 2 * N + 1):
    s[i] = s[i - 1] + m[i - 1]

# 初始化 dp
for i in range(1, 2 * N + 1):
    dp[i][i] = 0  # 单个石子堆不需要合并

# 区间 DP 递推
for j in range(2, 2 * N + 1):  # 枚举区间右端点
    for i in range(j - 1, 0, -1):  # 枚举左端点
        for k in range(i, j):  # 枚举分割点
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s[j] - s[i - 1])

# 计算最小得分
res = float('inf')
for i in range(1, N + 1):  # 枚举环形的起点
    res = min(res, dp[i][i + N - 1])

print(res)
