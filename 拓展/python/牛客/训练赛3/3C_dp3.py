n, k = map(int, input().split())
a = list(map(int, input().split()))
L = n - k  # 剩下的数组长度

# 预处理前缀和和后缀和
left = [0] * (n + 1)  # left[i]表示前i个元素的和
right = [0] * (n + 1)  # right[j]表示后j个元素的和

for i in range(1, n+1):
    left[i] = left[i-1] + a[i-1]

for j in range(1, n+1):
    right[j] = right[j-1] + a[n - j]

total = left[n]
max_sum = 0

for i in range(0, k+1):
    j = k - i
    if j < 0 or j > n:
        continue
    current_sum = total - left[i] - right[j]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
