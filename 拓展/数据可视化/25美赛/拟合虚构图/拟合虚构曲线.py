import numpy as np
import matplotlib.pyplot as plt

# 定义 x 轴范围
x = np.linspace(-7, 50, 500)

# 分段点
x0, x1, x2, x3 = -1, 3, 7, 12

def curve0(x):
    return 3.25 + 4 * np.log(-x)

# 定义每段曲线
def curve1(x):
    y_start = curve0(x0)
    y_end = -0.2
    # 第一段：下凹地增加
    return -2 * (1 - np.exp(-x))

def curve2(x):
    # 第二段：下凸地减小
    y_start = curve1(x1)
    y_end = -0.4
    return y_start - (y_start - y_end) * ((x - x1) / (x2 - x1))**2

def curve3(x):
    # 第三段：下凸地增加
    y_start = curve2(x2)
    y_end = -0.6
    return -8.2 + 4 * np.log(x)

def curve4(x):
    return 5.9 - 50 / x

# 拼接曲线
y = np.piecewise(
    x,
    [x < x0, (x >= x0) & (x < x1), (x >= x1) & (x < x2), (x > x2) & (x <= x3), x > x3],
    [curve0, curve1, curve2, curve3, curve4]
)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='kkk', color='#578B38',linewidth=5)

# 去除x轴的数字
plt.xticks([])
plt.yticks([])

# 去除网格线
plt.grid(False)
# 去除边框
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去除顶部边框
ax.spines['right'].set_visible(False)  # 去除右侧边框
ax.spines['left'].set_visible(False)  # 去除左侧边框
ax.spines['bottom'].set_visible(False)  # 去除底部边框
'''
# 设置边框（保留边框）
ax = plt.gca()
ax.spines['bottom'].set_linewidth(1)  # 设置x轴轴线宽度
ax.spines['left'].set_linewidth(1)  # 设置y轴轴线宽度
'''
'''
# 自定义y轴刻度
plt.yticks([300, 500, 700, 900])  # 自定义y轴刻度值
'''
'''
# 设置背景颜色
ax.axvspan(-7, x0, color='#C4D6A0', alpha=0.3)
ax.axvspan(x0, x2, color='#F6F8EB', alpha=0.3)  # 在 x0 到 x1 范围内填充黄色背景，透明度为 0.3
ax.axvspan(x2, 25, color='#FFFF9E', alpha=0.5)  # 在 x2 到 x3 范围内填充浅蓝色背景，透明度为 0.5
#ax.axvspan(x1, x2, color='lightgreen', alpha=0.3)  # 在 x0 到 x1 范围内填充黄色背景，透明度为 0.3
ax.axvspan(25, 50, color='#D5BE98', alpha=0.5)  # 在 x2 到 x3 范围内填充浅蓝色背景，透明度为 0.5
'''
# 使用 fill_between 填充不同区间
plt.fill_between(x[x < x0], y[x < x0], -5, color='#FFFF9E', alpha=0.3, label='Region 1')
plt.fill_between(x[(x >= x0) & (x < x2)], y[(x >= x0) & (x < x2)], -5, color='#C7EC99', alpha=0.3, label='Region 2')
plt.fill_between(x[(x >= x2) & (x <= 25)], y[(x >= x2) & (x <= 25)], -5, color='#8ED694', alpha=0.5, label='Region 3')
plt.fill_between(x[x > 25], y[x > 25], -5, color='#36B88E', alpha=0.5, label='Region 4')

# 去除左右两边的留白
plt.xlim(np.min(x), np.max(x))

# 显示图形
plt.show()
