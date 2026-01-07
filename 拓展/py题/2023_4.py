from collections import deque,defaultdict

d=defaultdict(set)

n=int(input())

'''

不能双向！！！！
字典无法从values到keys

'''

for i in range(n):
    a,n1,b,n2=input().split()
    if n1==n2:
        d[a].add((b,0))
        #明显不能双向：否则会Yu 1 Yuci 0 Yuci 0 Yu 0 = Yu 1 Yu 0
        #d[b].add((a,0))#双向图?
        
    else:
        d[a].add((b,1))
        
        #d[b].add((a,1))
        
     
def get_nei(cur):
    neis=d[cur]
    return neis


def bfs(k):
    sta=end=k
    staq=deque([sta])
    endq=deque([end])
    vissta={sta:1}#用0，1表示相对性
    visend={end:0}


    presta={sta:None}#记录前驱节点
    preend={end:None}
    
    while staq and endq:
        ls=len(staq)
        le=len(endq)
        if ls<=le:
            for _ in range(ls):#当前层
                cur=staq.popleft()
                flag=vissta[cur]
                for nei,k in get_nei(cur): #解包
                    if k:
                        nflag= flag #0,1间取反
                    else:
                        nflag=not flag
                    if nei not in vissta:
                        vissta[nei]=nflag
                        staq.append(nei)

                        presta[nei]=cur
                        
                        if nei in visend and visend[nei]==vissta[nei]:
                            return build_path(nei,presta,preend)
        else:
            for _ in range(le):
                cur=endq.popleft()
                flag=visend[cur]
                for nei,k in get_nei(cur):
                    if k:
                        nflag=not flag #0,1间取反
                    else:
                        nflag=flag
                    if nei not in visend:
                        visend[nei]=nflag
                        endq.append(nei)

                        preend[nei]=cur
                        
                        if nei in vissta and vissta[nei]==visend[nei]:
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

print(d)

for i in d:
    k=bfs(i)
    print(k)


'''不能dfs：不知道何时停止
def dfs()
'''
