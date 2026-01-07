def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0和1不是素数
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # 从i²开始，步长为i，标记所有i的倍数
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
