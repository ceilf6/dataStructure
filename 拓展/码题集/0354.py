class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)  # 存储区间和
        self.lazy_set = [None] * (4 * n)  # 懒标记：区间赋值
        self.lazy_add = [0] * (4 * n)  # 懒标记：区间加减
    
    def push_down(self, node, l, r):
        """下推懒标记"""
        mid = (l + r) // 2
        
        if self.lazy_set[node] is not None:
            # 处理区间赋值懒标记
            val = self.lazy_set[node]
            self.tree[node * 2] = val * (mid - l + 1)
            self.tree[node * 2 + 1] = val * (r - mid)
            
            self.lazy_set[node * 2] = val
            self.lazy_set[node * 2 + 1] = val
            self.lazy_add[node * 2] = 0
            self.lazy_add[node * 2 + 1] = 0
            
            self.lazy_set[node] = None
        
        if self.lazy_add[node] != 0:
            # 处理区间加减懒标记
            add_val = self.lazy_add[node]
            
            self.tree[node * 2] += add_val * (mid - l + 1)
            self.tree[node * 2 + 1] += add_val * (r - mid)
            
            if self.lazy_set[node * 2] is not None:
                self.lazy_set[node * 2] += add_val
            else:
                self.lazy_add[node * 2] += add_val
                
            if self.lazy_set[node * 2 + 1] is not None:
                self.lazy_set[node * 2 + 1] += add_val
            else:
                self.lazy_add[node * 2 + 1] += add_val
            
            self.lazy_add[node] = 0
    
    def update_set(self, node, l, r, ql, qr, val):
        """区间赋值更新"""
        if ql <= l and r <= qr:
            self.tree[node] = val * (r - l + 1)
            self.lazy_set[node] = val
            self.lazy_add[node] = 0
            return
        
        self.push_down(node, l, r)
        mid = (l + r) // 2
        
        if ql <= mid:
            self.update_set(node * 2, l, mid, ql, qr, val)
        if qr > mid:
            self.update_set(node * 2 + 1, mid + 1, r, ql, qr, val)
        
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def update_add(self, node, l, r, ql, qr, val):
        """区间加减更新"""
        if ql <= l and r <= qr:
            self.tree[node] += val * (r - l + 1)
            if self.lazy_set[node] is not None:
                self.lazy_set[node] += val
            else:
                self.lazy_add[node] += val
            return
        
        self.push_down(node, l, r)
        mid = (l + r) // 2
        
        if ql <= mid:
            self.update_add(node * 2, l, mid, ql, qr, val)
        if qr > mid:
            self.update_add(node * 2 + 1, mid + 1, r, ql, qr, val)
        
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def query(self, node, l, r, ql, qr):
        """区间查询求和"""
        if ql <= l and r <= qr:
            return self.tree[node]
        
        self.push_down(node, l, r)
        mid = (l + r) // 2
        result = 0
        
        if ql <= mid:
            result += self.query(node * 2, l, mid, ql, qr)
        if qr > mid:
            result += self.query(node * 2 + 1, mid + 1, r, ql, qr)
        
        return result

def solve():
    n, m = map(int, input().split())
    seg_tree = SegmentTree(n)
    
    for _ in range(m):
        operation = list(map(int, input().split()))
        
        if operation[0] == 1:
            # 区间赋值
            l, r, x = operation[1], operation[2], operation[3]
            seg_tree.update_set(1, 1, n, l, r, x)
        elif operation[0] == 2:
            # 区间加减
            l, r, x = operation[1], operation[2], operation[3]
            seg_tree.update_add(1, 1, n, l, r, x)
        else:
            # 区间查询
            l, r = operation[1], operation[2]
            result = seg_tree.query(1, 1, n, l, r)
            print(result)

if __name__ == "__main__":
    solve()