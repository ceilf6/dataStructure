from collections import defaultdict

def analyze_graph():
    # 第三个测试用例的图
    graph = defaultdict(list)
    edges = [
        (1, 2, 4),
        (1, 4, 7),
        (3, 2, 5),
        (7, 6, 6),
        (6, 4, 9),
        (4, 5, 1)
    ]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    print("邻接表:")
    for node in sorted(graph.keys()):
        neighbors = [(v, w) for v, w in graph[node]]
        print(f"节点{node}: {neighbors}")
    
    print("\n从节点1开始的BFS遍历检查连通性:")
    from collections import deque
    visited = set()
    queue = deque([1])
    visited.add(1)
    
    while queue:
        node = queue.popleft()
        print(f"访问节点{node}")
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    print(f"\n从节点1可以到达的所有节点: {sorted(visited)}")
    
    # 检查到节点6的所有可能路径
    print("\n寻找从1到6的所有路径:")
    find_all_paths(graph, 1, 6, [1], set([1]))
    
    print("\n寻找从1到7的所有路径:")
    find_all_paths(graph, 1, 7, [1], set([1]))

def find_all_paths(graph, start, end, path, visited):
    if start == end:
        print(f"路径: {' -> '.join(map(str, path))}")
        return
    
    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            new_path = path + [neighbor]
            new_visited = visited | {neighbor}
            find_all_paths(graph, neighbor, end, new_path, new_visited)

if __name__ == "__main__":
    analyze_graph()
