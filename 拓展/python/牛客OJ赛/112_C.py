T=int(input())

n=[0]*T
m=[0]*T
k=[0]*T
q=[0]*T



for i in range(T):
    n[i],m[i],k[i],q[i]=map(int,input().split())

for i in range(T):
    up=m[i]*(k[i]-1)
    su=n[i]%k[i]
    
    flag=0
    
    if q[i]%k[i]==su and q[i]<=up:
        print('YES')

    else:
        print('NO')

'''
def dfs(step,summ,num,q,m):
    global flag

    if flag:
        return
    
    if step==m-1:
        last=summ-sum(num)
        print(num)
        if sum(num)==q:
            flag=1
        return

    
    new_step=step+1
    new_num=num.copy()
    
    for j in range(summ):
        new_num.append(j)
        new_summ=summ-j
        dfs(new_step,new_summ,new_num,q,m)
'''



'''
    if flag:
        print('YES')
    else:
        print('NO')
    




for i in range(T):
    if q[i]<=m[i]*(k[i]-1) and q[i]<=n[i]:
        print('YES')
    else:
        print('NO')


    summ=n[i]%(k[i]*m[i])

    flag=0
    
    for a in range(min(summ,k[i]+1)):
        if flag==1:
            break
        for b in range(a,min(summ-a+1,k[i]+1)):
            c=summ-a-b
            if flag:
                break

            if ((a+b)%k[i]+c)==q[i] or ((a+c)%k[i]+b)==q[i] or ((c+b)%k[i]+a)==q[i]:
                flag=1                

    if flag:
        print('YES')
    else:
        print('NO')
'''
