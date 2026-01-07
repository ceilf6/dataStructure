class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.data = []  # 用来存储当前数组的数据
        self.tree_sum = [0] * (4 * n)  # 存储区间和
        self.tree_weighted_sum = [0] * (4 * n)  # 存储加权和
        self.lazy_reverse = [False] * (4 * n)  # 用于反转的懒标记
        self.lazy_rotate = 0  # 循环右移的偏移量

    # 追加元素到数组末尾
    def append(self, val):
        self.data.append(val)
        self.update_all()  # 每次 append 后更新线段树
    
    # 更新整个线段树
    def update_all(self):
        self._build(0, 0, len(self.data) - 1)

    # 重新构建线段树
    def _build(self, node, start, end):
        if start == end:
            self.tree_sum[node] = self.data[start]
            self.tree_weighted_sum[node] = self.data[start] * (start + 1)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self._build(left_child, start, mid)
            self._build(right_child, mid + 1, end)
            self.push_up(node)

    # 向上传递区间和与加权和
    def push_up(self, node):
        self.tree_sum[node] = self.tree_sum[2 * node + 1] + self.tree_sum[2 * node + 2]
        self.tree_weighted_sum[node] = self.tree_weighted_sum[2 * node + 1] + self.tree_weighted_sum[2 * node + 2]

    # 反转操作（懒标记）
    def reverse(self):
        self.lazy_reverse = not self.lazy_reverse
        self.update_all()

    # 循环右移
    def rotate(self):
        if self.data:
            # 模拟循环右移
            self.data = [self.data[-1]] + self.data[:-1]
            self.update_all()

    # 获取rizziness
    def get_rizz(self):
        return self.tree_weighted_sum[0]  # 根节点的加权和就是整个数组的rizziness

# 处理多个测试用例
t = int(input())
for _ in range(t):
    q = int(input())
    seg = SegmentTree(100)  # 初始化一个数组最大长度为100的SegmentTree
    for _ in range(q):
        parts = input().split()
        op = int(parts[0])
        if op == 1:
            seg.rotate()  # 循环右移
        elif op == 2:
            seg.reverse()  # 反转数组
        elif op == 3:
            k = int(parts[1])
            seg.append(k)  # 追加元素
        print(seg.get_rizz())  # 输出魅值
