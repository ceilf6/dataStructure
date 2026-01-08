n = int(input())
s = input().strip()

# 预处理前缀和数组
prefix_zero = [0] * (n + 1)
prefix_one = [0] * (n + 1)
for i in range(n):
    prefix_zero[i+1] = prefix_zero[i] + (s[i] == '0')
    prefix_one[i+1] = prefix_one[i] + (s[i] == '1')

ans_xor = 0

for k in range(1, n + 1):
    m = (n + k - 1) // k  # 段的数量
    y = 0
    for i in range(m):
        start = i * k
        end = min((i + 1) * k, n)
        cnt0 = prefix_zero[end] - prefix_zero[start]
        cnt1 = prefix_one[end] - prefix_one[start]
        if cnt0 > 0 and cnt1 > 0:
            y += 1
    ans_k = 1 + y
    ans_xor ^= ans_k

print(ans_xor)
