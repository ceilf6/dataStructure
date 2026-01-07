from collections import deque

def bfs_maze(maze, start, end):
    n, m = len(maze), len(maze[0])#地图的行数和列数
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右移动方向
    queue = deque([(start, 0)])  # 队列元素为 (当前坐标, 当前步数)
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps  # 找到终点，返回步数
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy #是小于，不是小于等于
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and (nx, ny) not in visited:
              #未超出边界、且可以通行、且未被访问
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))
    
    return -1  # 无法到达终点

# 测试数据
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 0)

print(bfs_maze(maze, start, end))
