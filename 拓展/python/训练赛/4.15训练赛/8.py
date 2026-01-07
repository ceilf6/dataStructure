def is_valid_sudoku(grid):
    nums = set(range(1, 10))

    # 检查行
    for row in grid:
        if set(row) != nums:
            return 0

    # 检查列
    for col in zip(*grid):
        if set(col) != nums:
            return 0

    # 检查每个 3x3 宫格
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if set(block) != nums:
                return 0

    return 1

n = int(input())
results = []

for _ in range(n):
    grid = []
    for _ in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    results.append(is_valid_sudoku(grid))

for r in results:
    print(r)
