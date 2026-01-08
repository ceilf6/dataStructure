import sys
import threading
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    k = int(input())
    los = [deque(map(int, input().split())) for _ in range(k)]
    w = int(input())

    total_nodes = 2 ** (k + 1) - 1
    tree = [0] * total_nodes  # 二叉树结构，记录每个节点的胜者能力值

    def build(node_idx, level):
        if level == k:
            return True

        if not los[level]:
            return False

        loser = los[level].popleft()
        winner = tree[node_idx]

        l, r = node_idx * 2 + 1, node_idx * 2 + 2

        # 两种分配方式：胜者在左或在右
        for left_win in [True, False]:
            tree[l] = winner if left_win else loser
            tree[r] = loser if left_win else winner

            # 合理性判断
            if max(tree[l], tree[r]) != winner:
                continue

            if build(l, level + 1) and build(r, level + 1):
                return True

        # 回溯
        tree[l] = tree[r] = 0
        los[level].appendleft(loser)
        return False

    tree[0] = w
    if build(0, 0):
        leaves = tree[(2 ** k - 1):]
        print(' '.join(map(str, leaves)))
    else:
        print('No Solution')

threading.Thread(target=main).start()
