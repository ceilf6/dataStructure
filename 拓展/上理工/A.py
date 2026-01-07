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
    
    # 对每个目标节点，计算所需的最小初始体力
    results = []
    
    for target in range(2, n + 1):
        min_energy = find_min_energy(graph, energy_gain, n, target)
        results.append(min_energy)
    
    return results

def find_min_energy(graph, energy_gain, n, target):
    """
    使用记忆化DFS找到所需的最小初始体力
    """
    # memo[node][energy] = 从该节点和能量状态到目标所需的最小额外初始体力
    memo = {}
    
    def dfs(node, current_energy, visited):
        if node == target:
            return 0
        
        # 记忆化
        state = (node, current_energy, tuple(sorted(visited)))
        if state in memo:
            return memo[state]
        
        min_additional = float('inf')
        
        # 如果不是起始节点，获得体力
        if node != 1:
            current_energy += energy_gain[node]
        
        # 尝试移动到每个未访问的相邻节点
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                new_visited = visited | {neighbor}
                
                if current_energy >= edge_weight:
                    # 当前体力足够
                    additional = dfs(neighbor, current_energy - edge_weight, new_visited)
                else:
                    # 当前体力不够，需要额外体力
                    needed_extra = edge_weight - current_energy
                    additional = needed_extra + dfs(neighbor, 0, new_visited)
                
                min_additional = min(min_additional, additional)
        
        memo[state] = min_additional
        return min_additional
    
    result = dfs(1, 0, {1})
    return result if result != float('inf') else 0

def main():
    T = int(input())
    for _ in range(T):
        results = solve()
        print(*results)

if __name__ == "__main__":
    main()
