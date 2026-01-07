def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def check(arr, b):
        bi = 0
        for val in arr:
            if bi < len(b) and val >= b[bi]:
                bi += 1
        return bi == len(b)

    if check(a, b):
        print(0)
        return

    left = 1
    right = max(max(a), max(b))
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        
        possible = False
        for i in range(n + 1):
            temp_a = a[:]
            temp_a.insert(i, mid)
            if check(temp_a, b):
                possible = True
                break
        
        if possible:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()
