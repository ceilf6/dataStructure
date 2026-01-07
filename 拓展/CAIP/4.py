import heapq
from collections import defaultdict

def solve_travel_route():
    # 读取输入
    n, m, s, t = map(int, input().split())
    popularity = list(map(int, input().split()))
    
    # 构建邻接表
    graph = defaultdict(list)
    for _ in range(m):
        u, v, cost = map(int, input().split())
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    # Dijkstra算法变种：同时记录最小成本和最大热度
    # dist[i] = (最小成本, 途经城镇的最大热度)
    dist = {i: (float('inf'), float('inf')) for i in range(1, n+1)}
    dist[s] = (0, 0)  # 起点成本为0，热度为0
    
    # 优先队列：(成本, 最大热度, 当前节点)
    pq = [(0, 0, s)]
    visited = set()
    
    while pq:
        cost, max_popularity, current = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        visited.add(current)
        
        # 如果到达目标节点，返回结果
        if current == t:
            return cost, max_popularity
        
        # 遍历邻居节点
        for neighbor, edge_cost in graph[current]:
            if neighbor in visited:
                continue
                
            new_cost = cost + edge_cost
            # 更新途经城镇的最大热度（不包括起点和终点）
            new_max_popularity = max_popularity
            if neighbor != t:  # 不包括终点
                new_max_popularity = max(max_popularity, popularity[neighbor-1])
            
            # 如果找到更短的路径，或者路径长度相同但热度更小
            if (new_cost < dist[neighbor][0] or 
                (new_cost == dist[neighbor][0] and new_max_popularity < dist[neighbor][1])):
                
                dist[neighbor] = (new_cost, new_max_popularity)
                heapq.heappush(pq, (new_cost, new_max_popularity, neighbor))
    
    # 如果无法到达目标节点
    return "Impossible"

# 处理输入并输出结果
result = solve_travel_route()
if result == "Impossible":
    print("Impossible")
else:
    cost, max_popularity = result
    print(f"{cost} {max_popularity}")
