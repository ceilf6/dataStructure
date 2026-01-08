MOD = 998244353

n, m = map(int, input().split())

from collections import defaultdict

def is_valid(pos, d):
    # 检查位置pos+1的奇偶性，决定d是否合法
    # 因为pos是当前处理到的位数，从0开始？
    # pos从0开始的话，第0位是第一位，奇数位
    return (d % 2) == ((pos + 1) % 2)

# 初始状态：处理第一位（i=1，pos=0）
# 四元组初始为 (None, None, None, d1)，其中d1是奇数，即d1 in {1,3,5,7,9}
# 为了简化，初始状态只记录可能的第四位，前三位不存在，用0填充，但奇偶性可能不匹配，但在i<5时不需要检查
# 所以初始状态的四元组为 (0, 0, 0, d1)
prev_dp = defaultdict(int)
for d in range(1, 10, 2):
    prev_dp[(0, 0, 0, d)] = 1

for i in range(2, n+1):
    curr_dp = defaultdict(int)
    # 当前处理到第i位（pos = i-1）
    pos = i - 1
    is_odd_pos = (i % 2 == 1)
    for last4, cnt in prev_dp.items():
        # 枚举当前可能的d
        if is_odd_pos:
            possible_d = [1, 3, 5, 7, 9]
        else:
            possible_d = [0, 2, 4, 6, 8]
        for d in possible_d:
            # 检查五位数和的条件
            if i >= 5:
                # 四元组last4是 (d1, d2, d3, d4)，对应i-4到i-1位
                # 当前五位是 d1, d2, d3, d4, d
                sum_five = sum(last4) + d
                if sum_five > m:
                    continue
            # 生成新的四元组
            new_last4 = (last4[1], last4[2], last4[3], d)
            curr_dp[new_last4] = (curr_dp[new_last4] + cnt) % MOD
    prev_dp = curr_dp

# 合并所有可能的状态
total = sum(prev_dp.values()) % MOD
print(total)
