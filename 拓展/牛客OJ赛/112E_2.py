import sys
from sys import stdin
from functools import lru_cache

def main():
    n, m = map(int, stdin.readline().split())
    k = list(map(int, stdin.readline().split()))
    M = [int(stdin.readline()) for _ in range(m)]

    # Precompute all possible subset sums and their masks
    subset_sums = {}
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if mask & (1 << i):
                s += k[i]
        if s not in subset_sums:
            subset_sums[s] = []
        subset_sums[s].append(mask)

    for mi in M:
        found = False
        # Handle mi = 0 case
        if mi == 0:
            # Check if there exists a non-empty subset sum 0 or any subset sum 0 and others
            if 0 in subset_sums and len(subset_sums[0]) > 0:
                print("Yes")
                mask = subset_sums[0][0]
                A = [k[i] for i in range(n) if mask & (1 << i)]
                B = []
                for i in range(n):
                    if not (mask & (1 << i)):
                        B.append(k[i])
                        if B:
                            break
                if not B:
                    B = [k[i] for i in range(n) if not (mask & (1 << i))][:1]
                print(len(A), len(B))
                print(' '.join(map(str, A)))
                print(' '.join(map(str, B)))
                continue
            else:
                # Check if there exists two subsets where one is empty (but product is 0)
                # This part can be enhanced
                print("No")
                continue

        # Enumerate factors
        factors = set()
        for a in subset_sums:
            if a == 0:
                continue
            if mi % a == 0:
                b = mi // a
                factors.add((a, b))
                factors.add((b, a))

        # Check for factors
        for a, b in factors:
            if a in subset_sums and b in subset_sums:
                for mask_a in subset_sums[a]:
                    for mask_b in subset_sums[b]:
                        if (mask_a & mask_b) == 0 and mask_a != 0 and mask_b != 0:
                            # Found valid masks
                            A = [k[i] for i in range(n) if mask_a & (1 << i)]
                            B = [k[i] for i in range(n) if mask_b & (1 << i)]
                            print("Yes")
                            print(len(A), len(B))
                            print(' '.join(map(str, A)))
                            print(' '.join(map(str, B)))
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
        if found:
            continue
        print("No")

if __name__ == "__main__":
    main()
