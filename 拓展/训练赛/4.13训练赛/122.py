from itertools import permutations, combinations

n = int(input())
a = input().split()

res = list(permutations(a))
nums = [int(''.join(p)) for p in res]

total_sq_sum = sum([x**2 for x in nums])
half = len(nums) // 2

for comb in combinations(nums, half):
    if sum([x**2 for x in comb]) == total_sq_sum // 2:
        for x in comb:
            print(x)
        break
