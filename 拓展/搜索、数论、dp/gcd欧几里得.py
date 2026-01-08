from math import *

def gcd(a, b):
    if b == 0:
        print("%d %d"%(a,b))
        return a, 1, 0  # gcd, x, y
    gcd2, x1, y1 = gcd(b, a % b)
    x = y1
    y = x1 -floor( a / b) * y1
    print("%d %d %d"%(gcd2,x,y))
    return gcd2, x, y

def mod_inverse(a, p):
    """
    求 a 在模 p 下的模逆元
    """
    gcd2, x, _ = gcd(a, p)
    if gcd2 != 1:
        raise ValueError("模逆元不存在，因为 gcd(a, p) ≠ 1")
    return x % p  # 确保模逆元是正数

a=300
b=7
gcd(a,b)

a = 3
p = 7
mod_inv = mod_inverse(a, p)
print(f"The modular inverse of {a} modulo {p} is {mod_inv}")
