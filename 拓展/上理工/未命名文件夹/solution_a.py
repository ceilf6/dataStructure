from collections import defaultdict
from heapq import heappush, heappop

def solve():
    n = int(input())
    
    # 读取每个节点能获得的体力值
    energy_gain = [0] * (n + 1)  # 1号节点没有超市，体力增益为0
    gains = list(map(int, input().split()))
    for i in range(2, n + 1):
        energy_gain[i] = gains[i - 2]
    
    # 构建邻接表
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # 计算从节点1到所有其他节点的最小初始体力
    results = []
    
    for target in range(2, n + 1):
        min_initial_energy = find_min_energy(graph, energy_gain, n, target)
        results.append(min_initial_energy)
    
    return results

def find_min_energy(graph, energy_gain, n, target):
    """
    使用修改的Dijkstra算法
    状态：(所需最小初始体力, 节点)
    """
    # (所需最小初始体力, 节点)
    pq = [(0, 1)]  # 从节点1开始，所需初始体力为0
    # best[node] = 到达该节点所需的最小初始体力
    best = [float('inf')] * (n + 1)
    best[1] = 0
    
    while pq:
        current_min_initial, node = heappop(pq)
        
        if node == target:
            return current_min_initial
            
        # 如果当前状态不是最优的，跳过
        if current_min_initial > best[node]:
            continue
        
        # 尝试从当前节点移动到邻居节点
        for neighbor, edge_weight in graph[node]:
            # 计算到达neighbor所需的最小初始体力
            # 我们需要考虑从起点到当前节点的路径中获得的所有体力
            
            # 使用DFS来计算实际路径
            new_min_initial = calculate_min_initial_to_neighbor(
                graph, energy_gain, n, 1, neighbor, edge_weight, node, current_min_initial
            )
            
            if new_min_initial < best[neighbor]:
                best[neighbor] = new_min_initial
                heappush(pq, (new_min_initial, neighbor))
    
    return best[target] if best[target] != float('inf') else -1

def calculate_min_initial_to_neighbor(graph, energy_gain, n, start, target, edge_weight, via_node, min_initial_to_via):
    """
    计算通过特定路径到达目标节点所需的最小初始体力
    """
    # 简化方法：使用DFS找到从start到via_node的路径，计算途中获得的体力
    def dfs_path(current, target, path, visited):
        if current == target:
            return path[:]
        
        visited.add(current)
        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                path.append((neighbor, _))
                result = dfs_path(neighbor, target, path, visited)
                if result:
                    return result
                path.pop()
        visited.remove(current)
        return None
    
    # 找到从start到via_node的路径
    path = dfs_path(start, via_node, [], set())
    
    if not path:
        return float('inf')
    
    # 计算路径中获得的总体力
    total_gained = 0
    current_energy = min_initial_to_via
    
    for i, (node, weight) in enumerate(path):
        # 到达节点后获得体力
        if node != start:  # 起始节点不获得体力
            total_gained += energy_gain[node]
            current_energy += energy_gain[node]
    
    # 现在尝试从via_node到neighbor
    if current_energy >= edge_weight:
        return min_initial_to_via
    else:
        return min_initial_to_via + (edge_weight - current_energy)

def main():
    T = int(input())
    for _ in range(T):
        results = solve()
        print(*results)

if __name__ == "__main__":
    main()
