from collections import deque,defaultdict

edges=defaultdict(list)

n=int(input())

for i in range(n):#邻接表
    a,fa,b,fb=input().split()
    fa,fb=int(fa),int(fb)
    edges[(a,fa)]=(b,fb)#数组不能当作key，元组可以

path=None

nodes=set()#set自动去重
for key in edges:
    nodes.add(key[0])#出发点
    for b,_ in edges[key]:
        nodes.add(b)#到达点

nodes=list(nodes)

for sta in nodes:#遍历所有点
    for stastate in [0,1]:#两种起始状态0,1
        targetstate=1-stastate #目标状态：逆状态
        vis={}
        q=deque()
        q.append((sta,stastate,[]))#队列元素：当前节点，当前状态，路径
        vis[(sta,stastate)]=True
        found=False
        while q and not found:
            cur,curstate,path=q.popleft()
            if cur==sta and curstate==targetstate:#形成闭环，而且状态符合要求
                if path is None or len(path)                 

