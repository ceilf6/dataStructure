import math

p = list(map(int, input().split()))
n = p[0]
k = p[1]

a = list(map(int, input().split()))

vis = [0] * 21
sum2 = 0

def ispr(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 0
    return 1

def dfs(step, m):
    global sum2
    if m == k:
        total = 0
        for i in range(n):
            if vis[i]:
                total += a[i]
        if ispr(total):
            sum2 += 1
            print(total)
        return
    if step == n:
        return
    vis[step] = 0
    dfs(step + 1, m)
    vis[step] = 1
    dfs(step + 1, m + 1)
    vis[step] = 0

dfs(0, 0)
print(sum2)
