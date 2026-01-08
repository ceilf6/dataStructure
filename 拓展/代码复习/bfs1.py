def bfs(start,target,get_nei):
    if start==target:
        return 0

    queue=deque([start])

    vis={start:0}

    while queue:
        cur=queue.popleft()
        cur_steps=vis[cur]

        if cur==target:
            return cur_steps

        for nei in get_nei(cur):
            if nei not in vis:
                vis[nei]=cur_step+1
                queue.append(nei)

    return -1

def get_nei(pos):
    x,y=pos

    neis=[]

    for dx,dy in [[]]:
        nx,ny=
        if

    return neis
