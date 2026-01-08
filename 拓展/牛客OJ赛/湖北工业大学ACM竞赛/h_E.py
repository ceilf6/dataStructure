N=int(input())

LR=[[]for i in range(N)]
for i in range(N):
    LR[i]=(list(map(int,input().split())))
flag=0
def dfs(step,chose):
    global flag
    if flag:
        return
    
    if step==N and sum(chose)==0:
        print('YES')
        for i in range(len(chose)):
            print(chose[i],end=' ')
        flag=1
        return
    
    if step==N:
        return
    
    for i in range(LR[step][0],LR[step][1]+1):
        new_chose=chose.copy()
        new_chose.append(i)
        dfs(step+1,new_chose)

dfs(0,[])
if not flag:
    print('NO')
