'''
n,m=map(int,input().split())

edges=[]

for i in range(m):
    edges.append(list(map(int,input().split())))

def bellman(n,edges,sta)
'''

n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, vval, pval = map(int, input().split())
    edges.append((u, v, vval, pval))

def has_positive_cycle(avg):
    new_edges = []
    for u, v, vval, pval in edges:
        new_edges.append((u, v, vval - avg * pval))

    # Bellman-Ford检测负环
    dist = [0] * (n + 1)  # 注意：要从任意点开始，所以初始化全为0
    for i in range(n):
        updated = False
        for u, v, w in new_edges:
            if dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            return False
    return True  # 第n轮还能更新 -> 存在正环

# 二分最大比值
l, r = 0, 1000
eps = 1e-4
ans = -1

while r - l > eps:
    mid = (l + r) / 2
    if has_positive_cycle(mid):
        ans = mid
        l = mid
    else:
        r = mid

if ans == -1:
    print(-1)
else:
    print(f"{ans:.1f}")
