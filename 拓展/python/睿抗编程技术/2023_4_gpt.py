from collections import deque, defaultdict

n = int(input())
edges = []  # 保存原始推论
graph = defaultdict(list)

# 构建图，每个“论点 方向”是一个节点
for _ in range(n):
    a, d1, b, d2 = input().split()
    d1, d2 = int(d1), int(d2)
    edges.append(((a, d1), (b, d2)))
    graph[(a, d1)].append(((b, d2)))
    
# BFS 搜索从每个点出发能否到达其矛盾版本
def bfs(start):
    queue = deque()
    visited = {}
    parent = {}
    queue.append(start)
    visited[start] = None
    
    while queue:
        u = queue.popleft()
        if u[0] == start[0] and u[1] != start[1]:
            # 找到矛盾路径
            path = []
            cur = u
            while cur is not None:
                path.append(cur)
                cur = visited[cur]
            path.reverse()
            return path
        for v in graph[u]:
            if v not in visited:
                visited[v] = u
                queue.append(v)
    return None

# 用于打印路径对应的推论
def build_result(path):
    output = []
    for i in range(len(path) - 1):
        a = path[i]
        b = path[i + 1]
        output.append(f"{a[0]} {a[1]}")
        output.append(f"{b[0]} {b[1]}")
    output.append("=")
    output.append(f"{path[0][0]} {path[0][1]} {path[-1][0]} {path[-1][1]}")
    res=(' '.join(output))
    return res

# 从所有节点尝试寻找矛盾路径
found = False
for node in graph:
    path = bfs(node)
    if path:
        print(build_result(path))
        found = True
        break