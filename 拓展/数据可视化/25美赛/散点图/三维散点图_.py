import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap


# 生成随机元组并存入数组
m= []
for _ in range(3):
    # 生成一个随机元组，这里假设元组包含两个整数
    tuple_data = (random.randint(1, 100), random.randint(1, 100))
    m.append(tuple_data)
    
# 生成随机元组并存入数组
z=[]
for _ in range(30):
    # 生成一个随机元组，这里假设元组包含两个整数
    tuple_data = (random.randint(1, 100), random.randint(1, 100))
    z.append(tuple_data)
    
'''
m = [(20, 30), (70, 80)]  # 对称后
z = [
    (10, 10), (10, 90), (90, 10), (90, 90), (50, 50), 
    (20, 20), (30, 70), (70, 30), (80, 80), (25, 25), 
    (75, 75), (15, 85), (85, 15), (40, 60), (60, 40),
    (50, 20), (20, 50), (50, 80), (80, 50)
]
'''

N=100

mapp=[[0]*100 for i in range(100)]

p=[[0]*100 for _ in range(100)]
for i in range(100):
    for  j in range(100):
        if i<50 and j<50:
            p[i][j]=0.1
        elif i>=50 and j>=50:
            p[i][j]=0.4
        elif i>=50 and j<50:
            p[i][j]=0.2
        else:
            p[i][j]=0.2

r=[[0]*100 for _ in range(100)]
for i in range(100):
    for j in range(100):
        if (i==40 or i==50) and (j==50 or j== 60 or j==70):
            r[i][j]=4
        else:
             r[i][j]=3.76



def D(point1,point2):
    x1,y1=point1#解包
    x2,y2=point2
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return d
    
def Dinfructure(point):
    s=0
    for i in range(len(z)):
        s+=D(point,z[i])
    return s/4

def Dhazurd(point):
    s=0
    for i in range(len(m)):
        s+=D(point,m[i])
    return s/len(m)

def Y(point):
    x,y=point
    pp=p[x][y]
    rr=r[x][y]
    s=-0.4*Dinfructure(point)+0.3*Dhazurd(point)-0.2*pp+0.1*rr
    return s

maxk=-float('inf')
maxx=-float('inf')
maxy=-float('inf')
for i in range(100):
    for j in range(100):
        k=Y((i,j))
        mapp[i][j]=round(k,2)+110
        if k>maxk and (i,j) not in z:
            maxk=k
            maxx=i
            maxy=j
'''
output='\n'.join(' '.join(map(str,row))for row in mapp)
print(output)
print("except the stations,schools...")
print("the x of max is %d"%(maxx))
print()
print("the y of max is %d"%(maxy))
'''
mapp = np.array(mapp)


'''
# 定义自定义颜色映射
colors = ["#BE5C37", "#F7F7E9"]  # 橙色到黄色
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
'''

colors=[
        '#313695',
        '#4575b4',
        '#74add1',
        '#abd9e9',
        '#e0f3f8',
        '#ffffbf',
        '#fee090',
        '#fdae61',
        '#f46d43',
        '#d73027',
        '#a50026'
      ]
# 定义离散颜色列表
#colors = ["#BE5C37", "#D78851", "#D88F92"]  # 亮黄色、黄色和橙色
custom_cmap = ListedColormap(colors)


# 创建热力图
plt.figure(figsize=(8, 6))
plt.imshow(mapp, cmap=custom_cmap, interpolation='nearest')  # 使用自定义映射



# 添加颜色条
plt.colorbar()


# 添加基础设施位置，用红色点标记
infrastructure_x, infrastructure_y = zip(*z)
plt.scatter(infrastructure_y, infrastructure_x, color='#8AB09E', label='Infrastructure', edgecolors='black', s=100)

# 添加极端天气位置，用蓝色点标记
extreme_weather_x, extreme_weather_y = zip(*m)
plt.scatter(extreme_weather_y, extreme_weather_x, color='#FCA556', label='Extreme Weather', edgecolors='black', s=100)



# 反转 y 轴，使原点 (0, 0) 出现在左上角
plt.gca().invert_yaxis()


# 设置轴标签和标题
plt.title("Livability analysis of complex map in 2D")
plt.xlabel("Y")
plt.ylabel("X")

# 显示网格
plt.xticks(range(0,101,10))
plt.yticks(range(0,101,10))
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)

# 显示图像
plt.show()


mapp = np.array(mapp)

# 曲面图展示
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
x,y= np.meshgrid(range(100), range(100))
#从1开始



# 绘制曲面
surf = ax.plot_surface(x, y, mapp, cmap=custom_cmap)  # 使用自定义映射


# 添加颜色条并设置为水平
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.1)

# 设置颜色条标签
cbar.set_label('habitability')

# 设置轴标签
ax.set_xlabel("X")
ax.set_ylabel("Y")
#ax.set_zlabel("habitability")


# 设置坐标范围，使 (0, 0) 显示在靠近的位置
ax.set_xlim(0,100)
ax.set_ylim(0,100)

# 设置视角（可调整以获得更好的效果）
ax.view_init(elev=30, azim=-120)  # elev 是仰角，azim 是方位角


plt.title("Livability analysis of complex map in 3D")
plt.show()


