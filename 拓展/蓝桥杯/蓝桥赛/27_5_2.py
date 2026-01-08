import bisect
from collections import defaultdict

mod = 10**9 + 7
n, d = map(int, input().split())
a = list(map(int, input().split()))

country = defaultdict(list)
for idx in range(n):
    country[a[idx]].append(idx)  # 电脑编号从1开始

result = 1
for key in country:
    positions = sorted(country[key])
    m = len(positions)
    pairs = 0
    for i in range(m):
        max_allowed = positions[i] + d
        j = bisect.bisect_right(positions, max_allowed)
        pairs += j - i - 1  # 统计[i+1, j-1]范围内的对数
    contrib = (1 + m + pairs) % mod
    result = (result * contrib) % mod

print((result - 1) % mod)
