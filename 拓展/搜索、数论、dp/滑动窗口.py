from collections import deque

def maxSlidingWindow(nums: list, k: int) -> list:
    q = deque()  # 存储元素索引的双端队列
    result = []
    
    for right in range(len(nums)):
        # 清理队尾：移除所有小于当前值的元素
        while q and nums[right] >= nums[q[-1]]:
            q.pop()
        q.append(right)
        
        # 清理队首：移除超出窗口的左边界
        while q[0] <= right - k:
            q.popleft()
        
        # 当窗口形成后记录最大值
        if right >= k - 1:
            result.append(nums[q[0]])
    
    return result


nums=list(map(int,input().split()))
k=int(input())

print(maxSlidingWindow(nums,k))
