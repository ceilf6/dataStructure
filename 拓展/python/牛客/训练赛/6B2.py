def min_operations_to_equalize(arr):
    arr.sort()
    median = arr[len(arr) // 2]  # 取中位数
    min_operations = sum(abs(x - median) for x in arr)  # 计算操作次数
    return min_operations, median

# 读取输入
n = int(input())
arr = list(map(int, input().split()))

# 计算结果
operations, target = min_operations_to_equalize(arr)

# 输出结果
print(operations, target)
