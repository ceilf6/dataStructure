import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


mapp=[[0]*100 for i in range(100)]
'''
print("请输入极端天气概率")
p=float(input())
print("请输入利润率")
r=float(input())
'''
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


z = [(10, 10), (30, 40), (50, 50), (70, 30), (90, 90)]  # 基础设置位置
m = [(20, 20), (40, 60), (60, 40), (80, 80), (10, 90)]  # 极端天气位置

'''
print("请输入公共措施位置，x、y中间用空格区分,输入'E'结束")
z=[]
k=input()
while k!='E':
    x,y=map(int,k.split())
    z.append((x,y))
    k=input()

print("请输入极端天气坐标，x、y中间用空格区分,输入'E'结束")
m=[]
k=input()
while k!='E':
    x,y=map(int,k.split())
    m.append((x,y))
    k=input()
'''    

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
        mapp[i][j]=round(k,2)
        if k>maxk and (i,j) not in z:
            maxk=k
            maxx=i
            maxy=j

output='\n'.join(' '.join(map(str,row))for row in mapp)
print(output)
print("except the stations,schools...")
print("the x of max is %d"%(maxx))
print()
print("the y of max is %d"%(maxy))


mapp = np.array(mapp)

# 创建热力图
plt.figure(figsize=(8, 6))
plt.imshow(mapp, cmap='viridis', interpolation='nearest')

# 添加颜色条
#plt.colorbar(label='Value')


# 添加基础设施位置，用红色点标记
infrastructure_x, infrastructure_y = zip(*z)
plt.scatter(infrastructure_y, infrastructure_x, color='red', label='Infrastructure', edgecolors='black', s=100)

# 添加极端天气位置，用蓝色点标记
extreme_weather_x, extreme_weather_y = zip(*m)
plt.scatter(extreme_weather_y, extreme_weather_x, color='blue', label='Extreme Weather', edgecolors='black', s=100)



# 反转 y 轴，使原点 (0, 0) 出现在左上角
plt.gca().invert_yaxis()


# 设置轴标签和标题
plt.title("Demonstrate regional livability in three dimensions")
plt.xlabel("Y")
plt.ylabel("X")

# 显示网格
plt.xticks(range(1,101,10))
plt.yticks(range(1,101,10))
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)

# 显示图像
plt.show()



'''3D
mapp = np.array(mapp)

# 创建坐标网格
x, y = np.meshgrid(range(mapp.shape[1]), range(mapp.shape[0]))
z = np.zeros_like(x)  # 底部为 0
dx = dy = 0.8         # 柱宽
dz = mapp.ravel()     # mapp 的值作为柱子的高度

# 绘制三维柱状图
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(x.ravel(), y.ravel(), z.ravel(), dx, dy, dz, shade=True, cmap='viridis')

# 设置轴标签
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("habitability")

plt.title("habitability")
plt.show()
'''

mapp = np.array(mapp)

# 曲面图展示
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
x,y= np.meshgrid(range(1,101), range(1,101))
#从1开始


# 绘制曲面
surf = ax.plot_surface(x, y, mapp, cmap='viridis')

# 添加颜色条并设置为水平
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, orientation='horizontal', pad=0.1)

# 设置颜色条标签
cbar.set_label('habitability')

# 设置轴标签
ax.set_xlabel("X")
ax.set_ylabel("Y")
#ax.set_zlabel("habitability")


# 设置坐标范围，使 (0, 0) 显示在靠近的位置
ax.set_xlim(0, 99)
ax.set_ylim(0, 99)

# 设置视角（可调整以获得更好的效果）
ax.view_init(elev=30, azim=-120)  # elev 是仰角，azim 是方位角


plt.title("Demonstrate regional livability in three dimensions")
plt.show()
