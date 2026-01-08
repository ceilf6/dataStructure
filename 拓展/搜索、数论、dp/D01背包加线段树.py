import sys
from bisect import bisect_right

V = 10000

def merge(a, b, P):
    return max(a[s] + b[P - s] for s in range(P + 1))

class Info:
    def __init__(self):
        self.l = 0
        self.m = 0
        self.r = 0
        self.dpl = []
        self.dpr = []

class SegmentTree:
    def __init__(self, v, w):
        self.n = len(v)
        self.v = v
        self.w = w
        self.info = [Info() for _ in range(4 * self.n)]
        self.build(1, 0, self.n)
    
    def build(self, p, l, r):
        if r - l == 1:
            return
        m = (l + r) >> 1
        node = self.info[p]
        node.l, node.m, node.r = l, m, r
        self.build(p * 2, l, m)
        self.build(p * 2 + 1, m, r)
        node.dpl = [[0] * (V + 1) for _ in range(m - l + 1)]
        for i in range(m - 1, l - 1, -1):
            j = m - 1 - i
            node.dpl[j + 1] = node.dpl[j][:]
            for s in range(V, self.v[i] - 1, -1):
                node.dpl[j + 1][s] = max(node.dpl[j + 1][s], node.dpl[j][s - self.v[i]] + self.w[i])
        
        node.dpr = [[0] * (V + 1) for _ in range(r - m + 1)]
        for i in range(m, r):
            j = i - m
            node.dpr[j + 1] = node.dpr[j][:]
            for s in range(V, self.v[i] - 1, -1):
                node.dpr[j + 1][s] = max(node.dpr[j + 1][s], node.dpr[j][s - self.v[i]] + self.w[i])
    
    def query(self, p, l, r, P):
        if r - l == 1:
            return self.w[l] if self.v[l] <= P else 0
        node = self.info[p]
        m = node.m
        if node.l <= l < m < r <= node.r:
            return merge(node.dpl[m - l], node.dpr[r - m], P)
        if r <= m:
            return self.query(p * 2, l, r, P)
        return self.query(p * 2 + 1, l, r, P)

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    
    n = int(data[index])
    index += 1
    v = list(map(int, data[index:index + n]))
    index += n
    w = list(map(int, data[index:index + n]))
    index += n
    
    segment_tree = SegmentTree(v, w)
    
    Q = int(data[index])
    index += 1
    lst = 0
    result = []
    
    for _ in range(Q):
        iL, iR, iP = map(int, data[index:index + 3])
        index += 3
        L = (iL + lst) % n + 1
        R = (iR + lst) % n + 1
        if L > R:
            L, R = R, L
        P = (iP + lst) % V + 1
        L -= 1
        
        lst = segment_tree.query(1, L, R, P)
        result.append(str(lst))
    
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
