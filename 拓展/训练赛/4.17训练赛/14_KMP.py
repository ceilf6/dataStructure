def kmp(text, pattern):
    # 构建部分匹配表（前缀函数）
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    # KMP 匹配过程
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1  # 匹配成功
    return -1  # 匹配失败

# 输入读取
n = int(input())
l = list(map(int, input().split()))
m = int(input())

matches = []
for i in range(m):
    temp = list(map(int, input().split()))
    k = temp[0]
    heights = temp[1:]
    pos = kmp(l, heights)
    matches.append((pos, i + 1))  # 存储匹配位置和编号

# 按匹配位置排序
matches.sort()
print(" ".join(str(x[1]) for x in matches))
