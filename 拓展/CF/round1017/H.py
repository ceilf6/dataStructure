import sys
input = sys.stdin.read

data = input().split()
idx = 0

t = int(data[idx])
idx += 1

results = []

for _ in range(t):
    n = int(data[idx])
    q = int(data[idx+1])
    idx += 2

    a = list(map(int, data[idx:idx+n]))
    idx += n

    for _ in range(q):
        k = int(data[idx])
        l = int(data[idx+1]) - 1
        r = int(data[idx+2]) - 1
        idx += 3

        ans = 0
        for i in range(l, r+1):
            while k % a[i] == 0:
                k //= a[i]
            ans += k
        results.append(str(ans))

print('\n'.join(results))
