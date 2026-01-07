from collections import deque

# 输入
n, m, x, y = map(int, input().split())

# 起始点索引从 0 开始
start_x, start_y = x - 1, y - 1  

# 骑士的 8 个移动方向
di = [(2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]

# 结果矩阵，-1 表示不可达
result = [[-1] * m for _ in range(n)]

# BFS 队列
queue = deque([(start_x, start_y, 0)])  # (当前 x, 当前 y, 当前步数)

# BFS 开始
while queue:
    x, y, steps = queue.popleft()

    # 如果已经访问过，跳过
    if result[x][y] != -1:
        continue

    # 更新步数到结果矩阵
    result[x][y] = steps

    # 遍历所有可能的方向
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and result[nx][ny] == -1:
            queue.append((nx, ny, steps + 1))

# 输出结果矩阵
for row in result:
    print(" ".join(f"{v:3}" for v in row))  # 格式化对齐输出
