from collections import deque

hezi = []  # 小盒子，栈
ans = []   # 最终成品松枝列表
now = []   # 当前正在制作的松枝
j = 0      # 当前推送器的位置

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

def cz():
    global j, now, hezi, ans
    while j < n:
        # 如果当前松枝是空的，先尝试从盒子取，否则从推送器取
        if not now:
            if hezi:
                now.append(hezi.pop())
            else:
                now.append(a[j])
                j += 1
            continue

        # 优先使用盒子中合适的
        while hezi and hezi[-1] <= now[-1] and len(now) < k:
            now.append(hezi.pop())

        # 判断当前松枝是否完成
        if len(now) == k:
            ans.append(now)
            now = []
            continue

        # 如果推送器还有
        if j < n:
            if a[j] <= now[-1]:
                now.append(a[j])
            else:
                hezi.append(a[j])
                if len(hezi) == m:
                    # 小盒子已满，当前松枝无法继续，放入成品
                    ans.append(now)
                    now = []
            j += 1
        else:
            # 推送器无针了，只能用盒子，不行就结束
            if not hezi or hezi[-1] > now[-1]:
                ans.append(now)
                now = []
            # 否则继续循环上面 hezi while 使用盒子部分

while j < n or now:
    cz()

# 如果还有未放入成品篮的松枝
if now:
    ans.append(now)

# 输出所有成品
for branch in ans:
    print(*branch)
