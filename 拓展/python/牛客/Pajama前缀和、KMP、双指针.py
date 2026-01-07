n = int(input())  # 读取 n 个用例

s = [[0] * 2 for _ in range(n)]

for i in range(n):
    s[i][0] = int(input())
    s[i][1] = input()

s1 = 'u'
s2 = 'uwawauwa'

s2_len = len(s2)

for i in range(n):
    text = s[i][1]
    text_len = s[i][0]

    # **前缀和预处理**：计算每个位置之前有多少个 'u'
    prefix_u = [0] * (text_len + 1)
    for j in range(text_len):
        prefix_u[j + 1] = prefix_u[j] + (1 if text[j] == 'u' else 0)

    # **寻找 `s2` 的匹配位置**
    j2 = s2_len - 1  # 从 `s2` 的最后一个字符开始匹配
    positions = []
    for j in range(text_len - 1, -1, -1):
        if text[j] == s2[j2]:  
            j2 -= 1  # 成功匹配一个字符
        if j2 == -1:  # 完全匹配 `s2`
            positions.append(j)  # 记录匹配 `s2` 结束的位置
            j2 = s2_len - 1  # 重新匹配 `s2`

    # **计算 `u` 的数量**
    result = sum(prefix_u[pos] for pos in positions)
    print(result)
