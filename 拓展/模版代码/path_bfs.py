from collections import deque

def bfs(sta):
    q=deque([sta])
    #vis={sta:0} 如果还需要输出长度的话用字典记录长度
    vis=set([sta])
    
    pre={sta:None}

    while q:
        cur=q.popleft()
        for nei in get_nei(cur):
            if nei not in vis:
                vis.add(nei)
                pre[nei]=cur

                if nei==end:
                    return buildpath(nei,pre)

def buildpath(i,pre):
    path=[]
    cur=i
    while cur!=None:
        path.append(cur)
        cur=pre[cur]

    path=path.reverse()
    return path

