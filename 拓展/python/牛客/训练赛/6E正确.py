import math

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    k1 = math.ceil(y / (x + 1))
    k2 = math.ceil((y - 1) / (x + 1))

    n1 = 2 * k1
    n2 = 2 * k2 + 1

    print(max(min(n1, n2),0))
