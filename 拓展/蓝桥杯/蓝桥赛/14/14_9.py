T=int(input())

n=[0]*T
m=[0]*T
k=[0]*T

for i in range(T):
    n[i],m[i],k[i]=map(int,input().split())

for i in range(T):
    t=m[i]
    summ=[0]
    step=0
    
    while summ[-1]<k[i]:
        summ.append(summ[-1]+t**step)
        step+=1

    nstep=step

    while summ[-1]<n[i]:
        summ.append(summ[-1]+t**nstep)
        nstep+=1

    step-=1
    nstep-=1

    
    num=1
    for j in range(1,nstep-step):
        num+=t**j

    #剩下最后一层的

    I=k[i]-summ[step-1]-1


    left=0

    if I>0:
        left=n[i]-I*t**(nstep-step)-summ[nstep-1]

    if left>0:
        if left<t**(nstep-step):#是从子树头开始往下增加！
            num+=left
        else:
            num+=t**(nstep-step)


    print(num)
