N = int(input())
m = list(map(int, input().split()))

# 复制数组，处理环形
m = m * 2  # 复制一遍数组
dp_min = [[float('inf')] * (2 * N + 1) for _ in range(2 * N + 1)]
dp_max = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]

# 计算前缀和
s = [0] * (2 * N + 2)
for i in range(1, 2 * N + 1):
    s[i] = s[i - 1] + m[i - 1]

# 初始化 dp
for i in range(1, 2 * N + 1):
    dp_min[i][i] = dp_max[i][i] = 0  # 只有一个石子堆，不需要合并

# 区间 DP 递推
for j in range(2, 2 * N + 1):  # 枚举区间右端点
    for i in range(j - 1, 0, -1):  # 枚举左端点
        if j - i + 1 > N:  # 只处理长度 ≤ N 的区间
            continue
        for k in range(i, j):  # 枚举分割点
            cost = s[j] - s[i - 1]  # 当前区间合并的代价
            dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j] + cost)
            dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j] + cost)

# 计算最小得分和最大得分
min_res = float('inf')
max_res = 0

for i in range(1, N + 1):  # 枚举环形的起点
    min_res = min(min_res, dp_min[i][i + N - 1])
    max_res = max(max_res, dp_max[i][i + N - 1])

# 输出最小得分和最大得分
print(min_res)
print(max_res)
