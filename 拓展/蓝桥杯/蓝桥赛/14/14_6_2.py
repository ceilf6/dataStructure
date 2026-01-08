from collections import deque

mod=998244353
def f_max(nums,k):
    q=deque()
    result=[]


    for current in range(len(nums)):
        while q and nums[current]>nums[q[-1]]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:#超出了左边界
            q.popleft()

        if current>=k-1:#形成窗口后记录最大值
            result.append(nums[q[0]])
    return result

def f_min(nums,k):
    q=deque()
    result=[]


    for current in range(len(nums)):
        while q and nums[current]<nums[q[-1]]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:#超出了左边界
            q.popleft()

        if current>=k-1:#形成窗口后记录最大值
            result.append(nums[q[0]])

    return result


print(f_min([1,2,3,4,7,3,2,4],3))
n,m,a,b=map(int,input().split())

A=[[]for i in range(n)]
for i in range(n):
    A[i]=list(map(int,input().split()))


summ=0
'''
#a*b的
maxx=[]
minn=[]
for i in range(n):
    maxx.append(f_max(A[i],a))
    minn.append(f_min(A[i],a))
#得到每行长a的，总共m-a+1个的数组
maxx2=[]
minn2=[]

        #现求a列的max中b行的max

for z in range(n-b+1): 
    for i in range(m-a+1):
        ma=[]
        mi=[]
        for j in range(b):
            ma.append(maxx[z+j][i])
            mi.append(minn[z+j][i])
        maxx2.append(f_max(ma,b))
        minn2.append(f_min(mi,b))

for i in range(len(maxx2)):
    for j in range(len(maxx2[0])):
        summ=(summ+maxx2[i][j]*minn2[i][j])%mod
print(maxx2,minn2)
'''
#b*a的
maxx=[]
minn=[]
for i in range(n):
    maxx.append(f_max(A[i],b))
    minn.append(f_min(A[i],b))
#得到每行长a的，总共m-a+1个的数组
maxx2=[]
minn2=[]

        #现求a列的max中b行的max

for z in range(n-a+1): 
    for i in range(m-b+1):
        ma=[]
        mi=[]
        for j in range(a):
            ma.append(maxx[z+j][i])
            mi.append(minn[z+j][i])
        maxx2.append(f_max(ma,a))
        minn2.append(f_min(mi,a))
#print(maxx2,minn2)
for i in range(len(maxx2)):
    for j in range(len(maxx2[0])):
        summ=(summ+maxx2[i][j]*minn2[i][j])%mod

print(summ)
'''
#b*a的
maxx3=[]
minn3=[]
for i in range(n):
    maxx3.append(f_max(A[i],b))
    minn3.append(f_min(A[i],b))
#得到每行长a的，总共m-a+1个的数组
maxx4=[]
minn4=[]

        #现求a列的max中b行的max

for z in range(n-a+1): 
    for i in range(m-b):
        ma=[]
        m=0
        mi=[]
        m2=float('inf')
        for j in range(a):
            m=max(m,max(maxx3[i]))
            m2=min(m2,min(minn3[i]))
        ma.append(m)
        mi.append(m2)
    maxx4.append(ma)
    minn4.append(mi)

for i in range(len(maxx4)):
    for j in range(len(maxx4[0])):
        summ=(summ+maxx4[i][j]*minn4[i][j])%mod

print(summ)
    
'''
'''
for i in range(n):
    ma=0
    mi=float('inf')
    for j in range(b):
        ma=max(ma,maxx[i][j])
        mi=min(mi,minn[i][j])
    summ=(summ+ma*mi)%998244353

maxx2=[]
minn2=[]
for i in range(n):
    maxx2.append(f_max(A[i],b))
    minn2.append(f_min(A[i],b))

for i in range(n):
    ma=0
    mi=float('inf')
    for j in range(a):#上面已经有b了，现在a列
        ma=max(ma,maxx[i][j])
        mi=min(mi,minn[i][j])
    summ=(summ+ma*mi)%998244353

print(summ)
'''
