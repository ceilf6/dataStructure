t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = []
    if k == 2:
        # 棋盘式填充：相邻格子颜色不同
        for i in range(n):
            row = []
            for j in range(m):
                # (i+j)奇偶性决定颜色，0为黑(1)，1为白(2)
                row.append('1' if (i + j) % 2 == 0 else '2')
            grid.append(' '.join(row))
    else:
        # 分组交替填充：每两行使用不同的数字对
        pairs = k // 2
        for i in range(n):
            row = []
            # 确定当前行使用哪个数字对
            pair_idx = i % pairs
            num1 = pair_idx + 1
            num2 = k - pair_idx
            for j in range(m):
                # 列号奇偶性决定使用哪个数字
                row.append(str(num1) if j % 2 == 0 else str(num2))
            grid.append(' '.join(row))
    # 输出当前测试用例的网格
    print('\n'.join(grid))
