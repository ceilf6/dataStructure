import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent, depth, edges, visited):
    # 返回最远的节点和深度
    farthest_node = node
    max_depth = depth
    visited[node] = True
    
    for u, v in edges:
        # 只考虑没有访问过的节点
        if u == node and not visited[v]:
            candidate_node, candidate_depth = dfs(v, u, depth + 1, edges, visited)
            if candidate_depth > max_depth:
                max_depth = candidate_depth
                farthest_node = candidate_node
        elif v == node and not visited[u]:
            candidate_node, candidate_depth = dfs(u, v, depth + 1, edges, visited)
            if candidate_depth > max_depth:
                max_depth = candidate_depth
                farthest_node = candidate_node
    
    return farthest_node, max_depth

def find_tree_diameter(n, edges):
    # 初始化一个访问标记数组
    visited = [False] * (n + 1)
    
    # 1. 从任意一个节点（比如节点1）开始 DFS，找到一个最远的节点
    farthest_from_root, _ = dfs(1, -1, 0, edges, visited)
    
    # 2. 从最远的节点出发，再进行一次 DFS，得到树的直径
    visited = [False] * (n + 1)  # 重新初始化访问标记
    _, diameter = dfs(farthest_from_root, -1, 0, edges, visited)
    
    return diameter

# 输入读取
n = int(input().strip())

edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append([u, v])

# 计算并输出最大深度
print(find_tree_diameter(n, edges))
