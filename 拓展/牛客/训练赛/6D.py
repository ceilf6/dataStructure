def min_t_length(n, s):
    result = 0  # 用于存储最终的异或结果

    for k in range(1, n + 1):  # 遍历所有 k
        substrings = {}  # 记录子串及其最早出现的位置
        t = []  # 构造 t

        for i in range(n - k + 1):  # 生成所有长为 k 的子串
            sub = s[i:i + k]
            if sub not in substrings:  # 只有新的子串才加入 t
                substrings[sub] = len(t)
                t.append(sub)

        lk = sum(len(t[i]) for i in range(len(t)))  # 计算最短 t 的长度
        result ^= (k * lk)  # 按照公式计算异或和

    return result

# 读取输入
n = int(input().strip())
s = input().strip()

# 输出结果
print(min_t_length(n, s))
