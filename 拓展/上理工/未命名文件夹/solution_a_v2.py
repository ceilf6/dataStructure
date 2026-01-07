from collections import defaultdict

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
    
    # 对每个目标节点，使用DFS找到所需的最小初始体力
    results = []
    
    for target in range(2, n + 1):
        min_energy = find_min_energy_dfs(graph, energy_gain, n, target)
        results.append(min_energy)
    
    return results

def find_min_energy_dfs(graph, energy_gain, n, target):
    """
    使用DFS枚举所有可能的路径，找到所需的最小初始体力
    """
    min_initial_energy = float('inf')
    
    def dfs(node, target_node, visited, current_energy, min_initial_needed):
        nonlocal min_initial_energy
        
        if node == target_node:
            min_initial_energy = min(min_initial_energy, min_initial_needed)
            return
        
        # 剪枝：如果当前需要的最小初始体力已经超过了找到的最优解，停止搜索
        if min_initial_needed >= min_initial_energy:
            return
        
        # 到达当前节点后，获得体力（除了起始节点1）
        if node != 1:
            current_energy += energy_gain[node]
        
        # 尝试移动到每个相邻节点
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                
                if current_energy >= edge_weight:
                    # 当前体力足够，直接移动
                    dfs(neighbor, target_node, visited, current_energy - edge_weight, min_initial_needed)
                else:
                    # 当前体力不够，需要增加初始体力
                    additional_energy = edge_weight - current_energy
                    new_min_initial = min_initial_needed + additional_energy
                    dfs(neighbor, target_node, visited, 0, new_min_initial)
                
                visited.remove(neighbor)
    
    visited = {1}
    dfs(1, target, visited, 0, 0)
    
    return min_initial_energy if min_initial_energy != float('inf') else 0

def main():
    T = int(input())
    for _ in range(T):
        results = solve()
        print(*results)

if __name__ == "__main__":
    main()
