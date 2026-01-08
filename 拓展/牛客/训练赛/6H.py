'''
import math

def maxx(m):
    left, right = 1, int(math.sqrt(2 * m)) + 1
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 <= m:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1

N=int(input())

for i in range(N):
    m=int(input())
    print(maxx(m))
'''

import math

def max_mex(m):
    # 计算 k 的最大可能值
    k_max = int((3 * m) ** (1/3)) + 1
    # 找到最大的 k 满足 m >= k(k-1)(k+1)/3
    for k in range(k_max, 0, -1):
        if m >= k * (k - 1) * (k + 1) // 3:
            return k
    return 0

# 读取输入
T = int(input())
for _ in range(T):
    m = int(input())
    print(max_mex(m))
