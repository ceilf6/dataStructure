n=int(input())


INF=float('inf')
ma=[]


for i in range(n):
    temp=input()
    temp=temp.replace('-1','inf')
    #print(temp)
    ma.append(list(map(float,temp.split()))) ##float

#print(ma)

shui=list(map(int,input().split()))

s=[]
while 1:
    temp=list(map(int,input().split()))
    if temp[0]==temp[1]==-1:
        break
    s.append(temp)

#用链表存储前驱-->路径
    
pre = [[i for j in range(n)] for i in range(n)]
print(pre)



def floyd(ma):#直接获得任意两点之间的最小cost
    
    d=[[ma[i][j] for j in range(n)]for i  in range(n)]

    for k in range(n):#中间节点：shui[k]
        for i in range(n):
            for j in range(n):
                #if d[i][k]!=-1 and d[k][j]!=-1:
                if d[i][j] > d[i][k] + d[k][j] + shui[k]:#更新判断
                    d[i][j] = d[i][k] + d[k][j] + shui[k]#shui:直接加在点上
                    pre[i][j] = pre[k][j]

    return d

def buildpath(i, j):
    path = [j]
    while i != j:
        j = pre[i][j]
        path.append(j)
    path.reverse()#因为是从终点往前：得掉个头
    return path


d=floyd(ma)

for i,j in s:
    print(f'From {i} to {j} :')
    i-=1
    j-=1
    path=buildpath(i,j)
    print('Path:','-->'.join(str(x+1) for x in path))
    print('Total cost :',int(d[i][j]))

    print()
