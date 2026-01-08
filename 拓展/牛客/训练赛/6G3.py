import sys
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solve(n, a):
    a.sort()  # 按亮度排序，便于贪心选择
    used = [False] * n
    group_count = 0

    for i in range(n):
        if used[i]: 
            continue  # 已分组的跳过

        # 新建一组
        group_xor = 0
        group_min = a[i]
        group_lcm = a[i]

        for j in range(i, n):
            if used[j]: 
                continue

            # 试着加入当前组
            new_xor = group_xor ^ a[j]
            new_lcm = lcm(group_lcm, a[j])
            new_min = min(group_min, a[j])

            # 判断是否满足公式
            if new_lcm + new_xor == 2 * new_min:
                group_xor = new_xor
                group_lcm = new_lcm
                group_min = new_min
                used[j] = True  # 该星星已分组

        group_count += 1  # 记录分组数
    
    return group_count

# 读取输入
input = sys.stdin.read
data = input().split()
index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    results.append(str(solve(n, a)))

# 输出所有结果
sys.stdout.write("\n".join(results) + "\n")
