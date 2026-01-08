'''
def bfs(start,target,get_nei):
    q=deque()
    vis={start:0}

    while q:
'''

from collections import deque

def bi_bfs(sta, end, get_nei):
    staq = deque([sta])
    endq = deque([end])

    vissta = {sta: 0}
    visend = {end: 0}

    while staq and endq:
        if len(staq) <= len(endq):
            for _ in range(len(staq)):
                cur = staq.popleft()
                curstp = vissta[cur]
                for nei in get_nei(cur):
                    if nei not in vissta:
                        vissta[nei] = curstp + 1
                        staq.append(nei)
                        if nei in visend:
                            return vissta[nei] + visend[nei]
        else:
            for _ in range(len(endq)):
                cur = endq.popleft()
                curstp = visend[cur]
                for nei in get_nei(cur):
                    if nei not in visend:
                        visend[nei] = curstp + 1
                        endq.append(nei)
                        if nei in vissta:
                            return vissta[nei] + visend[nei]
    return -1

def get_nei_puzzle(state):
    index = state.index('0')
    swap_pos = [
        [1,3],
        [0,2,4],
        [1,5],
        [0,4,6],
        [1,3,5,7],
        [2,4,8],
        [3,7],
        [4,6,8],
        [5,7]
    ]
    res = []
    for nei in swap_pos[index]:
        lst = list(state)
        lst[index], lst[nei] = lst[nei], lst[index]
        res.append("".join(lst))
    return res

def solve_puzzle(start, end):
    return bi_bfs(start, end, get_nei_puzzle)

# 示例调用
print(solve_puzzle("123405678", "123456780"))
# 输出：最少步数（如果可达）
