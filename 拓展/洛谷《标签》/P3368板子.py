MAXN = 100010
t1 = [0] * MAXN
t2 = [0] * MAXN
n = 0

def lowbit(x):
    return x & (-x)

def add(k, v):
    v1 = k * v
    while k <= n:
        t1[k] += v
        t2[k] += v1
        k += lowbit(k)

def getsum(tree, k):
    ret = 0
    while k:
        ret += tree[k]
        k -= lowbit(k)
    return ret

def add1(l, r, v):
    add(l, v)
    if r + 1 <= n:
        add(r + 1, -v)

def getsum1(l, r):
    # 获取区间[l, r]的和
    return r * getsum(t1, r) - (l - 1) * getsum(t1, l - 1) - (getsum(t2, r) - getsum(t2, l - 1))

# 预处理：将初始数组中的每个数放入 BIT 中
for i in range(1, n + 1):
    a = int(next(it))
    add1(i, i, a)

out_lines = []
for _ in range(m):
    op = next(it)
    if op == '1':
        x = int(next(it))
        y = int(next(it))
        k = int(next(it))
        add1(x, y, k)
    elif op == '2':
        x = int(next(it))
        # 查询第 x 个数点值，可表示为区间 [x,x] 的和
        val = getsum1(x, x)
        out_lines.append(str(val))
        
sys.stdout.write("\n".join(out_lines))
