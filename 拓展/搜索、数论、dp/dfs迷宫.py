def dfs_maze(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    
    # 边界条件
    if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == 1 or (x, y) in visited:
        return False
    
    # 如果到达终点
    if maze[x][y] == 9:
        print("Reached destination:", (x, y))
        return True
    
    # 标记为已访问
    visited.add((x, y))
    
    # 尝试上下左右四个方向
    if (dfs_maze(maze, x+1, y, visited) or  # 下
        dfs_maze(maze, x-1, y, visited) or  # 上
        dfs_maze(maze, x, y+1, visited) or  # 右
        dfs_maze(maze, x, y-1, visited)):   # 左
        print("Path:", (x, y))
        return True
    
    return False

# 示例迷宫
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 9, 1]  # 9 是终点
]
visited = set()
dfs_maze(maze, 0, 0, visited)
