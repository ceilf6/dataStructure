def max_nested_depth(N, edges, labels):
    # 构建树的邻接表
    tree = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # 深度优先搜索计算最大嵌套深度
    def dfs(node, depth, parent):
        nonlocal max_depth
        if labels[node - 1] == '(':
            depth += 1
        else:
            depth -= 1

        max_depth = max(max_depth, depth)

        for child in tree[node]:
            if child != parent:
                dfs(child, depth, node)

    max_depth = 0
    dfs(1, 0, 0)
    return max_depth

# 示例输入
N = 3
edges = [(1, 2), (1, 3)]
labels = ['(', ')', '(']

# 计算并输出结果
print(max_nested_depth(N, edges, labels))
