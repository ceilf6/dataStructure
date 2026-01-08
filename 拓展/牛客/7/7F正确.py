n = int(input())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# 调整索引为1-based到n-based
# 假设a现在为0-based的列表，行和列都是0到n-1。但题目中的棋盘中间格子是1-based到n-based。
# 所以需要重新构造棋盘，其中a[i][j]对应棋盘中的行i+1，列j+1？
# 或者可能需要重新组织数组，使得a是1-based的。
# 为了方便，这里将输入的n行n列转换为1-based索引，即a[1..n][1..n]

# 创建一个 (n+2) x (n+2) 的棋盘，周围填充0
grid = [[0]*(n+2) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, n+1):
        grid[i][j] = a[i-1][j-1]

valid = True
for i in range(1, n+1):
    for j in range(1, n+1):
        v = grid[i][j]
        # 计算四个邻接的值
        up = grid[i-1][j] if i-1 >= 0 else 0
        down = grid[i+1][j] if i+1 <= n+1 else 0
        left = grid[i][j-1] if j-1 >= 0 else 0
        right = grid[i][j+1] if j+1 <= n+1 else 0
        # 计算最大值和最小值
        max_neighbor = max(up, down, left, right)
        min_neighbor = min(up, down, left, right)
        if v == 0:
            continue
        if v > max_neighbor or v < min_neighbor:
            continue
        valid = False
        break
    if not valid:
        break

print("YES" if valid else "NO")
