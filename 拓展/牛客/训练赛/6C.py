
# 生成随机数
class RandomGenerator:
    def __init__(self, seed):
        self.seed = seed
    
    def rnd(self):
        self.seed ^= (self.seed << 13) & 0xFFFFFFFF
        self.seed ^= (self.seed >> 17) & 0xFFFFFFFF
        self.seed ^= (self.seed << 5) & 0xFFFFFFFF
        return self.seed & 0xFFFFFFFF  # 保持 unsigned int 范围

def solve():
    # 读取输入
    n, m, k, seed = map(int,input().split())

    # 初始化随机数生成器
    rng = RandomGenerator(seed)
    
    # 记录列的植物状态
    column = [0] * (m + 1)  # column[j] 记录第 j 列的最新植物编号
    removed = {}  # 记录被移除的植物 (a, b) -> True
    
    # 生成 k 次操作
    for _ in range(k):
        op = (rng.rnd() % 2) + 1
        if op == 1:
            i = (rng.rnd() % m) + 1  # 1 ≤ i ≤ m
            x = (rng.rnd() % (n * m)) + 1  # 1 ≤ x ≤ n*m
            column[i] = x  # 更新该列最新种植的植物
        else:
            a = (rng.rnd() % n) + 1  # 1 ≤ a ≤ n
            b = (rng.rnd() % m) + 1  # 1 ≤ b ≤ m
            removed[(a, b)] = True  # 记录被移除的点

    # 计算最终 XOR 值
    xor_result = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            index = (i - 1) * m + j  # 计算索引 (i-1)*m + j
            if (i, j) in removed:
                p_ij = 0  # 被移除则植物编号为 0
            else:
                p_ij = column[j]  # 否则取该列最后种植的值
            xor_result ^= (p_ij * index)

    print(xor_result)

solve()
