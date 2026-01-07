import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
# 原来用 n−1 行描述道路，构建无向图（树）
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 预处理：DFS 求每个节点的深度和父节点
LOG = (n).bit_length()
parent = [[0]*(n+1) for _ in range(LOG)]
depth = [0]*(n+1)
visited = [False]*(n+1)
def dfs(u, p):
    visited[u] = True
    parent[0][u] = p
    for v in tree[u]:
        if not visited[v]:
            depth[v] = depth[u] + 1
            dfs(v, u)
dfs(1, 0)   # 任意选 1 作为根

# 构建二进制倍增表
for k in range(1, LOG):
    for i in range(1, n+1):
        parent[k][i] = parent[k-1][parent[k-1][i]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    k = 0
    while diff:
        if diff & 1:
            u = parent[k][u]
        diff //= 2
        k += 1
    if u == v:
        return u
    for k in range(LOG-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

def dist(u, v):
    return depth[u] + depth[v] - 2 * depth[lca(u, v)]

# 读取 m 次查询，每次查询三个点 a, b, c
queries = []
for _ in range(m):
    a, b, c = map(int, input().split())
    queries.append((a, b, c))

# 对于三个点，结合 Steiner Tree 的性质，
# 总花费 = (dist(a,b)+dist(a,c)+dist(b,c))//2，
# 合适的集合点可以选三个 lca 中深度最大的那个
for a, b, c in queries:
    l1 = lca(a, b)
    l2 = lca(a, c)
    l3 = lca(b, c)
    candidate = l1
    if depth[l2] > depth[candidate]:
        candidate = l2
    if depth[l3] > depth[candidate]:
        candidate = l3
    total_cost = (dist(a, b) + dist(a, c) + dist(b, c)) // 2
    print(candidate, total_cost)
