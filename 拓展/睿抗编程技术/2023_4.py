from collections import defaultdict, deque

# 构建图
d = defaultdict(list)
n = int(input())
for _ in range(n):
    a, n1, b, n2 = input().split()
    n1, n2 = int(n1), int(n2)
    d[a].append((b, n1 == n2))  # True表示方向相同，False表示方向相反

def bfs(start):
    # 队列存储 (节点, 相对性) 对
    queue = deque([(start, 0)])  # 0表示正向
    visited = {(start, 0): []}  # 记录路径
    
    while queue:
        node, rel = queue.popleft()
        path = visited[(node, rel)]
        
        # 如果找到了一个节点的两种相对性，说明找到了矛盾
        if (node, not rel) in visited:
            return path
        
        # 遍历邻居
        for next_node, same_dir in d[node]:
            # 计算新的相对性
            new_rel = rel if same_dir else not rel
            if (next_node, new_rel) not in visited:
                new_path = path + [(node, rel, next_node, new_rel)]
                visited[(next_node, new_rel)] = new_path
                queue.append((next_node, new_rel))
    
    return None

# 对每个节点尝试查找矛盾路径
for start_node in d:
    path = bfs(start_node)
    if path:
        # 构建输出字符串
        result = []
        # 添加起始节点
        first_node = path[0][0]
        result.append(f"{first_node} 0")
        
        # 添加路径中的节点
        for _, _, next_node, rel in path:
            result.append(f"{next_node} {1 if rel else 0}")
        
        # 输出结果
        print(" ".join(result) + f" = {first_node} 0 {first_node} 1")
        break
