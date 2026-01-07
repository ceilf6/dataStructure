n = int(input())
s = input().strip()
k = list(map(int, input().split()))

# 预处理括号序列，获取每个push操作的深度
d_arr = []
current_depth = 0
for c in s:
    if c == '(':
        d_arr.append(current_depth)
        current_depth += 1
    else:
        current_depth -= 1

# 统计每个深度的出现次数
depth_count = {}
for d in d_arr:
    depth_count[d] = depth_count.get(d, 0) + 1

# 对颜色数组进行分组排序
groups = {}
current_pos = 0
sorted_depths = sorted(depth_count.keys())
k_sorted = sorted(k)

possible = True
for depth in sorted_depths:
    count = depth_count[depth]
    if current_pos + count > len(k_sorted):
        possible = False
        break
    group = k_sorted[current_pos : current_pos + count]
    # 检查组内是否严格递增
    for i in range(len(group) - 1):
        if group[i] >= group[i+1]:
            possible = False
            break
    if not possible:
        break
    groups[depth] = group
    current_pos += count

if current_pos != len(k_sorted):
    possible = False

if not possible:
    print("NO")
else:
    # 生成结果
    current_indices = {depth: 0 for depth in sorted_depths}
    result = []
    for d in d_arr:
        idx = current_indices[d]
        result.append(str(groups[d][idx]))
        current_indices[d] += 1
    print(' '.join(result))
