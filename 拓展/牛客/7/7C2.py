import heapq

N = int(input())
a = list(map(int, input().split()))

# 构建最大堆（Python 的 heapq 是最小堆，所以存入负数）
heap = [-x for x in a if x > 0]  # 只存正数
heapq.heapify(heap)

summ = 0

while len(heap) > 0:
    summ += 1  # 计步

    # 遍历堆，所有元素减 1
    heap = [-(x-1) for x in heap if x < 0]
    
    # 重新构建堆
    heapq.heapify(heap)

    if len(heap) == 0:
        break  # 如果堆为空，跳出循环
    
    # 取出最大值
    max1 = -heapq.heappop(heap)

    if max1 - 1 > 0:
        heapq.heappush(heap, -(max1 - 1))

    if len(heap) == 0:
        break  # 如果堆为空，跳出循环

    max1 = -heapq.heappop(heap)

    if max1 - 1 > 0:
        heapq.heappush(heap, -(max1 - 1))
        
    # 取出次大值（如果有的话）
    max2 = -heapq.heappop(heap) if len(heap) > 0 else 0

    if max2 - 1 > 0:
        heapq.heappush(heap, -(max2 - 1))

print(summ)
