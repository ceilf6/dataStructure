from collections import deque

def shortest_path(start, target, get_neighbors):
    """
    单向BFS寻找最短路径（使用字典记录步长）
    :param start: 起点坐标 (x, y)
    :param target: 终点坐标 (x, y)
    :param get_neighbors: 函数，输入坐标返回可达的相邻坐标列表
    :return: 最短路径步数（无法到达返回-1）
    """
    if start == target:
        return 0
    
    # 初始化队列和访问字典（记录坐标到步数的映射）
    queue = deque([start])
    visited = {start: 0}  # 字典存储：坐标 -> 步数

    while queue:
        current = queue.popleft()
        current_steps = visited[current]

        # 到达终点直接返回步数
        if current == target:
            return current_steps

        # 遍历所有可达邻居
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = current_steps + 1  # 更新步数
                queue.append(neighbor)
    
    return -1  # 队列耗尽未找到路径


# 示例用法（与双向BFS相同的测试数据）
if __name__ == "__main__":
    # 定义网格（0=可通过，1=障碍）
    grid = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    target = (3, 3)
    
    # 定义邻居生成函数（闭合grid变量）
    def get_neighbors(pos):
        x, y = pos
        neighbors = []
        # 四个移动方向（上、下、左、右）
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            # 检查坐标是否在网格范围内且非障碍
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                neighbors.append( (nx, ny) )
        return neighbors
    
    # 执行单向BFS
    steps = shortest_path(start, target, get_neighbors)
    print(f"最短路径步数: {steps}")  # 输出6
