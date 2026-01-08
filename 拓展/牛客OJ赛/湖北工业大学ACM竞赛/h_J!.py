import heapq

n = int(input())
courses = []
for _ in range(n):
    a, b, c, t = map(int, input().split())
    total = a + b + c
    if total <= t:
        courses.append((t, total))

courses.sort()
max_heap = []
current_time = 0

for t_i, total in courses:
    heapq.heappush(max_heap, -total)
    current_time += total
    if current_time > t_i:
        removed = -heapq.heappop(max_heap)
        current_time -= removed

print(len(max_heap))
