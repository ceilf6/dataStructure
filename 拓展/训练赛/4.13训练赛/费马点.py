import math

# 三个点 A, B, C
points = [(0, 0), (4, 0), (2, 3)]

# 计算一个点 P 到所有点的最大距离
def max_distance(P):
    return max(math.hypot(P[0]-x, P[1]-y) for x, y in points)

# 搜索范围（根据点的位置设定）
def find_optimal_point():
    # 粗略搜索范围
    l, r = 0.0, 5.0
    d, u = 0.0, 5.0
    best = float('inf')
    px, py = 0, 0

    step = 0.1
    while step > 1e-4:
        x = l
        while x <= r:
            y = d
            while y <= u:
                val = max_distance((x, y))
                if val < best:
                    best = val
                    px, py = x, y
                y += step
            x += step
        # 缩小搜索范围
        l, r = px - step, px + step
        d, u = py - step, py + step
        step /= 2
    return px, py, best

x, y, mindist = find_optimal_point()
print(f"最佳点: ({x:.5f}, {y:.5f})，最大距离最小值为: {mindist:.5f}")
