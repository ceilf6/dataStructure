def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n == 0:
            print(0)
            continue

        a = list(map(int, input().split()))
        full_mask_val = (1 << m) - 1
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = a[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] | a[i]
        suffix[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] | a[i]

        total_ans = 0
        for i in range(n):
            left_or = prefix[i - 1] if i - 1 >= 0 else 0
            right_or = suffix[i + 1] if i + 1 < n else 0
            T = left_or | right_or

            base = a[i] & (full_mask_val ^ T)
            part = a[i] & T

            if i > 0:
                left_val = a[i - 1]
                mask1 = part & (full_mask_val ^ left_val)
                U1 = part | left_val
            else:
                mask1 = 0
                U1 = full_mask_val

            if i < n - 1:
                right_val = a[i + 1]
                mask2 = part & (full_mask_val ^ right_val)
                U2 = part | right_val
            else:
                mask2 = 0
                U2 = full_mask_val

            mask = mask1 | mask2
            S = (U1 & U2) & T

            if mask & ~S:
                count_i = 0
            else:
                bits_S = bin(S).count('1')
                bits_mask = bin(mask).count('1')
                pop_free = bits_S - bits_mask
                count_i = (1 << pop_free) - 1

            total_ans += count_i

        print(total_ans)

if __name__ == "__main__":
    main()
