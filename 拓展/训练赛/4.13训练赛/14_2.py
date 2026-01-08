n = int(input())
a = list(map(int, input().split()))

def cnt(b):
    count =0
    for i in range(n):
        for j in range(i + 1, n):
            if b[i] > b[j]:
                count += 1
    return count

ans = []
for i in range(n):
    for j in range(i, n):
        b = a[:i] + list(reversed(a[i:j+1])) + a[j+1:]
        ans.append(cnt(b))

print(' '.join(map(str, ans)))
