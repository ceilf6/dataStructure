
from collections import deque

s1=input()
s2=input()

di=[(1,0),(-1,0),(0,1),(0,-1)]

k1=s1.find('.')
k2=s2.find('.')

(x1,y1)=(k1%3,k1//3)
(x2,y2)=(k2%3,k2//3)

start=(x1,y1)
end=(x2,y2)
rows,cols=3,3
def get_neighbors(current):
    x, y = current
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:  # 边界检查
            ##if grid[nx][ny] == 0:  # 假设0表示可通行
            neighbors.append((nx, ny))
    return neighbors

def bidirectional_bfs(start, end):



    queue_start = deque([start])
    queue_end = deque([end])
    visited_start = {start: 0}
    visited_end = {end: 0}

    while queue_start and queue_end:
        # 选择较小的队列扩展
        if len(queue_start) <= len(queue_end):
            current = queue_start.popleft()
            for neighbor in get_neighbors(current):
                if neighbor not in visited_start:
                    visited_start[neighbor] = visited_start[current] + 1
                    queue_start.append(neighbor)
                    if neighbor in visited_end:
                        return visited_start[neighbor] + visited_end[neighbor]
        else:
            current = queue_end.popleft()
            for neighbor in get_neighbors(current):
                if neighbor not in visited_end:
                    visited_end[neighbor] = visited_end[current] + 1
                    queue_end.append(neighbor)
                    if neighbor in visited_start:
                        return visited_start[neighbor] + visited_end[neighbor]
    return -1  # 无路径

'''
def bfs():
    n,m=3,3
    start=(x1,y1)
    end=(x2,y2)
    queue=collections.deque([(start,0)])
    vis=set()
    vis.add(start)
    while queue:
        (x,y),steps=queue.popleft()
        if (x,y)==end:
            return steps

        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in vis:
                queue.append(((nx,ny),steps+1))
                vis.add((nx,ny))

    return -1
'''
print(bidirectional_bfs(start,end))


