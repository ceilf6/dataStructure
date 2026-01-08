from collections import deque
import math

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    queue = deque()
    queue.append([x, y])
    found = False
    while queue and not found:
        current = queue.popleft()
        #print(queue,current)
        length = len(current)
        for i in range(length):
            for j in range(i + 1, length):
                a = current[i]
                b = current[j]
                if (a & b) == 0 or (a ^ b) == 0:
                    print(length - 1)
                    found = True
                    break  # 退出内层循环
            if found:
                break  # 退出外层循环
        '''
        if found:
            continue  # 最外层的for循环   处理下一个测试用例
        '''
        # 生成新状态并加入队列
        for i in range(length):
            for j in range(i + 1, length):
                a = current[i]
                b = current[j]
                g = math.gcd(a, b)
                new_numbers = [a & b, a | b, a ^ b, g]
                for num in new_numbers:
                    new_vec = current.copy()
                    new_vec.append(num)
                    queue.append(new_vec)
