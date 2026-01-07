class Node:                 # 节点类
    def __init__(self, l, r):
        self.l = l          # 区间左端点
        self.r = r          # 区间右端点
        self.left = None    # 左子节点
        self.right = None   # 右子节点
        self.sum = 0        # 区间和
        self.max = -float('inf')  # 区间最大值
        self.min = float('inf')   # 区间最小值
        self.mul = 1       # 乘法延迟标记(初始为1)
        self.add = 0       # 加法延迟标记(初始为0)
        
class Tree:
    '''
    构造及更新部分
    '''
    def __init__(self, data, mod):  # 增加mod参数
        self.n = len(data)
        self.mod = mod      # 存储模数
        self.root = self._build(0, self.n - 1, data)
    
    def _build(self, l, r, data):
        """构建线段树"""
        node = Node(l, r)
        if l == r:  # 叶子节点
            node.sum = data[l] % self.mod  # 初始值取模
            node.max = data[l] % self.mod
            node.min = data[l] % self.mod
            return node
        mid = (l + r) // 2
        node.left = self._build(l, mid, data)
        node.right = self._build(mid+1, r, data)
        node.sum = (node.left.sum + node.right.sum) % self.mod
        node.max = max(node.left.max, node.right.max)
        node.min = min(node.left.min, node.right.min)
        return node
    
    def _push_down(self, node):
        """下推懒惰延迟更新标记"""
        # 先处理乘法，再处理加法
        if node.mul != 1 or node.add != 0:
            left = node.left
            right = node.right
            
            # 更新左子树
            if node.mul != 1:
                left.sum = (left.sum * node.mul) % self.mod
                left.max = (left.max * node.mul) % self.mod
                left.min = (left.min * node.mul) % self.mod
                left.mul = (left.mul * node.mul) % self.mod
                left.add = (left.add * node.mul) % self.mod
                
            if node.add != 0:
                left.sum = (left.sum + node.add * (left.r - left.l + 1)) % self.mod
                left.max = (left.max + node.add) % self.mod
                left.min = (left.min + node.add) % self.mod
                left.add = (left.add + node.add) % self.mod
            
            # 更新右子树
            if node.mul != 1:
                right.sum = (right.sum * node.mul) % self.mod
                right.max = (right.max * node.mul) % self.mod
                right.min = (right.min * node.mul) % self.mod
                right.mul = (right.mul * node.mul) % self.mod
                right.add = (right.add * node.mul) % self.mod
                
            if node.add != 0:
                right.sum = (right.sum + node.add * (right.r - right.l + 1)) % self.mod
                right.max = (right.max + node.add) % self.mod
                right.min = (right.min + node.add) % self.mod
                right.add = (right.add + node.add) % self.mod
            
            # 清除标记
            node.mul = 1
            node.add = 0


    
    def update_mul(self, L, R, k):
        """区间乘法更新：[L, R] 乘以 k"""
        self._update_mul(self.root, L, R, k % self.mod)  # 参数取模
    
    def _update_mul(self, node, L, R, k):
        if node.r < L or node.l > R:
            return
        if L <= node.l and node.r <= R:
            # 更新当前节点
            node.sum = (node.sum * k) % self.mod
            node.max = (node.max * k) % self.mod
            node.min = (node.min * k) % self.mod
            node.mul = (node.mul * k) % self.mod
            node.add = (node.add * k) % self.mod  # 加法标记也需要乘k
            return
        self._push_down(node)
        self._update_mul(node.left, L, R, k)
        self._update_mul(node.right, L, R, k)
        node.sum = (node.left.sum + node.right.sum) % self.mod
        node.max = max(node.left.max, node.right.max)
        node.min = min(node.left.min, node.right.min)


    
    def update_add(self, L, R, val):
        """区间加法更新：[L, R] 加上 val"""
        self._update_add(self.root, L, R, val % self.mod)  # 参数取模
    
    def _update_add(self, node, L, R, val):
        if node.r < L or node.l > R:
            return
        if L <= node.l and node.r <= R:
            node.sum = (node.sum + val * (node.r - node.l + 1)) % self.mod
            node.max = (node.max + val) % self.mod
            node.min = (node.min + val) % self.mod
            node.add = (node.add + val) % self.mod
            return
        self._push_down(node)
        self._update_add(node.left, L, R, val)
        self._update_add(node.right, L, R, val)
        node.sum = (node.left.sum + node.right.sum) % self.mod
        node.max = max(node.left.max, node.right.max)
        node.min = min(node.left.min, node.right.min)





    '''
    下面是查询部分
    '''
    def query_sum(self, L, R):
        """区间和查询"""
        return self._query_sum(self.root, L, R) % self.mod  # 结果取模
    
    def _query_sum(self, node, L, R):
        if node.r < L or node.l > R:
            return 0
        if L <= node.l and node.r <= R:
            return node.sum
        self._push_down(node)
        return (self._query_sum(node.left, L, R) + self._query_sum(node.right, L, R)) % self.mod
    
    def query_max(self, L, R):
        """区间最大值查询"""
        return self._query_max(self.root, L, R) % self.mod
    
    def _query_max(self, node, L, R):
        if node.r < L or node.l > R:
            return -float('inf')
        if L <= node.l and node.r <= R:
            return node.max
        self._push_down(node)
        return max(self._query_max(node.left, L, R), self._query_max(node.right, L, R))
    
    def query_min(self, L, R):      # 有点像最小堆
        """区间最小值查询"""
        return self._query_min(self.root, L, R) % self.mod
    
    def _query_min(self, node, L, R):
        if node.r < L or node.l > R:
            return float('inf')
        if L <= node.l and node.r <= R:
            return node.min
        self._push_down(node)
        return min(self._query_min(node.left, L, R), self._query_min(node.right, L, R))


'''
P3372应用
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
st = Tree(a, float('inf'))
for _ in range(m):
    parts = input().split()
    if parts[0] == '1':
        L = int(parts[1])
        R = int(parts[2])
        val = int(parts[3])
        st.update_add(L-1, R-1, val)
    else:
        L = int(parts[1])
        R = int(parts[2])
        print(int(st.query_sum(L-1, R-1)))


'''
P3373应用
'''
n, m, q = map(int, input().split())
a = list(map(int, input().split()))
st = Tree(a, q)  # 传入模数参数
for _ in range(m):
    parts = input().split()
    if parts[0] == '1':
        L = int(parts[1]) - 1  # 转0-based
        R = int(parts[2]) - 1
        val = int(parts[3])
        st.update_mul(L, R, val)
    elif parts[0] == '2':
        L = int(parts[1]) - 1
        R = int(parts[2]) - 1
        val = int(parts[3])
        st.update_add(L, R, val)
    else:
        L = int(parts[1]) - 1
        R = int(parts[2]) - 1
        print(st.query_sum(L, R))

