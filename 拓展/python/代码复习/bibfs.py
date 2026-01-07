def bi_bfs(sta,end,get_nei):
    if sta == end:
        return 0
    staq=deque([sta])
    endq=deque([end])
    vissta={sta:0}
    visend={end:0}
    while staq and endq:
        if len(staq)<=len(endq):
            for i in range(len(staq)):
                cur=staq.popleft()
                cursteps=vissta[cur]
                for nei in get_nei(cur):
                    if nei not in vissta:
                        vissta[nei]=cursteps+1
                        staq.append(nei)
                        if nei in visend:
                            return visend[nei]+vissta[nei]
        else:
            for i in range(len(endq)):
                cur=endq.popleft()
                cursteps=visend[cur]
                for nei in get_nei(cur):
                    if nei not in visend:
                        visend[nei]=cursteps+1
                        endq.append(nei)
                        if nei in vissta:
                            return visend[nei]+vissta[nei]
    return -1
