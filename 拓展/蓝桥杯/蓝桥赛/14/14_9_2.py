def compute_subtree_size(n, m, k):
    if m == 1:
        return max(n - k + 1, 0)
    total = 0
    layer = 0
    while True:
        m_power=m**layer
        # 计算当前层的起始结点s
        s = m_power * (k - 1) + (m_power - 1) // (m - 1) + 1
        if s > n:
            break
        # 当前层结束结点e = s + m^layer - 1
        e = s + m_power - 1
        if e <= n:
            total += m_power
        else:
            total += (n - s + 1)
            break
        layer += 1
    return total

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    print(compute_subtree_size(n, m, k))
