import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x) + 1  # 数据在正区间更直观

# 创建面积图
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='y = sin(x) + 1', color='blue')  # 折线
plt.fill_between(x, y, color='blue', alpha=0.3)       # 填充到x轴

# 添加图例和标签
plt.title("面积图示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.legend()
plt.grid(alpha=0.5)

# 显示图形
plt.show()
