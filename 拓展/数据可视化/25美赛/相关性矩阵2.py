import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 直接输入相关性矩阵
corr_matrix = np.array([
    [1, 5/7, 5/3, 1, 5, 5/3, 5, 5/3],
    [7/5, 1, 7/3, 7/5, 7, 7/3, 7, 7/3],
    [3/5, 3/7, 1, 3/5, 3, 1, 3, 1],
    [1, 5/7, 5/3, 1, 5, 5/3, 5, 5/3],
    [1/5, 1/7, 3, 1/5, 1, 1/3, 1, 1/3],
    [3/5, 3/7, 1, 3/5, 3, 1, 3, 1],
    [1/5, 1/7, 1/3, 1/5, 1, 1/3, 1, 1/3],
    [3/5, 3/7, 1, 3/5, 3, 1, 3, 1]
])

# 转换为 DataFrame，提供正确的行列名
corr_matrix = pd.DataFrame(
    corr_matrix,
    columns=['1','2','3','4','5','6','7','8'],  # 8 个变量列名
    index=['1 - PH','2 - Organic Substance','3 - Water Pollution','4 - Chemical Residues','5 - Biological Tiers','6 - Diversity','7 - Cost','8 - Revenue']    # 8 个变量行名
)

# 创建掩码矩阵
mask_upper = np.triu(np.ones_like(corr_matrix, dtype=bool), k=0)  # 上三角掩码（包括对角线）
mask_lower = ~mask_upper  # 下三角排掩码（不包括对角线）

# 设置左下角绿色背景矩阵
left_lower_colors = corr_matrix.applymap(
    lambda x: "#FDD57F" if x >= 3 or x <= 1/3 else "white"
)

# 设置绘图风格
plt.figure(figsize=(10, 8))
sns.set_theme(style="white")

# 自定义配色：红色到蓝色的渐变
custom_cmap = LinearSegmentedColormap.from_list(
    "red_blue", ["red", "white", "#8596C4"], N=100  # 红色到蓝色渐变，设置更多的渐变色
)

# 绘制右上三角（颜色渐变，带标记）
sns.heatmap(
    corr_matrix,
    mask=mask_lower,  # 掩盖左下部分
    cmap=custom_cmap,  # 使用自定义颜色
    annot=False,  # 不显示原始数据值
    vmin=0, vmax=7,  # 设置颜色范围
    cbar_kws={"shrink": 0.8},  # 调整颜色条大小
    linewidths=0.5,  # 方块分割线宽度
    linecolor="black",  # 分割线颜色为黑色
    square=True,  # 方形格子
    cbar=True  # 显示颜色条
)

# 绘制左下三角（填充背景色，显示数值，并保留分隔线）
for i in range(corr_matrix.shape[0]):
    for j in range(i):  # 左下三角
        plt.gca().add_patch(
            plt.Rectangle((j, i), 1, 1, facecolor=left_lower_colors.iloc[i, j], edgecolor="black", linewidth=0.5)
        )
        plt.text(
            j + 0.5,  # X 坐标
            i + 0.5,  # Y 坐标
            f"{corr_matrix.iloc[i, j]:.2f}",  # 显示数值（两位小数）
            ha="center", va="center",  # 水平和垂直居中
            color="black",  # 数值字体颜色
            fontsize=14,  # 数值字体大小
        )

# 绘制右上三角的圆圈符号（满足条件时显示）
for i in range(corr_matrix.shape[0]):
    for j in range(i + 1, corr_matrix.shape[1]):  # 右上三角
        if corr_matrix.iloc[i, j] >= 3 or corr_matrix.iloc[i, j] <= 1/3:  # 满足条件
            plt.text(
                j + 0.5,  # X 坐标
                i + 0.5,  # Y 坐标
                "o",  # 使用圆圈符号
                ha="center", va="center",  # 水平和垂直居中
                color="#9D0109",  # 圆圈符号颜色
                fontsize=18,  # 符号字体大小
                fontweight="bold"  # 加粗字体
            )

# 添加标题
plt.title("Spearman Matrix Heatmap", fontsize=16)
plt.show()
