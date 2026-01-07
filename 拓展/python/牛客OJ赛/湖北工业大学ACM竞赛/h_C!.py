def can_unify(n, m, k):
    total = n + m + k
    if n == total or m == total or k == total:
        return True
    if (n - m) % 3 == 0 or (n - k) % 3 == 0 or (m - k) % 3 == 0:
        return True
    return False

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print("YES" if can_unify(n, m, k) else "NO")
