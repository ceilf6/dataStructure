n, q = map(int, input().split())
a = list(map(int, input().split()))

# 预计算所有区间的答案
ans = [[0] * n for _ in range(n)]

for l in range(n):
    for r in range(l, n):
        count = 0
        # 枚举区间[l,r]内的所有子区间
        for i in range(l, r + 1):
            for j in range(i, r + 1):
                # 检查子区间[i,j]是否为等差数列
                length = j - i + 1
                if length <= 2:
                    count += 1
                else:
                    # 检查等差数列
                    diff = a[i + 1] - a[i]
                    is_arithmetic = True
                    for k in range(i + 2, j + 1):
                        if a[k] - a[k - 1] != diff:
                            is_arithmetic = False
                            break
                    if is_arithmetic:
                        count += 1
        ans[l][r] = count

# 处理查询
for _ in range(q):
    l, r = map(int, input().split())
    print(ans[l - 1][r - 1])
