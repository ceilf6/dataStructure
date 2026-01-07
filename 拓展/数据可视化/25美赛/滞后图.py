import numpy as np
import matplotlib.pyplot as plt

# 上层食物限制系数
aP = 0.002
aI = 0.004
aI2 = 0.004
aS = 0.005
aBat = 0.005
aBird = 0.005

# 捕食系数和a一个数量级
bI = 0.002
bI2 = 0.002
bS = 0.001
bBat = 0.002
bBird = 0.001
bF = 0.001

# 竞争系数
cP = 0.018
cG = 0.02
cI = 0.007
cI2 = 0.005
cBat = 0.004
cBird = 0.004

# 自然死亡
dI, dI2, dS = 0.2, 0.18, 0.07
dBat, dBird = 0.08, 0.06
dF = 0.05

# 化学影响
wa = 1
wb = 0.5

# 初始数量
P0, G0, I0, I20, S0 = 10, 5, 2, 3, 1
Bat0, Bird0 = 1, 1
F0 = 1

# 自然增长
rP, rG, rI, rI2, rS = 3, 3.3, 2.9, 2.8, 2.5
rBat, rBird = 2.6, 2.4
rF = 2

# 限制
kP, kG, kI, kI2, kS = 100, 50, 20, 25, 10
kBat, kBird = 10, 8
kF = 5

# 设置时长和最大时间
dt = 0.1
T = 12
time_steps = int(T / dt)

# 初始化数量数组
P = np.zeros(time_steps)
G = np.zeros(time_steps)
I = np.zeros(time_steps)
I2 = np.zeros(time_steps)
S = np.zeros(time_steps)
F = np.zeros(time_steps)

# 初始值
P[0], G[0], I[0], I2[0], S[0], F[0] = P0, G0, I0, I20, S0, F0

# 动态更新公式
def P0_t(t):
    return rP * (1 - P[t-1] / kP) * P[t-1] - bI * I[t-1] * P[t-1]

def G0_t(t):
    return rG * (1 - G[t-1] / kG) * G[t-1]

def I0_t(t):
    return rI * (1 - I[t-1] / kI) * I[t-1] - dI * I[t-1] - bS * S[t-1] * I[t-1] - aP * P[t-1] * I[t-1]

def S0_t(t):
    return rS * (1 - S[t-1] / kS) * S[t-1] - dS * S[t-1] - aI * I[t-1] * S[t-1]

# 动态模拟
for t in range(1, time_steps):
    DP = P0_t(t) - bI2 * I2[t-1] * P[t-1]
    DG = G0_t(t) - cP * P[t-1] * G[t-1] - wa * G[t-1]
    DI = I0_t(t) - wb * I[t-1] - bBat * I[t-1]
    DI2 = rI2 * (1 - I2[t-1] / kI2) * I2[t-1] - dI2 * I2[t-1]
    DS = S0_t(t) - aI * I[t-1] * S[t-1]
    DF = rF * (1 - F[t-1] / kF) - dF * F[t-1]

    P[t] = P[t-1] + DP * dt / 5
    G[t] = G[t-1] + DG * dt / 5
    I[t] = I[t-1] + DI * dt / 5
    I2[t] = I2[t-1] + DI2 * dt / 5
    S[t] = S[t-1] + DS * dt / 5
    F[t] = F[t-1] + DF * dt / 5

# 滞后图绘制
variables = {
    "Crops": P,
    "Weeds": G,
    "Insects": I,
    "Voles": I2,
    "Secondary consumers": S,
    "Tertiary consumers": F
}
'''
# 自定义颜色字典
custom_colors = {
    "Crops (P)": "#D2A000",
    "Weeds (G)": "#8E6E3A",
    "Insects (I)": "#647B35",
    "Voles (I2)": "#56766E",
    "Secondary consumers (S)": "#2C7488",
    "Tertiary consumers (F)": "#85352F"
}
'''
custom_colors = {
    "Crops": "#FFCA21",
    "Weeds": "#D5BE98",
    "Insects": "#A2BE6A",
    "Voles": "#8BABA3",
    "Secondary consumers": "#62B5CC",
    "Tertiary consumers": "#E5B9B5"
}

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, (label, data) in enumerate(variables.items()):
    ax = axes[i]
    ax.plot(data[:-1], data[1:], marker='o', linewidth=2, label=label, color=custom_colors[label])
    ax.scatter(data[0], data[1], color="green", label="Start", s=80)
    ax.scatter(data[-2], data[-1], color="red", label="End", s=80)
    ax.set_xlabel('$y(t)$')
    ax.set_ylabel('$y(t+1)$')
    ax.set_title(f'Lag Diagram: {label}')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
