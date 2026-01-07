import heapq

def min_cost_to_merge_fruits(n, fruits):
    # 将所有果子堆初始化为最小堆
    heapq.heapify(fruits)
    
    total_cost = 0
    
    # 不断合并直到只剩下一堆
    while len(fruits) > 1:
        # 取出最小的两堆
        first = heapq.heappop(fruits)
        second = heapq.heappop(fruits)
        
        # 合并后的体力消耗
        cost = first + second
        total_cost += cost
        
        # 将新堆放回堆中
        heapq.heappush(fruits, cost)
    
    return total_cost

# 输入
n = int(input())
fruits = list(map(int, input().split()))

# 输出最小体力耗费值
print(min_cost_to_merge_fruits(n, fruits))
