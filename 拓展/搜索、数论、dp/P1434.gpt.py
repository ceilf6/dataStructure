def longest_slide(R, C, heights):
    # 方向数组：上下左右
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 初始化 dp 数组，-1 表示未计算
    dp = [[-1] * C for _ in range(R)]

    # 定义 DFS 函数
    def dfs(x, y):
        if dp[x][y] != -1:  #记忆化  如果已经计算过，直接返回缓存值
            return dp[x][y]
        
        dp[x][y] = 1  # 初始化为当前点本身的长度
        for k in range(4):  # 遍历四个方向
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and heights[nx][ny] < heights[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        
        return dp[x][y]

    # 遍历所有点，计算最长路径
    max_length = 0
    for i in range(R):
        for j in range(C):
            max_length = max(max_length, dfs(i, j))

    return max_length


# 输入
R, C = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(R)]

# 计算并输出结果
print(longest_slide(R, C, heights))
