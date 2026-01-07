import matplotlib.pyplot as plt
import numpy as np

# 数据准备
labels = ['Soil', 'Diversity', 'Propagate & Sell', 'Government Subsidy','Pollution']  # 雷达图上的标签
values_y = [2, 2, 3, 3,3]  # 数据值
values_n=[3,4,4,5,4]
values_3=[4,3,2,4,3]
values_4=[3,4,2,3,2]
num_vars = len(labels)

# 计算角度
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 闭合雷达图
values_y += values_y[:1]
values_n+=values_n[:1]
values_3+=values_3[:1]
values_4+=values_4[:1]
angles += angles[:1]

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制第一个数据集
ax.fill(angles, values_y, color='#578B38', alpha=0.25, label='PingQuan')
ax.plot(angles, values_y, color='#578B38', linewidth=2)

# 绘制第二个数据集
ax.fill(angles, values_n, color='#074E91', alpha=0.25, label='FengNing')
ax.plot(angles, values_n, color='#074E91', linewidth=2)

# 绘制第二个数据集
ax.fill(angles, values_3, color='red', alpha=0.25, label='XingLong')
ax.plot(angles, values_3, color='red', linewidth=2)

# 绘制第二个数据集
ax.fill(angles, values_4, color='blue', alpha=0.25, label='LongHua')
ax.plot(angles, values_4, color='blue', linewidth=2)

# 添加标签
ax.set_yticks([1, 2, 3, 4, 5])  # 设置径向刻度
ax.set_yticklabels(['1', '2', '3', '4', '5'], color="gray")  # 设置径向标签
ax.set_xticks(angles[:-1])  # 设置角度刻度
ax.set_xticklabels(labels)

# 添加图例
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

#plt.title('Pagoda of Guanyin Temple', size=20, color='black', y=1.07)  # 设置标题
plt.show()
