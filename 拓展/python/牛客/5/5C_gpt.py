n, x, y = map(int, input().split())
a = input().strip()
b = input().strip()
c = input().strip()

# 计算 a ⊕ c，得到需要修改的位
b2 = bin(int(a, 2) ^ int(c, 2))[2:].zfill(n)[-n:]

# 计算 b 和 b2 的差异
diff_pos = []  # 记录不同的位索引
for i in range(n):
    if b[i] != b2[i]:  # 需要修改
        diff_pos.append(i)

m = len(diff_pos)  # 需要修改的位总数
if m == 0:
    print(0)  # 已经满足 a ⊕ b = c

elif y >= 2 * x:
    # 只能用反转操作
    print(m * x)

else:
    # 尝试用交换 + 反转的混合操作
    swap_pairs = 0
    single_flip = 0
    i = 0
    while i < len(diff_pos) - 1:
        if diff_pos[i] + 1 == diff_pos[i + 1]:  # 找到相邻的不同位
            swap_pairs += 1
            i += 2  # 跳过下一个
        else:
            single_flip += 1
            i += 1
    # 处理可能遗漏的单独一位
    if i < len(diff_pos):
        single_flip += 1

    print(swap_pairs * y + single_flip * x)
