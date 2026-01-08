n = int(input())
degrees = [0] * (n + 1)  # 节点编号从1到n

for _ in range(n-1):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1

D = max(degrees[1:])
has_less = any(deg < D for deg in degrees[1:])

if has_less:
    candidates = [i for i in range(1, n+1) if degrees[i] <= D-1]
    min_node = min(candidates)
    print(D-1, min_node)
else:
    print(D, 1)
