import math

def sie(L, R):
    if L > R: return []
    # 生成基础素数
    limit = math.isqrt(R)
    sieve = [True] * (limit+1)
    sieve[0:2] = [False]*2
    for i in range(2, math.isqrt(limit)+1):
        if sieve[i]: sieve[i*i::i] = [False]*len(sieve[i*i::i])
    primes = [i for i, f in enumerate(sieve) if f]
    
    # 初始化区间筛
    isp = [True]*(R-L+1)
    for x in (0,1):  # 处理0和1
        if L <= x <= R: isp[x-L] = False
    
    # 标记合数
    for p in primes:
        start = max(p*p, (L+p-1)//p*p)  # 起始位置取较大值
        for m in range(start, R+1, p): isp[m-L] = False
    
    return [i+L for i, p in enumerate(isp) if p]

print(sie(1,100))
