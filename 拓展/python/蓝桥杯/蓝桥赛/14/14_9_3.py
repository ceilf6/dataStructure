T=int(input())

n=[0]*T
m=[0]*T
k=[0]*T

for i in range(T):
    n[i],m[i],k[i]=map(int,input().split())

num1=[]
num2=[]

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
        left=n[i]-(I)*(t**(nstep-step))-summ[nstep-1]

    if step!=nstep:
        if left>0:
            if left<t**(nstep-step):#是从子树头开始往下增加！
                num+=left
            else:
                num+=t**(nstep-step)

    num1.append(num)



def compute_subtree_size(n, m, k):
    if m == 1:
        return max(n - k + 1, 0)
    total = 0
    layer = 0
    while True:
        m_power=m**layer
        # 计算当前层的起始结点s
        s = m_power * (k - 1) + (m_power - 1) // (m - 1) + 1
        if s > n:
            break
        # 当前层结束结点e = s + m^layer - 1
        e = s + m_power - 1
        if e <= n:
            total += m_power
        else:
            total += (n - s + 1)
            break
        layer += 1
    return total


for i in range(T):
    a,b,c=n[i],m[i],k[i]
    num2.append(compute_subtree_size(a,b,c))

print(num1)
print(num2)
