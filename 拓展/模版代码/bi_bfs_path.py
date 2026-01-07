from collections import deque,defaultdict
     
def bfs(sta,end):
    staq=deque([sta])
    endq=deque([end])
    vissta=set(sta)
    visend=set(end)

    presta={sta:None}#记录前驱节点
    preend={end:None}
    
    while staq and endq:
        ls=len(staq)
        le=len(endq)
        if ls<=le:
            for _ in range(ls):#当前层
                cur=staq.popleft()
                
                for nei in get_nei(cur): #解包
                    if nei not in vissta:
                        vissta.add(nei)
                        staq.append(nei)

                        presta[nei]=cur
                        
                        if nei in visend:
                            return build_path(nei,presta,preend)
        else:
            for _ in range(le):
                cur=endq.popleft()
                
                for nei in get_nei(cur):
                    if nei not in visend:
                        visend.add(nei)
                        endq.append(nei)

                        preend[nei]=cur
                        
                        if nei in vissta:
                            return build_path(nei,presta,preend)
    return 0


def build_path(meet,presta,preend):
    path_sta=[]
    cur=meet
    while cur is not None:#开始链表回溯
        path_sta.append(cur)
        cur=presta[cur]
    path_sta.reverse()#掉头，方面后面衔接

    path_end=[]
    cur=preend[meet]
    while cur is not None:
        path_end.append(cur)
        cur=preend[cur]

    return path_sta+path_end

