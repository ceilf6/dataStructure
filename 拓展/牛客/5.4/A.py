import sys
sys.setrecursionlimit(1 << 25)
from collections import defaultdict

def build_tree(parents):
    tree = defaultdict(list)
    for i, p in enumerate(parents):
        tree[p].append(i + 2)  # 因为编号是从 1 开始，第 i 个是 i+2
    return tree

def dfs(u, p, d, tree, depth, fa, LOG=17):
    depth[u] = d
    fa[u][0] = p
    for i in range(1, LOG):
        fa[u][i] = fa[fa[u][i - 1]][i - 1]
    for v in tree[u]:
        if v != p:
            dfs(v, u, d + 1, tree, depth, fa)

def lca(u, v, depth, fa, LOG=17):
    if depth[u] < depth[v]:
        u, v = v, u
    for i in reversed(range(LOG)):
        if depth[fa[u][i]] >= depth[v]:
            u = fa[u][i]
    if u == v:
        return u
    for i in reversed(range(LOG)):
        if fa[u][i] != fa[v][i]:
            u = fa[u][i]
            v = fa[v][i]
    return fa[u][0]

def find_lca_for_nodes(nodes, depth, fa):
    curr = nodes[0]
    for node in nodes[1:]:
        curr = lca(curr, node, depth, fa)
    return curr

def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    keys = list(map(int, input().split()))
    a_weight = [0] + list(map(int, input().split()))
    a_parents = list(map(int, input().split()))
    b_weight = [0] + list(map(int, input().split()))
    b_parents = list(map(int, input().split()))

    LOG = 17  # 因为最多10^5节点，2^17 > 10^5

    # 建树
    tree_a = build_tree(a_parents)
    tree_b = build_tree(b_parents)

    # fa[i][j] 表示 i 的 2^j 祖先
    fa_a = [[0]*LOG for _ in range(N+1)]
    depth_a = [0]*(N+1)
    dfs(1, 0, 0, tree_a, depth_a, fa_a)

    fa_b = [[0]*LOG for _ in range(N+1)]
    depth_b = [0]*(N+1)
    dfs(1, 0, 0, tree_b, depth_b, fa_b)

    ans = 0
    for i in range(K):
        temp = keys[:i] + keys[i+1:]
        lca_a = find_lca_for_nodes(temp, depth_a, fa_a)
        lca_b = find_lca_for_nodes(temp, depth_b, fa_b)
        if a_weight[lca_a] > b_weight[lca_b]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
