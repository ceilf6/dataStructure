# -*- coding: utf-8 -*-

def update(idx, l, r, ql, qr):
    if lazy[idx]:
        tree[idx] = (r - l + 1) - tree[idx]
        if l != r:
            lazy[idx*2] ^= 1
            lazy[idx*2+1] ^= 1
        lazy[idx] = 0
    if r < ql or l > qr:
        return
    if ql <= l and r <= qr:
        tree[idx] = (r - l + 1) - tree[idx]
        if l != r:
            lazy[idx*2] ^= 1
            lazy[idx*2+1] ^= 1
        return
    mid = (l + r) // 2
    update(idx*2, l, mid, ql, qr)
    update(idx*2+1, mid+1, r, ql, qr)
    tree[idx] = tree[idx*2] + tree[idx*2+1]

def query(idx, l, r, ql, qr):
    if lazy[idx]:
        tree[idx] = (r - l + 1) - tree[idx]
        if l != r:
            lazy[idx*2] ^= 1
            lazy[idx*2+1] ^= 1
        lazy[idx] = 0
    if r < ql or l > qr:
        return 0
    if ql <= l and r <= qr:
        return tree[idx]
    mid = (l + r) // 2
    return query(idx*2, l, mid, ql, qr) + query(idx*2+1, mid+1, r, ql, qr)

if __name__ == '__main__':
    n, m = map(int, input().split())
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)
    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            update(1, 1, n, a, b)
        elif c == 1:
            print(query(1, 1, n, a, b))
