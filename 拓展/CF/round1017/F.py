from collections import deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1

    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3

        grid = [[0] * m for _ in range(n)]
        colors = [i + 1 for i in range(k)]
        count_per_color = (n * m) // k

        # 蛇形涂色
        
        color_queue = deque(colors * count_per_color)

        for i in range(n):
            row_range = range(m) if i % 2 == 0 else range(m-1, -1, -1)
            for j in row_range:

                for _ in range(len(color_queue)):
                    color = color_queue.popleft()
                    valid = True
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == color:
                            valid = False
                            break
                    if valid:
                        grid[i][j] = color
                        break
                    else:
                        color_queue.append(color)

        results.append('\n'.join(' '.join(map(str, row)) for row in grid))

    print('\n'.join(results))

solve()
