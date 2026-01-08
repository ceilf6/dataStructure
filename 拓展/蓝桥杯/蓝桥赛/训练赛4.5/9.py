import re
import bisect

k = int(input())
s = input().strip()

# 正则表达式匹配独立的Alice和Bob
pattern_alice = r'(?<![a-zA-Z])Alice(?![a-zA-Z])'
pattern_bob = r'(?<![a-zA-Z])Bob(?![a-zA-Z])'

# 提取所有Alice的结束位置（start +5）
a_ends = []
for match in re.finditer(pattern_alice, s):
    a_ends.append(match.end())

# 提取所有Bob的起始位置和结束位置
b_starts = []
b_ends = []
for match in re.finditer(pattern_bob, s):
    start = match.start()
    b_starts.append(start)
    b_ends.append(start + 3)  # Bob的长度是3

# 处理情况一：Alice在Bob前面，中间字符数为b_start - a_end <=k
count_case1 = 0
if b_starts:
    b_starts_sorted = sorted(b_starts)
    for a_end in a_ends:
        left = a_end
        right = a_end + k
        # 使用bisect查找在范围内的数目
        l = bisect.bisect_left(b_starts_sorted, left)
        r = bisect.bisect_right(b_starts_sorted, right)
        count_case1 += (r - l)

# 处理情况二：Bob在Alice前面，中间字符数为a_start - b_end <=k
count_case2 = 0
if a_ends:
    a_starts = [match.start() for match in re.finditer(pattern_alice, s)]
    a_starts_sorted = sorted(a_starts)
    for b_end in b_ends:
        left = b_end
        right = b_end + k
        l = bisect.bisect_left(a_starts_sorted, left)
        r = bisect.bisect_right(a_starts_sorted, right)
        count_case2 += (r - l)

total = count_case1 + count_case2
print(total)
