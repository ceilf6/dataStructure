import sys
import math

class State:
    def __init__(self):
        self.next = [-1] * 26  # Using array for transitions, ord(c) - ord('a')
        self.link = -1
        self.len = 0

def build_sam(s):
    ord_a = ord('a')
    size = 1
    last = 0
    states = [State()]
    for c in s:
        c_ord = ord(c) - ord_a
        p = last
        curr = size
        states.append(State())
        states[curr].len = states[p].len + 1
        while p >= 0 and states[p].next[c_ord] == -1:
            states[p].next[c_ord] = curr
            p = states[p].link
        if p == -1:
            states[curr].link = 0
        else:
            q = states[p].next[c_ord]
            if states[p].len + 1 == states[q].len:
                states[curr].link = q
            else:
                clone = size + 1
                states.append(State())
                states[clone].len = states[p].len + 1
                states[clone].next = list(states[q].next)
                states[clone].link = states[q].link
                while p != -1 and states[p].next[c_ord] == q:
                    states[p].next[c_ord] = clone
                    p = states[p].link
                states[q].link = clone
                states[curr].link = clone
                size = clone
        last = curr
        size += 1
    return states

def process_b(sam, b):
    n = len(b)
    max_len = [0] * n
    current = 0
    length = 0
    ord_a = ord('a')
    for i in range(n):
        c = b[i]
        c_ord = ord(c) - ord_a
        while current != 0 and sam[current].next[c_ord] == -1:
            current = sam[current].link
            length = sam[current].len
        if sam[current].next[c_ord] != -1:
            current = sam[current].next[c_ord]
            length += 1
        else:
            current = 0
            length = 0
        max_len[i] = length
    return max_len

class SparseTable:
    def __init__(self, data):
        n = len(data)
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
        self.k = self.log_table[n] + 1
        self.st = []
        self.st.append(data.copy())
        j = 1
        while (1 << j) <= n:
            curr = []
            for i in range(n - (1 << j) + 1):
                val = min(self.st[j-1][i], self.st[j-1][i + (1 << (j-1))])
                curr.append(val)
            self.st.append(curr)
            j += 1
    
    def query_min(self, l, r):
        if l > r:
            return float('inf')
        length = r - l + 1
        k = self.log_table[length]
        return min(self.st[k][l], self.st[k][r - (1 << k) + 1])

n,m,k=map(int,input().split())

A=input()
v=list(map(int,input().split()))

B_list=[]
for i in range(k):
     B_list.append(input())


    
    # Build SAM for A
sam = build_sam(A)
    
for b in B_list:
        # Compute max_len for b
    max_len = process_b(sam, b)
        # Compute prefix sum
    sum_vals = [0] * (m +1)
    for i in range(m):
        sum_vals[i+1] = sum_vals[i] + v[i]
        # Build sparse table for sum_vals
    st = SparseTable(sum_vals)
    max_sum = 0
    for i in range(m):
        current_max_len = max_len[i]
        if current_max_len ==0:
            continue
        a_start = i - current_max_len +1
        if a_start <0:
            a_start =0
        a_end = i
        if a_start > a_end:
            continue
        min_val = st.query_min(a_start, a_end)
        current_sum = sum_vals[i+1] - min_val
        if current_sum > max_sum:
            max_sum = current_sum
    print(max(max_sum, 0))

