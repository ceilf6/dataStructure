from collections import defaultdict

n, m = map(int, input().split())
mp = defaultdict(int)  # 使用 defaultdict 来替代 C++ 中的 map，避免初始化问题
id_map = {}  # 用于记录唯一标识符
cnt = 0
str_list = [''] * (n + 1)  # str 数组，保留每一行的字符串
nums = [[0] * (m + 1) for _ in range(n + 1)]  # nums 数组，保存每个输入的数字
vec = []

# 排序时使用的比较函数
def cmp(a, b):
    if mp[str_list[a]] == mp[str_list[b]]:
        for i in range(1, m + 1):
            if nums[a][i] != nums[b][i]:
                return nums[a][i] < nums[b][i]
    return mp[str_list[a]] < mp[str_list[b]]

# 读取输入数据
for i in range(1, n + 1):
    for j in range(1, m + 1):
        nums[i][j] = int(input())
    # 构造每一行的字符串
    str_list[i] = ''.join(map(str, nums[i][1:m + 1]))
    mp[str_list[i]] += 1
    if mp[str_list[i]] == 1:
        cnt += 1
        vec.append(i)

# 输出计数
print(cnt)

# 排序 vec
vec.sort(key=lambda x: (mp[str_list[x]], [nums[x][i] for i in range(1, m + 1)]))

# 输出结果
for i in vec:
    print(mp[str_list[i]], str_list[i])
