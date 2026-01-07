from collections import deque,defaultdict

n=int(input())
d=defaultdict(list)

for i in range(n):
    a,n1,b,n2=input().split()

    d[(a,n1)].append((b,n2))

print(d)


def bfs(sta):
    end=sta

    vis=

    q=deque([sta])
    #vis={sta:0} 如果还需要输出长度的话用字典记录长度
    vis={sta:0}
    
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

