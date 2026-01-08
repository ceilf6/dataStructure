import heapq

N = int(input())
a = list(map(int, input().split()))
current_key = a.copy()
heap = [(-current_key[i], i) for i in range(N)]
heapq.heapify(heap)
d = [0] * N
f = [0] * N
base = 0
summ = 0

def get_max_remaining():
    while heap:
        key, i = heapq.heappop(heap)
        key = -key
        if key == current_key[i]:
            remaining = key - base
            if remaining > 0:
                heapq.heappush(heap, (-key, i))
                return True
            else:
                continue
    return False

while True:
    if not get_max_remaining():
        break
    summ += 1
    base += 1
    
    # 处理步骤d
    processed_d = False
    while heap:
        key_d, j = heapq.heappop(heap)
        key_d = -key_d
        if key_d != current_key[j]:
            continue
        remaining = key_d - base
        if remaining <= 0:
            heapq.heappush(heap, (-key_d, j))
            break
        new_key = key_d - 1
        current_key[j] = new_key
        d[j] += 1
        heapq.heappush(heap, (-new_key, j))
        processed_d = True
        break
    
    # 处理步骤f的第一个元素
    k = None
    while heap:
        key_f1, i = heapq.heappop(heap)
        key_f1 = -key_f1
        if key_f1 != current_key[i]:
            continue
        remaining = key_f1 - base
        if remaining <= 0:
            heapq.heappush(heap, (-key_f1, i))
            continue
        new_key = key_f1 - 1
        current_key[i] = new_key
        f[i] += 1
        heapq.heappush(heap, (-new_key, i))
        k = i
        break
    
    # 处理步骤f的第二个元素
    if k is not None:
        while heap:
            key_f2, i = heapq.heappop(heap)
            key_f2 = -key_f2
            if key_f2 != current_key[i]:
                continue
            remaining = key_f2 - base
            if remaining <= 0:
                heapq.heappush(heap, (-key_f2, i))
                continue
            new_key = key_f2 - 1
            current_key[i] = new_key
            f[i] += 1
            heapq.heappush(heap, (-new_key, i))
            break

print(summ)
