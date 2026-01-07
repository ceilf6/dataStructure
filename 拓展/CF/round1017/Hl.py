import sys
import math

# 预处理所有数的质因数
MAX_A = 100000
spf = list(range(MAX_A + 1))  # spf[x] 存储 x 的最小质因数

def sieve():
    for i in range(2, int(math.sqrt(MAX_A)) + 1):
        if spf[i] == i: 
            for j in range(i * i, MAX_A + 1, i):
                if spf[j] == j:
                    spf[j] = i

# 求解 x 的质因数
def prime_factors(x):
    factors = []
    while x != 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors


def process_queries(t, queries):
    results = []
    for test_case in queries:
        n, q, a, query_list = test_case
        for k, l, r in query_list:
            ans = 0
            for i in range(l - 1, r):
                current_k = k
                factors = prime_factors(a[i])
                for factor in factors:
                    while current_k % factor == 0:
                        current_k //= factor
                ans += current_k
            results.append(str(ans))
    return results


def main():
    sieve()  # 先预处理质因数
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    queries = []
    
    for _ in range(t):
        n, q = map(int, data[idx].split())
        idx += 1
        a = list(map(int, data[idx].split()))
        idx += 1
        query_list = []
        for __ in range(q):
            k, l, r = map(int, data[idx].split())
            query_list.append((k, l, r))
            idx += 1
        queries.append((n, q, a, query_list))
    
    results = process_queries(t, queries)
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
