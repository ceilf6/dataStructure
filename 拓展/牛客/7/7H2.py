# 函数：检查是否满足停止条件
def check_stop_condition(arr):
    max_val = max(map(max, arr))  # 获取二维数组中的最大值
    min_val = min(map(min, arr))  # 获取二维数组中的最小值
    
    # 判断是否有两个相同的最大值或最小值，或者是整个数组的值统一
    max_count = sum(row.count(max_val) for row in arr)
    min_count = sum(row.count(min_val) for row in arr)
    
    if max_count >= 2 or min_count >= 2:
        return 1
    elif all(all(x == max_val for x in row) for row in arr) or all(all(x == min_val for x in row) for row in arr):
        return 2
    return False

# 函数：进行一次循环操作
def process_array(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max(map(max, arr)):
                neighbors = []
                if i > 0: neighbors.append(arr[i-1][j])  # 上
                if i < rows - 1: neighbors.append(arr[i+1][j])  # 下
                if j > 0: neighbors.append(arr[i][j-1])  # 左
                if j < cols - 1: neighbors.append(arr[i][j+1])  # 右
                print(neighbors)
                arr[i][j] = min(neighbors)
                
                
            elif arr[i][j] == min(map(min, arr)):
                neighbors = []
                if i > 0: neighbors.append(arr[i-1][j])  # 上
                if i < rows - 1: neighbors.append(arr[i+1][j])  # 下
                if j > 0: neighbors.append(arr[i][j-1])  # 左
                if j < cols - 1: neighbors.append(arr[i][j+1])  # 右
                print(neighbors)
                arr[i][j] = max(neighbors)
    
    return arr

# 主函数
def process_until_condition_met(n,arr):
    while not check_stop_condition(arr):
        arr = process_array(n,arr)
    if check_stop_condition(arr) == 1:
        print('NO')
    elif check_stop_condition(arr) == 2:
        print('YES')

# 输入处理
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 处理数组
if n == 1:
    print('YES')
else:
    process_until_condition_met(n,arr)
