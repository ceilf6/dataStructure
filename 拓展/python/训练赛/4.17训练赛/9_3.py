from collections import deque

hezi = []  # 小盒子，栈
ans = []   # 最终成品松枝列表
now = []   # 当前正在制作的松枝
j = 0      # 当前推送器的位置

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

def process_hezi():
    global now, hezi, ans
    while hezi and (len(now) == 0 or hezi[-1] <= now[-1]) and len(now) < k:
        now.append(hezi.pop())

def cz():
    global j, now, hezi, ans
    # 处理盒子中的松针
    process_hezi()
    if len(now) == k:
        ans.append(now)
        now = []
        return

    # 处理推送器中的松针
    while j < n:
        current = a[j]
        if not now:
            now.append(current)
            j += 1
            process_hezi()
            if len(now) == k:
                ans.append(now)
                now = []
                return
            continue
        # 当前松针是否满足条件
        if current <= now[-1]:
            now.append(current)
            j += 1
            process_hezi()
            if len(now) == k:
                ans.append(now)
                now = []
                return
        else:
            # 推入盒子
            if len(hezi) < m:
                hezi.append(current)
                j += 1
            else:
                # 盒子已满，无法处理，结束当前松枝
                ans.append(now)
                now = []
                return  # 当前current没有被处理，需要压回推送器，即j不递增
            # 处理盒子中的松针
            process_hezi()
            if len(now) == k:
                ans.append(now)
                now = []
                return

    # 推送器处理完后，再次处理盒子中的松针
    process_hezi()
    if len(now) > 0:
        ans.append(now)
        now = []

while j < n or now:
    cz()

# 如果还有未放入成品篮的松枝
if now:
    ans.append(now)

# 输出所有成品
for branch in ans:
    print(' '.join(map(str, branch)))
