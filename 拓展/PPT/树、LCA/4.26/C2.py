class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.sum = 0  # 区间内灯的总数（开着的灯数量）
        self.lazy = 0  # 懒惰标记（记录是否需要翻转）
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.root = self._build(0, n - 1)

    def _build(self, l, r):
        node = Node(l, r)
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = self._build(l, mid)
        node.right = self._build(mid + 1, r)
        return node

    def _push_down(self, node):
        if node.lazy:
            # 翻转当前节点的状态
            node.sum = (node.r - node.l + 1) - node.sum
            if node.left and node.right:
                # 将懒惰标记传递给子节点
                node.left.lazy ^= 1
                node.right.lazy ^= 1
            node.lazy = 0

    def _update(self, node, L, R):
        self._push_down(node)
        if node.r < L or node.l > R:
            return
        if L <= node.l and node.r <= R:
            # 翻转当前区间
            node.lazy ^= 1
            self._push_down(node)
            return
        self._update(node.left, L, R)
        self._update(node.right, L, R)
        node.sum = node.left.sum + node.right.sum

    def _query(self, node, L, R):
        self._push_down(node)
        if node.r < L or node.l > R:
            return 0
        if L <= node.l and node.r <= R:
            return node.sum
        return self._query(node.left, L, R) + self._query(node.right, L, R)

    def update(self, L, R):
        self._update(self.root, L, R)

    def query(self, L, R):
        return self._query(self.root, L, R)



n,m=map(int,input().split())
st=SegmentTree(n)
for i in range(m):
    k,l,r=map(int,input().split())
    if k==0:
        st.update(l-1,r-1)
    else:
        print(st.query(l-1,r-1))
