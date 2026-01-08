n, k = map(int, input().split())
n2 = list(map(int, input().split()))

n2.sort(reverse=True)  # 为了尽量选取最大的数字，先降序排列

# 用于存储每个余数模 k 下最多三个最大的值
n3 = [[] for _ in range(k)]

# 填充 n3，存储每个余数下的最多三个最大值
for num in n2:
    mod = num % k
    if len(n3[mod]) < 3:  # 每个余数最多存储 3 个数
        n3[mod].append(num)

ans = 0  # 用于存储最终答案

# 遍历所有可能的组合 i, j, q 满足 (i + j + q) % k == 0
for i in range(k):
    for j in range(k):
        q = (k - (i + j) % k) % k  # 确定第三个数的余数

        # 确保 i, j, q 的组合是有效的
        if i == j == q:  # i, j, q 都相等时，必须从同一组取 3 个数
            if len(n3[i]) >= 3:
                ans = max(ans, sum(n3[i][:3]))
        elif i == j:  # i == j 且 q 不等时，必须从 i 组取 2 个，从 q 组取 1 个
            if len(n3[i]) >= 2 and len(n3[q]) >= 1:
                ans = max(ans, n3[i][0] + n3[i][1] + n3[q][0])
        elif i == q:  # i == q 且 j 不等时，必须从 i 组取 2 个，从 j 组取 1 个
            if len(n3[i]) >= 2 and len(n3[j]) >= 1:
                ans = max(ans, n3[i][0] + n3[i][1] + n3[j][0])
        elif j == q:  # j == q 且 i 不等时，必须从 j 组取 2 个，从 i 组取 1 个
            if len(n3[j]) >= 2 and len(n3[i]) >= 1:
                ans = max(ans, n3[j][0] + n3[j][1] + n3[i][0])
        else:  # i, j, q 都不相等时，各取 1 个数
            if len(n3[i]) >= 1 and len(n3[j]) >= 1 and len(n3[q]) >= 1:
                ans = max(ans, n3[i][0] + n3[j][0] + n3[q][0])

print(ans)
