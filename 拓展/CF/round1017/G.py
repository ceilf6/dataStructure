from collections import deque

t = int(input())
for _ in range(t):
    q = int(input())
    arr = deque()
    rizz = 0
    rev = False  # 是否逻辑反转

    for _ in range(q):
        s = input().split()
        op = int(s[0])

        if op == 1:
            if arr:
                if not rev:
                    x = arr.pop()
                    arr.appendleft(x)
                    rizz += x * 1 - x * len(arr)
                else:
                    x = arr.popleft()
                    arr.append(x)
                    rizz += x * len(arr) - x * 1

        elif op == 2:
            rev = not rev
            n = len(arr)
            rizz = sum(arr[i] * (n - i) for i in range(n)) if rev else sum(arr[i] * (i + 1) for i in range(n))

        elif op == 3:
            k = int(s[1])
            if not rev:
                arr.append(k)
                rizz += k * len(arr)
            else:
                arr.appendleft(k)
                rizz += k * 1

        print(rizz)
