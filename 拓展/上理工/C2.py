import bisect
import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = []
    for i in range(n):
        if b[i] >= a[i]:
            c.append(b[i] - a[i])
        else:
            c.append(m + b[i] - a[i])

    c.sort()

    # 预处理后缀最大逆时针操作步数
    suffix = [0] * (n + 1)  # suffix[i] 表示从第 i 个位置开始，最大逆时针步数
    for i in range(n - 1, -1, -1):
        suffix[i] = max(suffix[i + 1], m - c[i])

    # 枚举分界点
    res = float('inf')
    for i in range(n):
        max_cw = c[i]  # 前缀最大顺时针步数
        max_ccw = suffix[i + 1]  # 后缀最大逆时针步数
        res = min(res, max_cw + max_ccw)

    print(res)
