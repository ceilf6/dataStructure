from collections import deque

def has_perfect_matching(n, blacklists):
    # 预处理：将黑名单转换为集合，便于快速查找
    blacklists = [set(blacklist) for blacklist in blacklists]

    pairU = [-1] * n  # 女士的匹配男士
    pairV = [-1] * n  # 男士的匹配女士
    dist = [0] * n    # BFS 层次距离
    INF = float('inf')

    def bfs():
        """
        BFS 建立距离层次图，找到从所有自由女士开始的最短增广路径长度。
        如果存在可增广路径则返回 True，并设置 dist；否则返回 False。
        """
        queue = deque()
        dist_nil = INF

        # 初始化：所有未匹配的女士距离为 0，其余为 INF
        for u in range(n):
            if pairU[u] == -1:  # u 是自由女士
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF

        # BFS 遍历
        while queue:
            u = queue.popleft()
            if dist[u] < dist_nil:
                for v in range(n):
                    if v not in blacklists[u]:  # 检查黑名单
                        if pairV[v] == -1:
                            dist_nil = dist[u] + 1
                        else:
                            if dist[pairV[v]] == INF:
                                dist[pairV[v]] = dist[u] + 1
                                queue.append(pairV[v])
        return dist_nil != INF

    def dfs(u):
        """
        DFS 寻找并增广路径，从女士 u 开始（假设 u 在合适的 BFS 层次上）。
        返回是否找到一条增广路径。
        """
        for v in range(n):
            if v not in blacklists[u]:  # 检查黑名单
                if pairV[v] == -1 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                    pairU[u] = v
                    pairV[v] = u
                    return True
        dist[u] = INF  # 如果 u 无增广路径可走，将其距离标为 INF（剪枝）
        return False

    # HK 主循环：重复 BFS + 多次 DFS，直到无法再增广
    matching = 0
    while bfs():
        for u in range(n):
            if pairU[u] == -1:  # 对每个自由女士尝试增广
                if dfs(u):
                    matching += 1

    # 如果匹配数等于 n，则存在完美匹配
    if matching == n:
        return [v + 1 for v in pairU]  # 返回匹配方案（男士编号从 1 开始）
    else:
        return None

# 输入处理
n = int(input())
blacklists = [list(map(int, input().split()))[1:] for _ in range(n)]

# 计算匹配方案
matching = has_perfect_matching(n, blacklists)

# 输出结果
if matching:
    print(" ".join(map(str, matching)))
else:
    print(-1)
