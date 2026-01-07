import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.len = r - l + 1
        # 1 的信息
        self.ones = {
            'cnt': 0,
            'pre': 0,
            'suf': 0,
            'max': 0
        }
        # 0 的信息
        self.zeros = {
            'cnt': 0,
            'pre': 0,
            'suf': 0,
            'max': 0
        }
        self.left = None
        self.right = None
        self.lazy_assign = None  # None表示没有赋值操作，取值0或1则表示需要将该区间整体赋值为对应值
        self.lazy_flip = False   # 懒延迟翻转标记

def merge(left_node, right_node):
    """合并两个子节点的信息"""
    res = {}
    # 对于1的信息
    res['ones_cnt'] = left_node.ones['cnt'] + right_node.ones['cnt']
    if left_node.ones['pre'] == left_node.len:
        ones_pre = left_node.len + right_node.ones['pre']
    else:
        ones_pre = left_node.ones['pre']
    if right_node.ones['suf'] == right_node.len:
        ones_suf = right_node.len + left_node.ones['suf']
    else:
        ones_suf = right_node.ones['suf']
    ones_max = max(left_node.ones['max'], right_node.ones['max'], left_node.ones['suf'] + right_node.ones['pre'])
    # 对于0 的信息
    res['zeros_cnt'] = left_node.zeros['cnt'] + right_node.zeros['cnt']
    if left_node.zeros['pre'] == left_node.len:
        zeros_pre = left_node.len + right_node.zeros['pre']
    else:
        zeros_pre = left_node.zeros['pre']
    if right_node.zeros['suf'] == right_node.len:
        zeros_suf = right_node.len + left_node.zeros['suf']
    else:
        zeros_suf = right_node.zeros['suf']
    zeros_max = max(left_node.zeros['max'], right_node.zeros['max'], left_node.zeros['suf'] + right_node.zeros['pre'])
    return ones_pre, ones_suf, ones_max, res['ones_cnt'], zeros_pre, zeros_suf, zeros_max, res['zeros_cnt']

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.root = self.build(0, self.n - 1, data)
        
    def build(self, l, r, data):
        node = Node(l, r)
        if l == r:
            val = data[l]
            if val == 1:
                node.ones = {'cnt': 1, 'pre': 1, 'suf': 1, 'max': 1}
                node.zeros = {'cnt': 0, 'pre': 0, 'suf': 0, 'max': 0}
            else:
                node.ones = {'cnt': 0, 'pre': 0, 'suf': 0, 'max': 0}
                node.zeros = {'cnt': 1, 'pre': 1, 'suf': 1, 'max': 1}
            return node
        mid = (l + r) // 2
        node.left = self.build(l, mid, data)
        node.right = self.build(mid + 1, r, data)
        self.pull_up(node)
        return node

    def pull_up(self, node):
        ones_pre, ones_suf, ones_max, ones_cnt, zeros_pre, zeros_suf, zeros_max, zeros_cnt = merge(node.left, node.right)
        node.ones = {'cnt': ones_cnt, 'pre': ones_pre, 'suf': ones_suf, 'max': ones_max}
        node.zeros = {'cnt': zeros_cnt, 'pre': zeros_pre, 'suf': zeros_suf, 'max': zeros_max}

    def apply_assign(self, node, val):
        """将节点全部赋值为 val (0或1)"""
        if val == 1:
            node.ones = {'cnt': node.len, 'pre': node.len, 'suf': node.len, 'max': node.len}
            node.zeros = {'cnt': 0, 'pre': 0, 'suf': 0, 'max': 0}
        else:
            node.ones = {'cnt': 0, 'pre': 0, 'suf': 0, 'max': 0}
            node.zeros = {'cnt': node.len, 'pre': node.len, 'suf': node.len, 'max': node.len}
        node.lazy_assign = val
        node.lazy_flip = False  # 清除翻转标记

    def apply_flip(self, node):
        """翻转节点的信息"""
        # 交换 ones 和 zeros 信息
        node.ones, node.zeros = node.zeros, node.ones
        if node.lazy_assign is not None:
            # 如果存在赋值操作，翻转后赋值为相反值
            node.lazy_assign = 1 - node.lazy_assign
        else:
            node.lazy_flip = not node.lazy_flip

    def push_down(self, node):
        if node.lazy_assign is not None:
            # 下传赋值操作到左右子节点
            self.apply_assign(node.left, node.lazy_assign)
            self.apply_assign(node.right, node.lazy_assign)
            node.lazy_assign = None
        if node.lazy_flip:
            self.apply_flip(node.left)
            self.apply_flip(node.right)
            node.lazy_flip = False

    def update_assign(self, node, L, R, val):
        # 完全不交集
        if node.r < L or node.l > R:
            return
        # 完全覆盖
        if L <= node.l and node.r <= R:
            self.apply_assign(node, val)
            return
        self.push_down(node)
        self.update_assign(node.left, L, R, val)
        self.update_assign(node.right, L, R, val)
        self.pull_up(node)

    def update_flip(self, node, L, R):
        if node.r < L or node.l > R:
            return
        if L <= node.l and node.r <= R:
            self.apply_flip(node)
            return
        self.push_down(node)
        self.update_flip(node.left, L, R)
        self.update_flip(node.right, L, R)
        self.pull_up(node)

    def query_range(self, node, L, R):
        # 返回一个节点的信息字典，结构与叶节点类似
        if node.r < L or node.l > R:
            # 构造一个空节点信息，空区间：
            res = Node(0,0)
            res.len = 0
            res.ones = {'cnt': 0, 'pre': 0, 'suf': 0, 'max': 0}
            res.zeros = {'cnt': 0, 'pre': 0, 'suf': 0, 'max': 0}
            return res
        if L <= node.l and node.r <= R:
            return node
        self.push_down(node)
        left_res = self.query_range(node.left, L, R)
        right_res = self.query_range(node.right, L, R)
        return self.merge_query(left_res, right_res)

    def merge_query(self, left_node, right_node):
        if left_node.len == 0:
            return right_node
        if right_node.len == 0:
            return left_node
        new_node = Node(0,0)
        new_node.len = left_node.len + right_node.len
        ones_pre, ones_suf, ones_max, ones_cnt, zeros_pre, zeros_suf, zeros_max, zeros_cnt = merge(left_node, right_node)
        new_node.ones = {'cnt': ones_cnt, 'pre': ones_pre, 'suf': ones_suf, 'max': ones_max}
        new_node.zeros = {'cnt': zeros_cnt, 'pre': zeros_pre, 'suf': zeros_suf, 'max': zeros_max}
        return new_node

    # 对外接口
    def update_set0(self, L, R):
        self.update_assign(self.root, L, R, 0)
        
    def update_set1(self, L, R):
        self.update_assign(self.root, L, R, 1)
        
    def update_flip_range(self, L, R):
        self.update_flip(self.root, L, R)
        
    def query_ones_count(self, L, R):
        nd = self.query_range(self.root, L, R)
        return nd.ones['cnt']
    
    def query_max_ones(self, L, R):
        nd = self.query_range(self.root, L, R)
        return nd.ones['max']


n,m=map(int,input().split())
data = list(map(int,input().split()))
st = SegmentTree(data)
for _ in range(m):
    op,l,r=map(int,input().split())
    if op == 0:
        st.update_set0(l, r)
    elif op == 1:
        st.update_set1(l, r)
    elif op == 2:
        st.update_flip_range(l, r)
    elif op == 3:
        print(st.query_ones_count(l, r))
    elif op == 4:
        print(st.query_max_ones(l, r))

