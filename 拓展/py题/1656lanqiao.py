n=int(input())


INF=float('inf')
ma=[]


for i in range(n):
    temp=input()
    temp=temp.replace('-1','inf')
    #print(temp)
    ma.append(list(map(float,temp.split())))

#print(ma)

shui=list(map(int,input().split()))

s=[]
while 1:
    temp=list(map(int,input().split()))
    if temp[0]==temp[1]==-1:
        break
    s.append(temp)


#shui:直接加在点上？


#用链表存储前驱-->路径
    #第一个元素得预构造0（或者用字典，但是我感觉二维数组更直观）
pre=[[0]*n for i in range(n)]
for i in range(n):
    pre[i][i]=i+1



def floyd(ma):#直接获得任意两点之间的最小cost
    
    d=[[ma[i][j] for j in range(n)]for i  in range(n)]

    for k in range(n):#“城市的税”：shui[k]
        for i in range(n):
            for j in range(n):
                #if d[i][k]!=-1 and d[k][j]!=-1:
                if d[i][j]>(d[i][k]+d[k][j]+shui[k]):#更新前驱,而且要求字典序最小？
                    d[i][j]=d[i][k]+d[k][j]+shui[k]
                    pre[i][j]=[pre[i][k]]+[k]+[pre[k][j]]

    return d

d=floyd(ma)
for i in d:
    print(*i)

for j in pre:
    print(*j)



    
'''
for i in range(n):
    ma.append(list(map(int,input().split())))

shui=list(map(int,input().split()))

s=[]
while 1:
    temp=list(map(int,input().split()))
    if temp[0]==temp[1]==-1:
        break
    s.append(temp)


#shui:直接加在点上？
'''

'''
pre=[[]]

def floyd(ma):#直接获得任意两点之间的最小cost
    d=[[ma[i][j] for j in range(n)]for i  in range(n)]

    for k in range(n):#“城市的税”：shui[k]
        for i in range(n):
            for j in range(n):
                if d[i][k]!=-1 and d[k][j]!=-1:
                    d[i][j]=min(d[i][j],d[i][k]+d[k][j]+shui[k])

    return d

d=floyd(ma)
for i in d:
    print(*i)
'''
