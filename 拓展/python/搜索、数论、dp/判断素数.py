import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):  # 2 和 3 是素数
        return True
    if n % 2 == 0 or n % 3 == 0:  # 排除能被 2 和 3 整除的数
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):  # 6 的倍数优化
        if n % i == 0 or n % (i + 2) == 0:  # 检查 6k ± 1
            return False
    return True

print(is_prime(5)) 
