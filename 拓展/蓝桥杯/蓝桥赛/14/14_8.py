n,m=map(int,input().split())

num=0
MOD=998244353

def dfs(step,summ,last):
    global num

    if step>=6:
        summ-=last[step-5]

    if summ>m:
        return
    
    if step>=n:
        num=(num+1)%998244353
        print(last)
        return

    if step==1:
        if n%2==1:
            for i in range(1,11,2):
                last=[0,i]
                dfs(1,i,last)
                last.pop()
        else:
            for i in range(2,10,2):
                last=[0,i]
                dfs(1,i,last)
                last.pop()
    else:

        if step%2==1:#下一位为偶
            for i in range(2,10,2):
                last.append(i)
                dfs(step+1,summ+i,last)
                last.pop()#回溯
        else:
            for i in range(1,11,2):
                last.append(i)
                dfs(step+1,summ+i,last)
                last.pop()
                
dfs(1,0,[])

print(num)
    
'''
def bfs(f,step,summ,last):
    global num
    
    if summ>m:
        return

    if step==n+1:
        num+=1
        return
    
    
    if step==1:
        if f==1:
            for i in range(1,11,2):
                last.append(i)
                bfs(2,2,summ+i,i,1)
        else:
            for i in range(2,10,2):
                bfs(1,2,summ+i,i,1)
    else:
        if l==5:
            if f==1:
                for i in range(1,11,2):
                    bfs(2,step+1,summ+i-last,l)
            else:
                for i in range(0,10,2):
                    bfs(1,step+1,summ+i)
        else:
            if f==1:
                for i in range(1,11,2):
                    bfs(2,step+1,summ+i,l+1)
            else:
                for i in range(0,10,2):
                    bfs(1,step+1,summ+i,l+1)

if n%2==1:
    bfs(1,1,m,0,0)
else:
    bfs(2,1,m,0,0)

print(num)
'''

'''
summ=0
if n%2==1:
    for i in range(1,11,2):
        last=i
        lsati=1
        summ+=i
        if summ>=m:
            continue
        for l in range(2,n+1):
            if l%2==0:
                for j in range(2,10,2):
                    summ+=j
            else:
                for z in range(1,11,2):
                    summ+=z
                    
            

    

        for j in range(2,10,2):
            summ+=j
            for z in range(
'''
