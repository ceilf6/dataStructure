# 定义新版国王的攻击方向（国王周围8格 + 马走日字的8格）
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1),
              (-2, -1), (-2, 1), (-1, -2), (-1, 2),
              (1, -2), (1, 2), (2, -1), (2, 1)]

def solve_case(n, m):
    max_count = 0
    best_board = []

    board = [[0] * m for _ in range(n)]
    attacked = [[0] * m for _ in range(n)]

    def is_safe(x, y):
        return board[x][y] == 0 and attacked[x][y] == 0

    def place_or_remove(x, y, delta):
        attacked[x][y] += delta
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                attacked[nx][ny] += delta

    def dfs(pos, count):
        nonlocal max_count, best_board
        if pos == n * m:
            if count > max_count:
                max_count = count
                best_board = [row[:] for row in board]
            return

        x, y = divmod(pos, m)

        # 不放
        dfs(pos + 1, count)

        # 放置新版国王
        if is_safe(x, y):
            board[x][y] = 1
            place_or_remove(x, y, 1)
            dfs(pos + 1, count + 1)
            place_or_remove(x, y, -1)
            board[x][y] = 0

    dfs(0, 0)

    return max_count, best_board

# 处理输入
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    count, result_board = solve_case(n, m)
    print(count)
    for row in result_board:
        print(''.join(['1' if cell else '0' for cell in row]))
