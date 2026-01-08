import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

k = int(input())
losers = [deque(map(int, input().split())) for _ in range(k)]
w = int(input())

n = 2 ** k
tree = [0] * (2 * n - 1)  # 完全二叉树表示比赛树

def build(node, level, winner):
    if level == k:
        tree[node] = winner
        return True
    if not losers[level]:
        return False
    lose = losers[level].popleft()

    # 当前比赛胜者是 winner，败者是 lose
    # 两种组合方式：winner 左边 or winner 右边
    for win_left in [True, False]:
        l = 2 * node + 1
        r = 2 * node + 2
        if win_left:
            lw, rw = winner, lose
        else:
            lw, rw = lose, winner

        if lw < rw:  # 胜者不能比败者弱
            continue
        tree[node] = winner
        if build(l, level + 1, lw) and build(r, level + 1, rw):
            return True

    losers[level].appendleft(lose)
    return False

if build(0, 0, w):
    print(' '.join(map(str, tree[n - 1:])))
else:
    print('No Solution')
