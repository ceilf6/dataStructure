def construct_sets(n):
    result = [[0] * n for _ in range(n)]
    cur = n + 1

    for i in range(n):
        # 设置对角线上的共享元素
        result[i][0] = (i + 1) if i != n - 1 else 1

    for i in range(n):
        for j in range(1, n):
            if i == 0:
                result[i][j] = j + 1  # 第一行是连续的
            else:
                # 共享元素在对角线，其余填充新的
                result[i][j] = cur
                cur += 1

    return result

# 读取输入
n = int(input().strip())
sets = construct_sets(n)

# 输出结果
for row in sets:
    print(" ".join(map(str, row)))
