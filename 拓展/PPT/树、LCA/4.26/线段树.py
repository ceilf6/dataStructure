class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(data, 2 * node, l, mid)
            self.build(data, 2 * node + 1, mid + 1, r)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return float('-inf')
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query(2 * node, l, mid, ql, qr)
        right = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return max(left, right)

    def update(self, node, l, r, idx, value):
        if l == r:
            if self.tree[node] < value:
                self.tree[node] = value
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node, l, mid, idx, value)
            else:
                self.update(2 * node + 1, mid + 1, r, idx, value)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])


# 主程序处理输入输出
n, m = map(int, input().split())
scores = list(map(int, input().split()))
seg = SegmentTree(scores)

for _ in range(m):
    parts = input().split()
    op = parts[0]
    a = int(parts[1]) - 1  # 转为 0-based
    b = int(parts[2])
    if op == 'Q':
        b -= 1  # 转为 0-based
        print(seg.query(1, 0, n - 1, a, b))
    elif op == 'U':
        seg.update(1, 0, n - 1, a, b)
