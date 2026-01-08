n=int(input())

def dis(a,b):#a到b单向
    x1,y1,d1=a
    x2,y2,d2=b
    if (x1-x2)**2+(y1-y2)**2 <= d1**2:
        return 1
    else:
        return 0

te=[]
for i in range(n):
    te.append(tuple(map(int,input().split())))
            # 用tuple才能在dis中解包


con=[[0] for i in range(n)]
#预处理
for i in range(n):
    for j in range(n):
        con[i][j]=dis(te[i],te[j])

#floyd 考虑中介点情况
for k in range(n):
    for i in range(n):
        for j in range(n):
            con[i][j] = con[i][j] or (con[i][k] and con[k][j])
    

'''不能按列统计：我们存储的是行的可能性
# 计算结果 - 按列计算
ans = 0
for j in range(n):  # 遍历列
    vis = 0
    for i in range(n):  # 遍历每列中的行
        vis += con[i][j]  # 累加这一列中的值
    ans = max(ans, vis)  # 更新最大值

print(ans)  # 输出结果
'''