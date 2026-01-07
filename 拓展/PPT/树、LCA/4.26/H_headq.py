import heapq

n, m = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(n)]

heap = []

# 初始化堆，x=1时每个函数的值
for i in range(n):
    A, B, C = abc[i]
    val = A * 1 * 1 + B * 1 + C
    heapq.heappush(heap, (val, i, 1))  # (函数值, 函数编号, 当前x)

res = []

for _ in range(m):
    val, idx, x = heapq.heappop(heap)
    res.append(val)
    A, B, C = abc[idx]
    next_x = x + 1
    next_val = A * next_x * next_x + B * next_x + C
    heapq.heappush(heap, (next_val, idx, next_x))

print(*res)
