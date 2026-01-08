def min_operations(n, a):
    a.sort()
    median = a[n // 2]
    max_add = max(median - ai for ai in a)
    max_sub = max(ai - median for ai in a)
    total_operations = max_add + max_sub
    return total_operations, median

# 示例输入
n = 8
a = [3, 2, 4, 5, 2, 3, 4, 2]

# 计算最少操作次数和目标数
operations, target = min_operations(n, a)

# 输出结果
print(operations, target)
