# 函数：检查是否满足停止条件
def check_stop_condition(arr):
    rows, cols = len(arr), len(arr[0])

    # 判断是否有相邻的最大值或最小值
    for i in range(rows):
        for j in range(cols):
            # 获取相邻的四个方向的值（只考虑横向或纵向相邻）
            neighbors = []
            if i > 0: neighbors.append(arr[i-1][j])  # 上
            if i < rows - 1: neighbors.append(arr[i+1][j])  # 下
            if j > 0: neighbors.append(arr[i][j-1])  # 左
            if j < cols - 1: neighbors.append(arr[i][j+1])  # 右
            
            # 如果当前元素是最大值，且相邻有一个最大值
            if arr[i][j] == max(map(max, arr)) and any(neighbor == arr[i][j] for neighbor in neighbors):
                return True
            # 如果当前元素是最小值，且相邻有一个最小值
            if arr[i][j] == min(map(min, arr)) and any(neighbor == arr[i][j] for neighbor in neighbors):
                return True
    return False

# 函数：进行一次循环操作
def process_array(n, arr):
    rows, cols = len(arr), len(arr[0])
    
    # 复制数组，避免直接修改原数组
    new_arr = [row[:] for row in arr]

    for i in range(rows):
        for j in range(cols):
            # 获取相邻四个数的坐标（仅考虑横向和纵向相邻）
            neighbors = []
            if i > 0: neighbors.append(arr[i-1][j])  # 上
            if i < rows - 1: neighbors.append(arr[i+1][j])  # 下
            if j > 0: neighbors.append(arr[i][j-1])  # 左
            if j < cols - 1: neighbors.append(arr[i][j+1])  # 右

            # 最大值操作
            if arr[i][j] == max(map(max, arr)):
                new_arr[i][j] = max(neighbors)
            # 最小值操作
            elif arr[i][j] == min(map(min, arr)):
                new_arr[i][j] = min(neighbors)

    return new_arr

# 主函数
def process_until_condition_met(n, arr):
    while not check_stop_condition(arr):
        arr = process_array(n, arr)
    
    # 如果数组中所有元素都一致，输出 'YES'
    print('YES' if all(all(x == arr[0][0] for x in row) for row in arr) else 'NO')

# 输入处理
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 处理数组
if n == 1:
    print('YES')
else:
    process_until_condition_met(n, arr)
