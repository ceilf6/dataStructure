from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(int)

for _ in range(n):
    l = tuple(map(int, input().split()))
    d[l] += 1

# 按模块数降序，再按输出的字典序升序
sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))

print(len(sorted_items))
for output, count in sorted_items:
    print(count, *output)
