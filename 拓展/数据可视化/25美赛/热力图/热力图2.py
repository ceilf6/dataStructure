import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 加载行政区划数据（GeoJSON文件）
mapp = gpd.read_file("world.zh.json")

# 加载保险和极端天气相关数据
data = pd.read_csv("全球保险渗透率_100国家.csv")  # 包括地区、投保率等

# 合并数据
merged_data = mapp.merge(data, how="left", left_on="name", right_on="国家")

# 绘制热力图
fig, ax = plt.subplots(1, 1, figsize=(12,20))
merged_data.plot(column='Insurance coverage rate', 
                 cmap='YlOrRd', 
                 legend=True, 
                 legend_kwds={'label': "Insurance coverage rate(%)",'orientation': "horizontal"},
                 edgecolor='black',
                 ax=ax)

plt.show()
