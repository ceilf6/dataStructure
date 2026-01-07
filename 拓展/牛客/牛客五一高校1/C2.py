from collections import deque

n = int(input())
blacklists = [set() for _ in range(n + 1)]  # 存储每个女士不喜欢的男士

# 构建黑名单
for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    k = parts[0]
    if k == n:  # 如果有女士不喜欢所有男士，直接输出-1
        print(-1)
        exit()
    blacklists[i] = set(parts[1:])

# 左边是女士，右边是男士，L[i]表示第i位女士选择的男士
L = [0] * (n + 1)
# R[i]表示第i位男士被哪位女士选择
R = [0] * (n + 1)
# D[i]表示第i位女士的BFS层数
D = [0] * (n + 1)

# BFS搜索匹配路径
def bfs():
    q = deque()
    for u in range(1, n + 1):
        if L[u] == 0:  # 如果该女士没有匹配
            D[u] = 0
            q.append(u)
        else:
            D[u] = float('inf')
    
    found = False
    while q:
        u = q.popleft()
        for v in range(1, n + 1):
            if v in blacklists[u]:  # 如果这个男士在黑名单中，跳过
                continue
            if R[v] == 0:  # 找到一个未匹配的男士
                found = True
            elif D[R[v]] == float('inf'):  # 继续向前推进BFS层级
                D[R[v]] = D[u] + 1
                q.append(R[v])
    
    return found

# DFS搜索增广路径
def dfs(u):
    for v in range(1, n + 1):
        if v in blacklists[u]:  # 如果这个男士在黑名单中，跳过
            continue
        if R[v] == 0 or (D[R[v]] == D[u] + 1 and dfs(R[v])):
            L[u] = v
            R[v] = u
            return True
    D[u] = float('inf')
    return False

# 主流程：通过BFS寻找增广路径，并通过DFS进行增广
match = 0
while bfs():
    for u in range(1, n + 1):
        if L[u] == 0 and dfs(u):  # 如果该女士没有匹配，尝试通过DFS找到一个匹配
            match += 1

# 如果匹配数不足n，输出-1；否则输出匹配结果
print(-1 if match < n else ' '.join(map(str, L[1:])))
