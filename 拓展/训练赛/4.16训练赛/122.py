k = int(input())
los = []
for i in range(k):
    los.append(list(map(int, input().split())))
w = int(input())

from collections import deque

tot = 2 ** (k + 1) - 1
t = [0] * tot
los = [deque(l) for l in los]

def dfs(x, lev):
    if lev == k:
        return True
    if not los[lev]:
        return False

    winner = t[x]
    loser = los[lev].popleft()
    l = x * 2 + 1
    r = x * 2 + 2

    for left_is_winner in [True, False]:
        if left_is_winner:
            t[l] = winner
            t[r] = loser
        else:
            t[l] = loser
            t[r] = winner

        # 检查胜者是否合理（必须是两者中的最大者）
        if max(t[l], t[r]) != winner:
            continue

        if dfs(l, lev + 1) and dfs(r, lev + 1):
            return True

    # 回溯
    t[l] = t[r] = 0
    los[lev].appendleft(loser)
    return False

t[0] = w
if dfs(0, 0):
    leaves = t[(2 ** k - 1):]
    print(' '.join(map(str, leaves)))
else:
    print('No Solution')
