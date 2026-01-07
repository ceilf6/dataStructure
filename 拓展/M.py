n, M, D = map(int, input().split())
total_days = M * D
occupied = [False] * (total_days + 1) #下标从1开始

def idx(month, day): #转为下标
    return (month - 1) * D + day

for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    start = idx(m1, d1)
    end = idx(m2, d2)
    for i in range(start, end + 1):
        occupied[i] = True

for i in range(1, total_days + 1):
    if not occupied[i]:
        month = (i - 1) // D + 1
        day = (i - 1) % D + 1
        print(month, day)
        break
else:
    print("Online")
