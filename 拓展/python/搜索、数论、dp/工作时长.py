import datetime

time = []

while True:
    try:
        s = input()

        dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")  # 修复参数缺失问题

        t = dt.timestamp()
        time.append(t)
    except:
        break
time.sort()
print(time)
ans = 0
# 循环步长应为每两个元素计算一次差值
for i in range(len(time) // 2):
    # 计算每对时间差（第0和1，2和3，依此类推）
    ans += time[2*i + 1] - time[2*i]

print(int(ans))  # 输出总时间差（秒数）
