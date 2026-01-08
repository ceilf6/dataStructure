# 方法1：使用zip和列表解包
def traverse_by_column1():
    # 创建示例二维数组
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # 使用zip(*matrix)按列遍历
    for column in zip(*matrix):
        print(f"当前列的元素：{column}")
        # 处理每一列的元素
        for element in column:
            print(element, end=' ')
        print()  # 换行

# 方法2：使用索引直接访问
def traverse_by_column2():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # 获取矩阵的行数和列数
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 外循环遍历列
    for j in range(cols):
        print(f"第{j+1}列的元素：", end=' ')
        # 内循环遍历每列中的元素
        for i in range(rows):
            print(matrix[i][j], end=' ')
        print()  # 换行

# 方法3：使用numpy（如果需要处理大型数组）
def traverse_by_column3():
    import numpy as np
    
    # 创建numpy数组
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    # 使用numpy的转置功能
    for column in matrix.T:
        print(f"当前列的元素：{column}")

if __name__ == "__main__":
    print("方法1：使用zip")
    print("-" * 20)
    traverse_by_column1()
    
    print("\n方法2：使用索引")
    print("-" * 20)
    traverse_by_column2()
    
    print("\n方法3：使用numpy")
    print("-" * 20)
    traverse_by_column3()