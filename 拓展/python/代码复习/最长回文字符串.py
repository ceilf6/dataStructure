def lggl(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    C = R = max_len = center = 0

    for i in range(n):
        # 核心对称计算
        p[i] = min(p[2*C-i], R-i) if i < R else 0
        
        # 边界扩展
        while i+p[i]+1 < n and i-p[i]-1 >= 0 and t[i+p[i]+1] == t[i-p[i]-1]:
            p[i] += 1

        # 更新中心及右边界
        if i + p[i] > R:
            C, R = i, i + p[i]

        # 记录最大值
        if p[i] > max_len:
            max_len, center = p[i], i

    return s[(center - max_len)//2 : (center + max_len)//2]

print(lggl('asddsaeds'))
