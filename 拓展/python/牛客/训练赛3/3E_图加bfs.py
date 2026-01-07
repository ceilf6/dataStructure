from collections import deque
import math

def bfs_min_energy(n):
    # 初始化距离数组，设置为无限大
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    
    # 队列，存放 (x, y) 格点
    queue = deque([(0, 0)])
    
    # 方向数组，代表四个相邻的方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        # 获取当前位置的数字
        gcd_val = math.gcd(x + 1, y + 1)  # x + 1, y + 1 是因为数组是从0开始的
        
        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        
        # 如果当前位置的数字不为1，尝试传送
        if gcd_val != 1:
            for i in range(n):
                for j in range(n):
                    if math.gcd(i + 1, j + 1) == gcd_val and dist[i][j] > dist[x][y]:
                        dist[i][j] = dist[x][y]
                        queue.append((i, j))
    
    return dist[n-1][n-1]

# 输入
n = int(input())

# 输出最少能量
print(bfs_min_energy(n))
