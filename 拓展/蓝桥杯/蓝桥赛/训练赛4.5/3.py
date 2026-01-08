# 初始化
prev_dp = [[0] * 10 for _ in range(26)]
prev_dp[0][0] = 1

for _ in range(7):  # 处理7个小朋友
    current_dp = [[0] * 10 for _ in range(26)]
    for sum_s_prev in range(26):
        for sum_a_prev in range(10):
            if prev_dp[sum_s_prev][sum_a_prev] == 0:
                continue
            # 当前小朋友的可能总糖果数s_i
            for s_i in [2, 3, 4, 5]:
                new_s = sum_s_prev + s_i
                if new_s > 25:
                    continue
                # 当前小朋友可能分到的第一种糖果数a_i
                for a_i in range(s_i + 1):
                    new_a = sum_a_prev + a_i
                    if new_a > 9:
                        continue
                    current_dp[new_s][new_a] += prev_dp[sum_s_prev][sum_a_prev]
    prev_dp = current_dp

print(prev_dp[25][9])
