'''
01背包模版代码
'''
def ZOpack(F, c, w):                
    for j in range(V, c-1, -1):     #V是背包容量上限
        F[j] = max(F[j], F[j-c] + w)
