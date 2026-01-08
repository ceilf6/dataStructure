import sys
sys.setrecursionlimit(10000)

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input())  # 输入矩阵大小
a = [list(input().split()) for _ in range(n)]  # 输入矩阵，按行拆分成字符列表

# 深度优先搜索 (DFS)，将 '0' 区域标记为 '2'
def dfs(x, y):
    if a[x][y] == '1': return  # 遇到 1，不处理
    a[x][y] = '2'  # 标记为已访问
    for i in range(4):  # 四个方向：右、上、左、下
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == '0':  # 如果是 '0'，继续递归
                dfs(nx, ny)

# 深度优先搜索 (DFS)，将所有与边界相连的 '2' 变回 '0'
def dfs2(x, y):
    if a[x][y] == '1': return  # 遇到 1，不处理
    a[x][y] = '0'  # 标记为可通过的区域
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == '2':  # 如果是 '2'，继续递归
                dfs2(nx, ny)

# 对于所有的 '0'，进行深度优先搜索，填充闭合圈
for i in range(n):
    for j in range(n):
        if a[i][j] == '0':
            dfs(i, j)

# 对于边界上的 '2'，进行 dfs2，确保它们不被填充
for i in range(n):
    if a[0][i] == '2':  # 上边界
        dfs2(0, i)
    if a[n-1][i] == '2':  # 下边界
        dfs2(n-1, i)
for i in range(n):
    if a[i][0] == '2':  # 左边界
        dfs2(i, 0)
    if a[i][n-1] == '2':  # 右边界
        dfs2(i, n-1)

# 输出处理后的矩阵
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()  # 每行输出后换行
