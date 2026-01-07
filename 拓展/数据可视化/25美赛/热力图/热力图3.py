import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from matplotlib.patches import Rectangle

# 加载示例地图数据和统计数据
china_map = gpd.read_file("world.zh.json")
data = pd.read_csv("全球保险渗透率_100国家.csv")

# 合并数据
merged_data = china_map.merge(data, how="left", left_on="name", right_on="国家")

# 自定义颜色映射：左黄右蓝
custom_cmap = LinearSegmentedColormap.from_list("YellowBlue", ["yellow", "blue"])

# 绘制热力图
fig, ax = plt.subplots(1, 1, figsize=(8, 12))  # 缩短宽度
merged_data.plot(
    column='Insurance coverage rate',
    cmap=custom_cmap,  # 使用自定义的颜色映射
    legend=True,
    legend_kwds={
        'label': "Insurance coverage rate(%)",
        'orientation': "horizontal",  # 设置比例尺为水平
        #'labelposition': 'top',       # 标签位置调整到比例尺上方
        #'pad': 2                      # 调整标签与比例尺之间的间距
    },
    missing_kwds={
        'color': 'none',  # 设置无数据区域的背景为透明
        'hatch': '///',   # 无数据区域使用斜黑线填充
        'label': 'No Data'  # 在图例中添加说明
    },
    edgecolor='black',
    ax=ax
)


# 调整比例尺位置
cbar = ax.get_figure().get_axes()[1]
cbar.set_position([0.25, 0.05, 0.5, 0.03])  # [x, y, width, height]


# 手动调整比例尺数字标签到上方
cbar.xaxis.set_ticks_position('top')  # 设置刻度到上方
cbar.xaxis.set_label_position('top')  # 设置标签到上方
cbar.set_label("保险覆盖率 (%)", labelpad=10)  # 增加标签的间距


# 添加无数据方块到比例尺左边
no_data_rect = Rectangle((0.1, 0.05), 0.05, 0.03, transform=fig.transFigure, facecolor='none', edgecolor='black', hatch='///')
fig.patches.append(no_data_rect)

# 添加 "No Data" 标注文字
ax.text(0.07, 0.065, "No Data", transform=fig.transFigure, fontsize=10, verticalalignment='center')


'''
# 调整比例尺位置
cbar = ax.get_figure().get_axes()[1]
cbar.set_position([0.2, 0.05, 0.6, 0.03])  # [x, y, width, height]
'''
#plt.title("极端天气下保险覆盖率热力图", fontsize=15)
plt.show()
