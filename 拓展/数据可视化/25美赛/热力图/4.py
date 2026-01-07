import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap,ListedColormap
from matplotlib.patches import Rectangle

# 加载示例地图数据和统计数据
china_map = gpd.read_file("world.zh.json")
data = pd.read_csv("全球保险渗透率_100国家.csv")

# 合并数据
merged_data = china_map.merge(data, how="left", left_on="name", right_on="国家")

# 自定义颜色映射（渐变）
custom_cmap = LinearSegmentedColormap.from_list(
    "CustomCmap",
    ["#FBF9FA", "#507AAF"]  # 黄色到蓝色的渐变
)
'''
# 自定义离散颜色映射
custom_cmap = ListedColormap(["#FBF9FA", "#DEDCEA", "#AFB7DB","#8197C6","#507AAF"])
'''
# 绘制热力图
fig, ax = plt.subplots(1, 1, figsize=(10,7))  # 缩短宽度
merged_data.plot(
    column='Insurance coverage rate',
    cmap=custom_cmap,
    #cmap='YlOrRd',
    #cmap=custom_cmap,  # 使用自定义的颜色映射
    legend=False,#不使用默认的比例尺

    legend_kwds={
        'label': "Insurance coverage rate(%)",
        'orientation': "horizontal",  # 设置比例尺为水平
        'pad': 0.005,  # 调整比例尺与图形之间的间距
    },

    missing_kwds={
        'color': 'none',  # 设置无数据区域的背景为透明
        'hatch': '///',   # 无数据区域使用斜黑线填充
        'label': 'No Data'  # 在图例中添加说明
    },
    edgecolor='black',
    ax=ax
)

# 去掉地图的经纬度尺度
ax.axis('off')

# 获取 colorbar 对象并调整其位置
cbar = fig.colorbar(ax.collections[0], ax=ax, orientation='horizontal')  # 获取colorbar对象
cbar.ax.set_position([0.25, 0.05, 0.5, 0.03])  # 设置colorbar的位置


# 获取 colorbar 的 Axes 对象，调整比例尺数字和标签
cbar.ax.xaxis.set_ticks_position('top')  # 设置刻度到上方
cbar.ax.xaxis.set_label_position('top')  # 设置标签到上方
cbar.ax.set_xlabel("Insurance coverage rate(%)", labelpad=10)  # 设置标签，并调整与比例尺的间距


# 添加无数据方块到比例尺左边
no_data_rect = Rectangle((0.1, 0.05), 0.05, 0.03, transform=fig.transFigure, facecolor='none', edgecolor='black', hatch='///')
fig.patches.append(no_data_rect)

# 添加 "No Data" 标注文字到比例尺上方
ax.text(0.125, 0.1, "No Data", transform=fig.transFigure, fontsize=10, verticalalignment='center', horizontalalignment='center')

plt.show()
