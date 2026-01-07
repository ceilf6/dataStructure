import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 示例数据
np.random.seed(42)
x = np.random.rand(6)  # X轴数据
y = np.random.rand(6)  # Y轴数据
z = np.random.rand(6)  # Z轴数据

# 创建图形
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维散点图
sc = ax.scatter(x, y, z, c=z, cmap='viridis', s=50, label='Data Points')

# 点与点之间连线
ax.plot(x, y, z, color='blue', linewidth=1, label='Connecting Line')

# 填充面
# 将点按照顺序连接，形成面
verts = [list(zip(x, y, z))]
poly = Poly3DCollection(verts, alpha=0.4, linewidths=1, edgecolor='blue', facecolor='cyan')
ax.add_collection3d(poly)

# 添加颜色条
cbar = fig.colorbar(sc, ax=ax, shrink=0.5, aspect=10, orientation='horizontal', pad=0.1)
cbar.set_label('Z Value')

# 设置轴标签
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# 设置视角
ax.view_init(elev=30, azim=-60)

# 图例和标题
plt.title("3D Scatter Plot with Connecting Lines and Colored Surface")
plt.legend()
plt.show()
