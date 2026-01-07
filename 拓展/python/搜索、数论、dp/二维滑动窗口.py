from collections import deque

n, m, a, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# 计算每行长度为b的窗口的最大值和最小值
maxx = []
minn = []
k = b
for i in range(n):
    q_max = deque()
    row_max = []
    for current in range(m):
        while q_max and A[i][current] > A[i][q_max[-1]]:
            q_max.pop()
        q_max.append(current)
        while q_max[0] <= current - k:
            q_max.popleft()
        if current >= k - 1:
            row_max.append(A[i][q_max[0]])
    maxx.append(row_max)

    q_min = deque()
    row_min = []
    for current in range(m):
        while q_min and A[i][current] < A[i][q_min[-1]]:
            q_min.pop()
        q_min.append(current)
        while q_min[0] <= current - k:
            q_min.popleft()
        if current >= k - 1:
            row_min.append(A[i][q_min[0]])
    minn.append(row_min)

# 初始化maxx2和minn2，每个子列表有足够的列数
rows = n - a + 1
cols = len(maxx[0])  # 即m - b + 1
maxx2 = [[0] * cols for _ in range(rows)]
minn2 = [[0] * cols for _ in range(rows)]

k = a
# 处理maxx的列，得到maxx2
for j in range(cols):
    q = deque()
    for current in range(n):
        while q and maxx[current][j] > maxx[q[-1]][j]:
            q.pop()
        q.append(current)
        while q[0] <= current - k:
            q.popleft()
        if current >= k - 1:
            idx = current - k + 1
            maxx2[idx][j] = maxx[q[0]][j]

# 处理minn的列，得到minn2
for j in range(cols):
    q = deque()
    for current in range(n):
        while q and minn[current][j] < minn[q[-1]][j]:
            q.pop()
        q.append(current)
        while q[0] <= current - k:
            q.popleft()
        if current >= k - 1:
            idx = current - k + 1
            minn2[idx][j] = minn[q[0]][j]

# 计算总和
summ = 0
for i in range(rows):
    for j in range(cols):
        summ += maxx2[i][j] * minn2[i][j]

print(summ)
