import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


mapp=[[0]*10 for i in range(10)]
'''
print("请输入极端天气概率")
p=float(input())
print("请输入利润率")
r=float(input())
'''
p=[[0]*10 for _ in range(10)]
for i in range(10):
    for  j in range(10):
        if i<5 and j<5:
            p[i][j]=0.1
        elif i>=5 and j>=5:
            p[i][j]=0.4
        elif i>=5 and j<5:
            p[i][j]=0.2
        else:
            p[i][j]=0.2

r=[[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if (i==4 or i==5) and (j==5 or j== 6 or j==7):
            r[i][j]=4
        else:
             r[i][j]=3.76

z=[(1,4),(2,1),(3,2),(5,7),(6,6),(7,3)]
m=[(1,7),(2,8)]

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
    for i in range(4):
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
for i in range(10):
    for j in range(10):
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


'''
# 假设 mapp 已经计算完成
mapp = [[0]*10 for _ in range(10)]
# 示例数据（在实际运行中用你的计算结果替换此内容）
mapp = np.array(mapp)

# 创建热力图
plt.figure(figsize=(8, 6))
plt.imshow(mapp, cmap='viridis', interpolation='nearest')

# 添加颜色条
plt.colorbar(label='Value')

# 设置轴标签和标题
plt.title("mapp visual")
plt.xlabel("Y轴")
plt.ylabel("X轴")

# 显示网格
plt.xticks(range(10))
plt.yticks(range(10))
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)

# 显示图像
plt.show()
'''


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
