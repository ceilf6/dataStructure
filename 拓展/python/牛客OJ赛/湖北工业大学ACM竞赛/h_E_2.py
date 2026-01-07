N=int(input())

LR=[[]for i in range(N)]
for i in range(N):
    LR[i]=(list(map(int,input().split())))

flag=0

def spread(a,l,r ):
    if a < l:
        return 1
    if a>r:
        return 2
    
    yield a
    max_offset = max(a - l, r - a)
    for offset in range(1, max_offset + 1):
        right = a + offset
        if right <= r:
            yield right
        left = a - offset
        if left >= l:
            yield left

def dfs(step,chose,summ):
    global flag
    if flag:
        return
    if step==N-1 and LR[N-1][0]<=-summ<=LR[N-1][1]:
        print('YES')
        for i in range(len(chose)):
            print(chose[i],end=' ')
        print(-summ)
        flag=1
        return
    if step==N-1:
        return

    if step>=1:
        if spread(-summ,LR[step][0],LR[step][1])==1:
            for i in range(LR[0][0],LR[0][1]+1):
                new_chose=chose.copy()
                new_chose.append(i)
                dfs(step+1,new_chose,summ+i)
        elif spread(-summ,LR[step][0],LR[step][1])==2:
            for j in range(LR[0][1],LR[0][0]-1,-1):
                new_chose=chose.copy()
                new_chose.append(j)
                dfs(step+1,new_chose,summ+j)
        else:
            for q in list(spread(-summ,LR[step][0],LR[step][1])):
                new_chose=chose.copy()
                new_chose.append(q)
                dfs(step+1,new_chose,summ+q)
    else:
        for p in range(LR[0][0],LR[0][1]+1):
            new_chose=chose.copy()
            new_chose.append(p)
            dfs(step+1,new_chose,summ+p)
dfs(0,[],0)
if not flag:
    print('NO')
