t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # 预处理每一位上1的数量
    bit_cnt = [0] * 30 #由题目规模可得

    for num in a:
        for b in range(30):
            if (num >> b) & 1:
                bit_cnt[b] += 1

    max_sum = 0
    for num in a:
        cur_sum = 0
        for b in range(30):
            bit = (num >> b) & 1
            if bit == 1:
                cur_sum += (n - bit_cnt[b]) * (1 << b)  # 与这一位为0的异或成1
            else:
                cur_sum += bit_cnt[b] * (1 << b)        # 与这一位为1的异或成1
        max_sum = max(max_sum, cur_sum)

    print(max_sum)
