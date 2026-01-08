import math

n = int(input())

if n == 1:
    print(0)
else:
    def fm(n):
        if n % 2 == 0:
            return 2
        max_d = int(math.sqrt(n))
        for i in range(3, max_d + 1, 2):
            if n % i == 0:
                return i
        return n

    d_min = fm(n)
    sum_factors = d_min

    sum_non_factors = float('inf')
    max_d = int(math.sqrt(n))
    for d in range(2, max_d + 1):
        r = n % d
        current_sum = d + r
        if current_sum < sum_non_factors:
            sum_non_factors = current_sum

    sum_candidate = min(sum_factors, sum_non_factors) if sum_non_factors != float('inf') else sum_factors

    candidate_step = 2 * sum_candidate - 2
    direct_step = 2 * n - 2
    answer = min(candidate_step, direct_step)
    print(answer)
