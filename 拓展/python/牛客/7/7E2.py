def construct_sets(n):
    matrix = [[0] * n for _ in range(n)]  # 初始化 n×n 的矩阵
    
    # 第一行填充 1 到 n
    for j in range(n):
        matrix[0][j] = j + 1
    
    # 依次构造后续行，每行基于前一行循环右移，并填充首列
    for i in range(1, n):
        matrix[i][0] = matrix[i - 1][-1]  # 前一行最后一个数作为当前行的第一个数
        for j in range(1, n):
            matrix[i][j] = matrix[i - 1][j - 1]  # 其余部分右移
    
    # 输出结果
    for row in matrix:
        print(" ".join(map(str, row)))

# 读取输入
n = int(input().strip())
construct_sets(n)
