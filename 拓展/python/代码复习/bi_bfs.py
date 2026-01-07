def bi_bfs(sta,end,get_nei):
    if sta==end:
        return 0
    staq=deque([sta])
    endq=deque([end])
    visend={end:0}
    vissta={sta:0}

    while staq and endq:
        if len(staq)<=len(endq):
            for _ in range(len(staq)):
                cur=staq.popleft()
                curstep=vissta[cur]
                for nei in get_nei(cur):
                    if nei not in vissta:
                        vissta[nei]=curstep+1
                        staq.append(nei)
                        if nei in visend:
                            return visend[nei]+vissta[nei]
        else:
            
