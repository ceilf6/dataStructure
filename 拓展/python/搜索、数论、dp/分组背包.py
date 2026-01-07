V, n = map(int, input().split())
from collections import defaultdict
group = defaultdict(list)
for _ in range(n):
    a, b, c = map(int, input().split())
    group[c].append((a, b))

F = [0] * (V + 1)
for k in group:  # K是字典，用in遍历每个组的实际编号
    for j in range(V, -1, -1):
        for cost, val in group[k]:
            if j >= cost:
                F[j] = max(F[j], F[j - cost] + val)
print(F[V])
