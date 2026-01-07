def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # 如果 a 本来就能匹配 b，直接输出 0
    def check(arr, b):
        bi = 0
        for val in arr:
            if bi < len(b) and val >= b[bi]:
                bi += 1
        return bi == len(b)
    
    if check(a, b):
        print(0)
        return

    # 求 prefix 数组：
    # prefix[i] 表示 a 的前 i 个元素最多匹配 b 的多少个元素
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1]
        if prefix[i - 1] < m and a[i - 1] >= b[prefix[i - 1]]:
            prefix[i] += 1

    # 对于每个 k (0 <= k <= m)，记录能在 a 中最早匹配到 k 个 b 元素的下标
    L = [None] * (m + 1)
    for i in range(n + 1):
        # prefix 数组单调非减，所以第一次出现就可以记录
        if prefix[i] <= m and L[prefix[i]] is None:
            L[prefix[i]] = i

    # 求 suff 数组：
    # suff[i] 表示 a[i:] 贪心匹配 b 后，b 中未匹配部分的起始下标
    suff = [None] * (n + 1)
    suff[n] = m
    for i in range(n - 1, -1, -1):
        suff[i] = suff[i + 1]
        if suff[i + 1] > 0 and a[i] >= b[suff[i + 1] - 1]:
            suff[i] = suff[i + 1] - 1

    # 对于 candidate，中间匹配 b[k]，需满足：
    # 1. L[k] 存在（即 a[:L[k]] 能匹配 b 的前 k 个元素）
    # 2. a[L[k]:] 能匹配 b[k+1:]，即 suff[L[k]] <= k+1
    # candidate 需要 >= b[k]，答案取所有满足条件的 b[k] 的最小值
    ans = -1
    for k in range(m):
        if L[k] is not None and suff[L[k]] <= k + 1:
            if ans == -1 or b[k] < ans:
                ans = b[k]
    print(ans)

t = int(input())
for _ in range(t):
    solve()
