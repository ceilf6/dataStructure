from math import ceil
n=int(input())

a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())


maxx=0
def dfs(step,chose,cn):
    global maxx

    if cn==n//2:
        summ=0
        for i in chose:
            summ+=a[i]-b[i]
        summ+=sum(b)
        if summ>=maxx:
            maxx=summ
        return

    if step==n:
        return

    new_chose=chose.copy()
    new_chose.append(step)
    dfs(step+1,new_chose,cn+1)

    dfs(step+1,chose,cn)

dfs(0,[],0)

print(maxx)
        
    
