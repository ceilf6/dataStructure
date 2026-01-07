import heapq

n,m=map(int,input().split())

s=[]
for i in range(n):
    s.append(tuple(map(int,input().split())))
            #用tuple才方便下面解包

hp=[]#直接用数组初始化即可
for i in range(len(s)):#从x等于1开始平行初始化
    a,b,c=s[i]
    fnow=a*1**2+b*1*1+c
    heapq.heappush(hp,(fnow,i,1))
                    #元素：值，fi，x

res=[]
for j in range(m):
    val,i,x=heapq.heappop(hp)
    res.append(val)
    a,b,c=s[i]
    newx=x+1
    fnow=a*newx**2+b*newx+c
    heapq.heappush(hp,(fnow,i,newx))

print(*res)
