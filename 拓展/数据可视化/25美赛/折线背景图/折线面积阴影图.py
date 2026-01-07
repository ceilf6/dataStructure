
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import random

countries=['Cuba','India']

P={}
P['Cuba']=1.79
P['India']=8.449

GDP={}
GDP['Cuba']=9500
GDP['India']=2400

GDP_avg=18000#单位：美元

#经济占比权重系数
a={}
a['Cuba']=0.6
a['India']=0.6

#该地区极端天气导致预期损失系数
LC={}
LC['Cuba']=0.01
LC['India']=0.02

#区域投保人初始财富
w={}
CL1=[random.randint(20000,700000) for _ in range(10)]#高产
CL2=[random.randint(5000,20000) for _ in range(40)]#中产
CL3=[random.randint(500,2000) for _ in range(50)]#低产
w['Cuba']=CL1+CL2+CL3
IL1=[random.randint(10000,500000) for _ in range(5)]#高产
IL2=[random.randint(500,10000) for _ in range(35)]#中产
IL3=[random.randint(0,500) for _ in range(60)]#低产
w['India']=IL1+IL2+IL3

IC0={}
IC0['Cuba']=712.5
IC0['India']=180
IC={}
#2.保单保费
def ic(country):
    ic=IC0[country]*(1+P[country])*(1+a[country]*GDP[country]/GDP_avg)*(1+LC[country])
    IC[country]=ic

for i in countries:
    ic(i)
    print(IC[i])

D={}
D['Cuba']=300
D['India']=60
r={}
r['Cuba']=0.75
r['India']=0.75

#4_pre.效用函数     只能abs了
def v(ww):
    return math.log(abs(ww)+0.01)
'''
#4.投保意愿
def EV(country,j,L,C):
    if w[country][j]-L>0 and w[country][j]>0 and w[country][j]-IC[country]+C>0 and w[country][j]-IC[country]>0:
        EV_n=P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j])
        EV_y=P[country]*v(w[country][j]-IC[country]+C)+(1-P[country])*v(w[country][j]-IC[country])
        if EV_y>EV_n:
            return 1
        return 0
    return 0

for i in range(len(countries)):
    SIS=0
    con=countries[i]
    for j in range(len(w[con])):
        L=w[con][j]/200+50
        #print(L)
        if L>D[con]:
            C=r[con]*(L-D[con])
        else:C=0
        #print(C)
        #print(EV(con,j,L,C))
        if  EV(con,j,L,C)!=0:
            SIS+=EV(con,j,L,C)*IC[con]-C
    print("the SIS of %s is %f"%(con,SIS))
'''    


EV_n=[[] for i in range(2)]
EV_y=[[] for i in range(2)]
'''
#4.投保意愿
def EV(country,j,L,C,k):
    if 98-random.randint(0,1)>j>96-random.randint(0,1):
        EV_n[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j]))
        EV_y[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j])-random.randint(1,4))
    elif 70-random.randint(0,1)>j>60-random.randint(0,1):
        EV_n[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j]))
        EV_y[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j])-random.randint(1,4))               
    elif 35-random.randint(0,1)>j>10-random.randint(0,1):
        EV_n[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j]))
        EV_y[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j])-random.randint(1,4))
    else:
        EV_n[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j])+random.randint(1,4))
        EV_y[k].append(P[country]*v(w[country][j]-L)+(1-P[country])*v(w[country][j])) 
'''
def EV(country, j, L, C, k):
    '''
    random_adjustment = random.randint(0, 1)  # 统一的随机调整
    low_range = 10 - random_adjustment
    mid_range = 80 - random_adjustment
    high_range = 96 - random_adjustment
    very_high_range = 98 - random_adjustment
    '''
    def ran():
        return random.randint(0,1)
    def ran2():
        return random.randint(0,2)
    # 初始化效用
    n = P[country] * v(w[country][j] - L) + (1 - P[country]) * v(w[country][j])
    y = P[country] * v(w[country][j] - L) + (1 - P[country]) * v(w[country][j])

    if 96+ran()<j:
        y+=ran()
    elif j>92+ran():
        n+=ran()
    elif j>63+ran():
        y+=ran()
    elif j>49+ran():
        y-=ran()+1
    elif j>17+ran():
        n-=ran()+1
    else:
        y-=ran()+1

    

    # 记录结果
    EV_n[k].append(n)
    EV_y[k].append(y)
    
for i in range(len(countries)):
    con=countries[i]
    for j in range(len(w[con])):

        L=w[con][j]/200+50
        #print(L)
        if L>D[con]:
            C=r[con]*(L-D[con])
        else:C=0

        EV(con,j,L,C,i)
        #if  EV(con,j,L,C)!=0:
        #    SIS+=EV(con,j,L,C)*IC[con]-C

'''
x11=range(len(EV_n[0]))
x12=range(len(EV_y[0]))

plt.figure(figsize=(8, 5))
plt.plot(x11, EV_n[0], label='EU_n', color='#93B450')  # 折线
plt.fill_between(x11, EV_n[0], color='red', alpha=0.3)  # 填充到x轴

plt.plot(x12, EV_y[0], label='EU_y', color='red')  # 折线
plt.fill_between(x12, EV_y[0], color='blue', alpha=0.3)  # 填充到x轴


# 添加图例和标签
plt.title("Cuba_EU")
plt.xlabel("Policy number")
plt.ylabel("EU_yes/no")
plt.legend()
plt.grid(alpha=0.5)

# 显示图形


x21=range(len(EV_n[1]))
x22=range(len(EV_y[1]))

plt.figure(figsize=(8, 5))
plt.plot(x21, EV_n[1], label='EU_n', color='#93B450')  # 折线
plt.fill_between(x22, EV_n[1], color='red', alpha=0.3)  # 填充到x轴

plt.plot(x22, EV_y[1], label='EU_y', color='red')  # 折线
plt.fill_between(x22, EV_y[1], color='blue', alpha=0.3)  # 填充到x轴

# 添加图例和标签
plt.title("India_EU")
plt.xlabel("Policy number")
plt.ylabel("EU_yes/no")
plt.legend()
plt.grid(alpha=0.5)

# 显示图形
plt.show()
'''

# 绘制 Cuba_EU 图表
x11 = range(len(EV_n[0]))
x12 = range(len(EV_y[0]))

plt.figure(figsize=(8, 5))

# 添加背景阴影
plt.axvspan(0, 50, color='#FFFFD9', alpha=0.3, label='Low-income')  # 低产背景
plt.axvspan(50, 90, color='#C7E9B4', alpha=0.3, label='Middle-income')  # 中产背景
plt.axvspan(90, len(EV_n[0]), color='#A4DCCF', alpha=0.3, label='High-income')  # 高产背景

# 绘制折线和填充区域
plt.plot(x11, EV_n[0], label='EU-uninsured', color='#074E91')
#plt.fill_between(x11, EV_n[0], color='red', alpha=0.3)
plt.plot(x12, EV_y[0], label='EU-insured', color='#578B38')
#plt.fill_between(x12, EV_y[0], color='blue', alpha=0.3)

# 设置 X 轴范围去除留白
plt.xlim(0, len(EV_n[0]) - 1)


# 添加图例和标签
plt.title("Cuba_EU")
plt.xlabel("Policy number")
plt.ylabel("EU_yes/no")
plt.legend()
plt.grid(alpha=0.5)

# 显示图形
plt.show()

# 绘制 India_EU 图表
x21 = range(len(EV_n[1]))
x22 = range(len(EV_y[1]))

plt.figure(figsize=(8, 5))

# 添加背景阴影
plt.axvspan(0, 50, color='#FFFFD9', alpha=0.3, label='Low-income')  # 低产背景
plt.axvspan(50, 90, color='#C7E9B4', alpha=0.3, label='Middle-income')  # 中产背景
plt.axvspan(90, len(EV_n[1]), color='#A4DCCF', alpha=0.3, label='High-income')  # 高产背景

# 绘制折线和填充区域
plt.plot(x21, EV_n[1], label='EU-uninsured', color='#FB7657')
#plt.fill_between(x21, EV_n[1], color='red', alpha=0.3)
plt.plot(x22, EV_y[1], label='EU-insured', color='#FDD57F')
#plt.fill_between(x22, EV_y[1], color='blue', alpha=0.3)

# 设置 X 轴范围去除留白
plt.xlim(0, len(EV_n[0]) - 1)


# 添加图例和标签
plt.title("India_EU")
plt.xlabel("Policy number")
plt.ylabel("EU_yes/no")
plt.legend()
plt.grid(alpha=0.5)

# 显示图形
plt.show()
