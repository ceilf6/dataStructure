from collections import deque

def has_perfect_matching(n, blacklists):
    """
    判断是否存在一个满足黑名单约束的完美匹配。
    n: 女士/男士数量
    blacklists: 长度为 n 的列表，其中 blacklists[u] 是女士 u 的黑名单列表（男士编号 0..n-1）
    """
    # 预处理：对每个女士的黑名单排序，便于按区间跳过
    for u in range(n):
        blacklists[u].sort()

    # pairU[u]: 与女士 u 匹配的男士编号（-1 表示未匹配）
    # pairV[v]: 与男士 v 匹配的女士编号（-1 表示未匹配）
    pairU = [-1] * n
    pairV = [-1] * n
    # dist[u]: BFS 层次距离
    dist = [0] * n
    INF = float('inf')

    def bfs():
        """
        BFS 建立距离层次图，找到从所有自由女士开始的最短增广路径长度 dist_nil。
        如果存在可增广路径则返回 True，并设置 dist_nil；否则返回 False。
        """
        queue = deque()
        dist_nil = INF

        # 初始化：所有未匹配的女士距离为 0，其余为 INF
        for u in range(n):
            if pairU[u] == -1:   # u 是自由女士
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF

        # BFS 遍历
        while queue:
            u = queue.popleft()
            # 只要当前距离小于已找到的增广路径最短距离，就继续扩展
            if dist[u] < dist_nil:
                prev = -1
                # 遍历女士 u 的允许匹配的男士：区间方式跳过黑名单
                for b in blacklists[u]:
                    # 遍历区间 [prev+1, b-1] 内的男士
                    for v in range(prev+1, b):
                        if pairV[v] == -1:
                            # 找到自由男士，更新 dist_nil（最短增广路径长度）
                            dist_nil = dist[u] + 1
                        else:
                            # 如果 v 匹配有女士，则扩展到该女士
                            if dist[pairV[v]] == INF:
                                dist[pairV[v]] = dist[u] + 1
                                queue.append(pairV[v])
                    prev = b
                # 最后一个区间 [prev+1, n-1]
                for v in range(prev+1, n):
                    if pairV[v] == -1:
                        dist_nil = dist[u] + 1
                    else:
                        if dist[pairV[v]] == INF:
                            dist[pairV[v]] = dist[u] + 1
                            queue.append(pairV[v])
        # 如果找到增广路径，则 dist_nil 被更新
        return dist_nil != INF

    def dfs(u):
        """
        DFS 寻找并增广路径，从女士 u 开始（假设 u 在合适的 BFS 层次上）。
        返回是否找到一条增广路径。
        """
        prev = -1
        # 遍历允许匹配的男士（跳过黑名单）
        for b in blacklists[u]:
            for v in range(prev+1, b):
                # 如果男士 v 空闲 或 v 的配对女士可继续扩展
                if pairV[v] == -1 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                    pairU[u] = v
                    pairV[v] = u
                    return True
            prev = b
        # 最后一个区间 [prev+1, n-1]
        for v in range(prev+1, n):
            if pairV[v] == -1 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                pairU[u] = v
                pairV[v] = u
                return True
        # 如果 u 无增广路径可走，将其距离标为 INF（剪枝）
        dist[u] = INF
        return False

    # HK 主循环：重复 BFS + 多次 DFS，直到无法再增广
    matching = 0
    while bfs():
        for u in range(n):
            if pairU[u] == -1:       # 对每个自由女士尝试增广
                if dfs(u):
                    matching += 1

    # 如果匹配数等于 n，则存在完美匹配
    return (matching == n)

n=int(input())
b=[]
for i in range(n):
    b.append(list(map(int,input().split()))[1:])

flag=has_perfect_matching(n,b)
print(flag)
