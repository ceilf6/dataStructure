n, m = map(int, input().split())
l = list(map(int, input().split()))

def lowbit(x):
    return x & -x

def getsum(x):
    ans = 0
    while x > 0:
        ans += c[x]
        x -= lowbit(x)
    return ans

def add(x, k):
    while x <= n:
        c[x] += k
        x += lowbit(x)

# 初始化
c = [0] * (n + 2)  # 要开到n+1，因为有add(y+1)
for i in range(1, n+1):
    add(i, l[i-1])
    add(i+1, -l[i-1])

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        x, y, k = op[1], op[2], op[3]
        add(x, k)
        add(y+1, -k)
    else:
        x = op[1]
        print(getsum(x))
