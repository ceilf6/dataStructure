from collections import deque
'''
queue=deque(1)

s=(3,7,17,29,53)

flag=1
while flag:
    current=queue.popleft()

'''

from queue import PriorityQueue

def nth_ugly_number(primes, n):
    pq = PriorityQueue()
    pq.put(1)
    visited = set()
    visited.add(1)

    count = 0
    while not pq.empty():
        cur = pq.get()
        count += 1
        if count == n:
            return cur
        for p in primes:
            next_val = cur * p
            if next_val not in visited:
                visited.add(next_val)
                pq.put(next_val)

# 示例：S = {3,7,17,29,53}，求第20220个丑数
S = [3, 7, 17, 29, 53]
n = 20220
result = nth_ugly_number(S, n)
print(result)
