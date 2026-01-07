import heapq

class DualHeap:
    def __init__(self):
        self.max_heap = []  # 大顶堆（用负数模拟）
        self.min_heap = []  # 小顶堆

    def add(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)        
        '''
        1. 如果新元素 ≤ 大顶堆的堆顶（即最大值），放进大顶堆。
        2. 否则放进小顶堆。
        3. 然后再检查是否平衡，不平衡就搬堆顶元素过去。
        # 根据长度比较，保持两个堆的平衡，有点类似于双向bfs
        '''
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0] #其实这里一定是第一个分支
                                     #因为本题输出时个数为奇，一定是大顶堆多一个
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

n=int(input())
l=list(map(int,input().split()))

hq=DualHeap()
for i in range(n):
    hq.add(l[i])
    if (i+1)%2==1:
        print(hq.get_median())
